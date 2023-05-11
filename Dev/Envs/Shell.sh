# To add functions/aliases/envs related to SHELLs or for adjacent scripts.
# Will be run by ~/nk/Setup/Sh/nk-rcfile.sh (by shell rc files)
# like `for nk_rcfile_sc in ~/nk/Dev/Envs/*; do . "$nk_rcfile_sc"; done` .

# shellcheck shell=sh

# May use this method to retain env variables unchanged,
## a='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'"'"'()*+,-./:;<=>?@[\]^_`{|}~ '$'\t\n\r\x0b\x0c'
## eval "fn_can_edit_a; a='$(/bin/echo "$a"|sed "s/'/'"'"'"'"'"'"'/")'"
##                                                   (s/'/')(")(')(")('/)
##                                ^-- https://stackoverflow.com/questions/36277870/zsh-why-is-n-interpreted-within-single-quotes
# Like:
## fn1_() { definition }
## fn() { eval "fn1_ $@; fn1_v1='$(above method)'; fn1_v2='$(above method)'"}
## # fn1_v* are all variables used inside fn1_ function.
#
# But this method is not suitable for other type of variables.

read_secret () { # Read secret string
    # The `read -s` will turn off echo for getting secrets.
    # The -s option of read is not defined in the POSIX standard.
    
    tty_settings=$(stty -g) || exit # save current tty settings
    save_traps=$(trap) # save current traps

    # schedule restore of the settings on exit or on receiving SIGINT or SIGTERM:
    trap 'stty "$tty_settings"; trap - EXIT INT TERM; eval "$save_traps"; unset tty_settings save_traps; return 0' EXIT
    trap 'stty "$tty_settings"; trap - EXIT INT TERM; eval "$save_traps"; unset tty_settings save_traps; return 130' INT
    trap 'stty "$tty_settings"; trap - EXIT INT TERM; eval "$save_traps"; unset tty_settings save_traps; return 143' TERM

    # disable terminal local echo
    stty -echo || exit

    # read command with arguments from read_secret & record exit status
    # shellcheck disable=SC2162 # -r can be passed from read_secret
    read "$@"; ret=$?

    # Restoring settings:
    stty "$tty_settings" # Enable echo by setting saved settings
    trap - EXIT INT TERM # Reset scheduled traps
    eval "$save_traps"   # Enable previous traps, if had
    unset tty_settings save_traps # Not needed anymore and to Avoid Polluting the Namespace.

    # Print a newline because the newline entered by the user after
    # entering the passcode is not echoed. This ensures that the
    # next line of output begins at a new line.
    #echo # not required since read command don't do

    # return what read command returned
    eval "unset ret; return $ret" # https://unix.stackexchange.com/a/456454

}
# https://stackoverflow.com/a/28393320
# https://unix.stackexchange.com/a/223000

## For linting and formatting shell scripts.
# find . -path './.git' -prune -o -type f -exec bash -c '
#  if [[ "{}" =~ \.sh$ ]]; then  clear;echo sc "{}";shellcheck {};echo cs;read;  clear;echo sf {};shfmt -i 4 -ci -p -d {};echo fs;read;
#  elif test "$(head -n1 '"'"'{}'"'"' | grep -E '"'"'^#! ?/bin/(da|ba|z|fi)?sh'"'"')"
#   then clear;echo sc {};shellcheck {};echo cs;read; clear;echo sf {};shfmt -i 4 -ci -d {};echo fs;read;
#  fi' \;
