# Will be run by shell rc files
# like `. ~/nk/Dev/Envs/Shell.sh`

# shellcheck shell=sh


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