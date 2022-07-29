# shellcheck shell=sh
if test -f "${HOME}/nk/Setup/Sh/nk-profile.sh" -a -r "${HOME}/nk/Setup/Sh/nk-profile.sh"; then
    . "${HOME}/nk/Setup/Sh/nk-profile.sh" # . is like source command
fi
