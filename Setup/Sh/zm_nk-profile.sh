# To make /etc/profile to run nk-profile.sh
# Will be copied to /etc/profile.d/ by ~/nk/setup-nk.py and run by /etc/profile 
# like `for profile in /etc/profile.d/*.sh; do test -r "$profile" && . "$profile"; done`.
# /etc/profile is sourced by all SHELLs, after initialized by login (which by init).

# shellcheck shell=sh
if test -f "${HOME}/nk/Setup/Sh/nk-profile.sh" -a -r "${HOME}/nk/Setup/Sh/nk-profile.sh"; then
    # shellcheck disable=SC1091
    . "${HOME}/nk/Setup/Sh/nk-profile.sh" # . is like source command
fi
