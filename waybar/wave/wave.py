#!/usr/bin/env python3
"""
Living line wave overlay for Waybar on Hyprland (X11 fallback version)
"""

import os
import sys
import math
import socket
import time
import subprocess
from dataclasses import dataclass
from typing import Tuple

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkX11', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkX11
import cairo

# ===== CONFIGURATION =====
BAR_HEIGHT = 46
WAVE_HEIGHT = 18
WAVE_RADIUS = 120
REVEAL_DISTANCE = 40
RIPPLE = 0.6
RIPPLE_SPEED = 0.3
EASE_POS = 0.15
EASE_AMP = 0.08
ACTIVE_HZ = 60
IDLE_HZ = 10

COL_LINE = (1.0, 1.0, 1.0, 0.4)
COL_CREST = (0.8, 0.7, 1.0, 0.6)
GLOW = (0.4, 0.3, 0.8, 0.15)

# =========================

@dataclass
class WaveState:
    target_x: float = 0.0
    current_x: float = 0.0
    target_amp: float = 0.0
    current_amp: float = 0.0
    phase: float = 0.0
    active: bool = False


class HyprlandIPC:
    def __init__(self):
        self.socket_path = os.getenv('HYPRLAND_INSTANCE_SIGNATURE')
        if not self.socket_path:
            self.socket_path = self._find_socket()
        self.sock = None
        
    def _find_socket(self) -> str:
        import glob
        sockets = glob.glob('/tmp/hypr/*/.socket.sock')
        if sockets:
            return sockets[0].replace('/.socket.sock', '')
        return '/tmp/hypr/{}'.format(os.getenv('USER', 'user'))
    
    def get_cursor_position(self) -> Tuple[float, float]:
        try:
            if not self.sock:
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.sock.connect(f'{self.socket_path}/.socket.sock')
            
            self.sock.send(b'cursorpos\n')
            data = self.sock.recv(1024).decode().strip()
            
            if data.startswith('cursorpos:'):
                parts = data.split()[1:]
                if len(parts) >= 2:
                    return float(parts[0]), float(parts[1])
        except:
            try:
                result = subprocess.run(
                    ['hyprctl', 'cursorpos'],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    parts = result.stdout.strip().split()
                    if len(parts) >= 2:
                        return float(parts[0]), float(parts[1])
            except:
                pass
        
        return 0.0, 0.0


class WaveOverlay(Gtk.Window):
    def __init__(self):
        super().__init__()
        
        self.state = WaveState()
        self.hypr = HyprlandIPC()
        self.last_update = time.time()
        self.display_width = 0
        self.display_height = 0
        
        # Setup window
        self.set_title('waybar-wave')
        self.set_decorated(False)
        self.set_resizable(False)
        self.set_keep_above(True)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_app_paintable(True)
        
        # Set transparent background
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)
        
        # Make window fullscreen
        self.fullscreen()
        
        # Connect signals
        self.connect('draw', self.on_draw)
        self.connect('size-allocate', self.on_resize)
        
        # Make window click-through using X11
        self._make_click_through()
        
        # Start animation
        self.tick()
        
        # Show window
        self.show_all()
        
        print("✅ Wave window created (X11 fallback mode)")
    
    def _make_click_through(self):
        """Make window click-through using X11 attributes"""
        try:
            gdk_window = self.get_window()
            if gdk_window:
                x11_window = gdk_window.get_xid()
                if x11_window:
                    # Use xprop to set window attributes
                    cmd = [
                        'xprop', '-id', str(x11_window),
                        '-f', '_NET_WM_WINDOW_TYPE', '32a',
                        '-set', '_NET_WM_WINDOW_TYPE', '_NET_WM_WINDOW_TYPE_DOCK'
                    ]
                    subprocess.run(cmd, check=False)
                    
                    # Set input region to empty (click-through)
                    cmd = [
                        'xprop', '-id', str(x11_window),
                        '-f', '_NET_WM_INPUT_REGION', '32a',
                        '-set', '_NET_WM_INPUT_REGION', '0,0,0,0'
                    ]
                    subprocess.run(cmd, check=False)
                    print("✅ Click-through enabled")
        except Exception as e:
            print(f"⚠️  Could not set click-through: {e}")
    
    def on_resize(self, widget, allocation):
        self.display_width = allocation.width
        self.display_height = allocation.height
        if self.display_width > 100:  # Only log real sizes
            print(f"📐 Window: {self.display_width}x{self.display_height}")
    
    def tick(self):
        now = time.time()
        dt = now - self.last_update
        self.last_update = now
        
        x, y = self.hypr.get_cursor_position()
        self._update_wave(x, y, dt)
        
        self.queue_draw()
        
        fps = ACTIVE_HZ if self.state.active else IDLE_HZ
        GLib.timeout_add(int(1000 / fps), self.tick)
    
    def _update_wave(self, cursor_x: float, cursor_y: float, dt: float):
        bar_bottom = self.display_height - BAR_HEIGHT
        distance = cursor_y - bar_bottom
        
        if -REVEAL_DISTANCE < distance < 50:
            self.state.target_x = cursor_x
            self.state.target_amp = WAVE_HEIGHT * (1 - max(0, distance) / REVEAL_DISTANCE)
            self.state.active = True
        else:
            self.state.target_x = cursor_x
            self.state.target_amp = 0
            self.state.active = False
        
        self.state.current_x += (self.state.target_x - self.state.current_x) * EASE_POS
        self.state.current_amp += (self.state.target_amp - self.state.current_amp) * EASE_AMP
        
        if self.state.active and self.state.current_amp > 0.5:
            self.state.phase += dt * RIPPLE_SPEED * 2 * math.pi
        else:
            self.state.phase = 0
    
    def on_draw(self, widget, cr: cairo.Context):
        if self.display_width == 0:
            return
        
        # Clear with transparency
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)
        
        if self.state.current_amp < 0.5:
            return
        
        self._draw_wave(cr)
    
    def _draw_wave(self, cr: cairo.Context):
        width = self.display_width
        amp = self.state.current_amp
        center_x = self.state.current_x
        phase = self.state.phase
        
        center_x = max(0, min(width, center_x))
        
        step = 3
        points = []
        
        for x in range(0, width, step):
            dist = x - center_x
            envelope = math.exp(-(dist * dist) / (WAVE_RADIUS * WAVE_RADIUS))
            ripple_factor = 1.0 + RIPPLE * math.sin(dist * 0.05 + phase) * envelope
            y = BAR_HEIGHT - amp * envelope * ripple_factor * 0.8
            points.append((x, y))
        
        if not points:
            return
        
        # Fill glow
        cr.save()
        cr.new_path()
        cr.move_to(points[0][0], BAR_HEIGHT)
        for x, y in points:
            cr.line_to(x, y)
        cr.line_to(points[-1][0], BAR_HEIGHT)
        cr.close_path()
        
        pat = cairo.LinearGradient(0, BAR_HEIGHT - amp, 0, BAR_HEIGHT)
        pat.add_color_stop_rgba(0, GLOW[0], GLOW[1], GLOW[2], GLOW[3])
        pat.add_color_stop_rgba(1, GLOW[0], GLOW[1], GLOW[2], 0)
        cr.set_source(pat)
        cr.fill()
        cr.restore()
        
        # Crest glow
        cr.save()
        cr.new_path()
        for i, (x, y) in enumerate(points):
            if i == 0:
                cr.move_to(x, y)
            else:
                cr.line_to(x, y)
        
        cr.set_source_rgba(COL_CREST[0], COL_CREST[1], COL_CREST[2], COL_CREST[3])
        cr.set_line_width(8)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)
        cr.stroke()
        cr.restore()
        
        # Hairline
        cr.save()
        cr.new_path()
        for i, (x, y) in enumerate(points):
            if i == 0:
                cr.move_to(x, y)
            else:
                cr.line_to(x, y)
        
        cr.set_source_rgba(COL_LINE[0], COL_LINE[1], COL_LINE[2], COL_LINE[3])
        cr.set_line_width(1)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)
        cr.stroke()
        cr.restore()


def main():
    # Check for Hyprland
    if not os.getenv('HYPRLAND_INSTANCE_SIGNATURE'):
        import glob
        sockets = glob.glob('/tmp/hypr/*/.socket.sock')
        if not sockets:
            print("Error: Hyprland not detected")
            sys.exit(1)
    
    print("🚀 Starting wave overlay...")
    
    # Check if running under X11
    display = os.getenv('DISPLAY', '')
    if display:
        print(f"📺 Display: {display}")
    
    app = Gtk.Application.new('com.waybar.wave', 0)
    
    def activate(app):
        win = WaveOverlay()
        win.set_application(app)
        win.show_all()
    
    app.connect('activate', activate)
    
    try:
        app.run(None)
    except KeyboardInterrupt:
        print("\n👋 Wave overlay stopped")
        sys.exit(0)


if __name__ == '__main__':
    main()
