local c = {
    bg = "#1f222d",
    bg_alt = "#17191f",
    cursorline = "#252936",
    fg = "#fff1c4",
    muted = "#7C8A93",
    red = "#e0283b",
    red_bright = "#fc161a",
    sage = "#9cbd82",
    blue = "#556fe6",
}

vim.cmd("highlight clear")
vim.o.background = "dark"
vim.o.termguicolors = true

local hi = vim.api.nvim_set_hl

hi(0, "Normal", { fg = c.fg, bg = c.bg })
hi(0, "NormalFloat", { fg = c.fg, bg = c.bg_alt })
hi(0, "FloatBorder", { fg = c.muted, bg = c.bg_alt })
hi(0, "CursorLine", { bg = c.cursorline })
hi(0, "Cursor", { fg = c.bg, bg = c.red_bright })
hi(0, "Visual", { fg = c.bg, bg = c.sage })

hi(0, "LineNr", { fg = c.muted, bg = c.bg })
hi(0, "CursorLineNr", { fg = c.red_bright, bg = c.bg, bold = true })
hi(0, "SignColumn", { fg = c.muted, bg = c.bg })
hi(0, "ColorColumn", { bg = c.cursorline })
hi(0, "VertSplit", { fg = c.muted, bg = c.bg })
hi(0, "WinSeparator", { fg = c.muted, bg = c.bg })

hi(0, "StatusLine", { fg = c.fg, bg = c.bg_alt })
hi(0, "StatusLineNC", { fg = c.muted, bg = c.bg_alt })
hi(0, "TabLine", { fg = c.muted, bg = c.bg_alt })
hi(0, "TabLineSel", { fg = c.bg, bg = c.red_bright, bold = true })
hi(0, "TabLineFill", { bg = c.bg_alt })

hi(0, "Search", { fg = c.bg, bg = c.sage })
hi(0, "IncSearch", { fg = c.bg, bg = c.red_bright })
hi(0, "CurSearch", { fg = c.bg, bg = c.red_bright, bold = true })
hi(0, "MatchParen", { fg = c.red_bright, bold = true, underline = true })

hi(0, "Comment", { fg = c.muted, italic = true })
hi(0, "String", { fg = c.sage })
hi(0, "Character", { fg = c.sage })
hi(0, "Function", { fg = c.blue })
hi(0, "Keyword", { fg = c.red_bright })
hi(0, "Statement", { fg = c.red })
hi(0, "Type", { fg = c.sage })
hi(0, "Constant", { fg = c.red })
hi(0, "Identifier", { fg = c.fg })
hi(0, "Special", { fg = c.blue })

hi(0, "ErrorMsg", { fg = c.red_bright, bold = true })
hi(0, "WarningMsg", { fg = c.red, bold = true })
hi(0, "DiagnosticError", { fg = c.red_bright })
hi(0, "DiagnosticWarn", { fg = c.red })
hi(0, "DiagnosticInfo", { fg = c.blue })
hi(0, "DiagnosticHint", { fg = c.sage })

hi(0, "@comment", { link = "Comment" })
hi(0, "@string", { link = "String" })
hi(0, "@function", { link = "Function" })
hi(0, "@keyword", { link = "Keyword" })
hi(0, "@type", { link = "Type" })
hi(0, "@constant", { link = "Constant" })
