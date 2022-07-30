# Will be run by shell rc files
# like `. ~/nk/Dev/Envs/Python.sh`

# shellcheck shell=sh

pyvenv () {
    if test "$1" = '-t'; then
        python -m venv --copies --clear --upgrade-deps --prompt PYtenv /tmp/.pyvenv
    elif test "$1" = '-d'; then
        rm -rf ./.pyvenv
    else
        python -m venv --copies --clear --upgrade-deps --prompt PYvenv ./.pyvenv
    fi
}
pyvea () {
    if test "$1" = '-t'; then
        if [ ! -d "/tmp/.pyvenv" ]; then pyvenv -t; fi
        . /tmp/.pyvenv/bin/activate
    else
        if [ ! -d "/tmp/.pyvenv" ]; then pyvenv; fi
        . ./.pyvenv/bin/activate
    fi
}
