# To add functions/aliases/envs related to Python.
# Will be run by ~/nk/Setup/Sh/nk-rcfile.sh (by shell rc files)
# like `for nk_rcfile_sc in ~/nk/Dev/Envs/*; do . "$nk_rcfile_sc"; done` .

# shellcheck shell=sh

#TODO these functions are not specific to linux, better move to cross-platform scripts

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
