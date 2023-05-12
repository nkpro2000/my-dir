#SKIPLINES:15 Comments in these lines won't be copied to map files.
#
# Include this file in map files like below :
#  #nk-kbdmap-include{ # copies all text in given files and pastes here
#  #./nk_kbd-header.inc
#  #nk-kbdmap-include}
#
# nk-kbdmap-include-0- : copy contents in files, but remove `include` statements.
# nk-kbdmap-include-0  : copy contents in files, no parsing/removing `include` statements. (default:nk-kbdmap-include)
# nk-kbdmap-include-   : copy contents in files and also in files parsed from `include` statements, recursively.
# nk-kbdmap-include-n  : " , but recursive up to n depth (below that `include`s will not be parsed/removed).
# nk-kbdmap-include-n- : same as 'nk-kbdmap-include-n', but below n depth `include` will be removed.
#
# nk-kbdmap-exclude-PATTERNS : while parsing `include`s, file names matching PATTERNS will be skipped.
#   This should be used with nk-kbdmap-include* tags. PATTERN s are parsed like shlex.split(PATTERNS);
#   then all are passed to `grep -E` with `-e` options (like `grep -E -e P1 -e P2 -e P3`).

# Recognized modifier names and their column numbers:
#  shift      1   # 2nd SubLayer
#  altgr      2   # 3rd SubLayer
#  control    4   
#  alt        8   
#  shiftl     16  # 2nd Layer
#  shiftr     32  # 4th Layer
#  ctrll      64  # 3rd Layer
#  ctrlr      128 # 5th Layer
#  capsshift  256 

#keymaps 0-15 better loadkeys handle this. py script will make full table using `#KEYMAPS:`.
#KEYMAPS: 0,1,4,8,2,12,5,9,13,6,3,7
#\\         `single/`ShCoAl C/`ShCoAg C| Default: 0-2,4-6,8-9,12
# 0-15 columns (Shift, AltGr, Control, Alt, and all of their Combinations) is used for this layout.
# Others (>15) can be used for extended layouts, Eg: shiftl + 0-15 gives 16-31 columns.
#
#  N Sh Ag Co Al  Combination
# --  -  -  -  -  ---------------------------
#  0  0  0  0  0  Plain
#  1  1  0  0  0  Shift
#  4  0  0  1  0  Ctrl
#  8  0  0  0  1  Alt
#  2  0  1  0  0  AltGr
# 12  0  0  1  1  Ctrl + Alt
#  5  1  0  1  0  Shift + Ctrl
#  9  1  0  0  1  Shift + Alt
# 13  1  0  1  1  Shift + Ctrl + Alt
#  6  0  1  1  0  Ctrl + AltGr
#  3  1  1  0  0  Shift + AltGr
#  7  1  1  1  0  Shift + Ctrl + AltGr
# 10  0  1  0  1  Alt + AltGr
# 11  1  1  0  1  Shift + Alt + AltGr
# 14  0  1  1  1  Ctrl + Alt + AltGr
# 15  1  1  1  1  Shift + Ctrl + Alt + AltGr
#
# Actually `keymaps` is for mentioning modifier weights used in the keymap file. So
# `#KEYMAPS:` will be used for custom column order (which is incorrect format) and then
# converted to right format using python scripts. Right format keymaps will to exported to
# locations mentioned in each files (in `#PATH:`).
#
#SKIPLINES:-28 Refer above table for column order of keymap files in ~/nk/Setup/Tty/ .
# 0  1  2  3   | 4 5 6 7 | 8 9 10 11 | 12 13 14 15 | Just for
# Pl Sh Ag SAg | Co +    | Al + 4sub | Co + Al +   |  remembering
# 4 SubLayers  |   4subL |    Layers |  4subLayers |   columns order.
# No {Co,Al,Co+Al} + sub-layer symbols. Eg: Sh+Co+a is not Co+A .

alt_is_meta
#\
# The Alt key typically prefixes the sent symbol with the Esc character,
# e.g. pressing Alt+x generates the Esc (0x1B) byte followed by x.
# As far as I know, traditionally the Meta key used to set the high bit,
# e.g. Meta+x used to generate the byte 0xF8 (x = 0x78; 0x78 + the 8th bit is 0xF8).
# Or maybe there used to be two different popular configurations for the Meta key:
# setting the 8th bit, as well emitting an Esc prefix.
#
# Then two things happened.
# - One is that today's computers no longer have a physical Meta key,
#   so in terminal emulators running on PCs the Alt key took its role.
# - The other is that with the widespread adoption of Unicode (UTF-8),
#   setting the high bit no longer makes any sense;
#   in fact, conflicts with the encoding of pretty much any non-English letter.
#   Applications expect the terminal to send valid UTF-8, and flipping the 8th bit would break this.
#
# That's how terminals ended up with the current situation of **Alt (or possibly Option on Mac)
# replaces Meta key and emitting an Esc prefix**.
#
# https://superuser.com/a/1555005
# joplin://x-callback-url/openNote?id=5042e4e078114c21a0872ae2ca08b512
#
#SKIPLINES:-22 to avoid lot of comments in exported map files.

## replaces first with second. this will be after `#nk-kbdmap-include*`.
#DEFINE:VS VoidSymbol 
#DEFINE:\0 nul        # ^@
#DEFINE:\a Control_g  # ^G
#DEFINE:\b BackSpace  # ^H
#DEFINE:\t Tab        # ^I
#DEFINE:\n Linefeed   # ^J
#DEFINE:\v Control_k  # ^K
#DEFINE:\f Control_l  # ^L
#DEFINE:\r Control_m  # ^M
#DEFINE:\e Escape     # ^[
