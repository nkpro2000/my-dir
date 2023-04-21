# Will be run by SHELL from RCfiles (appended by ~/nk/setup-nk.py)
# like `. ~/nk/Setup/Sh/nk-rcfile.sh`

# shellcheck shell=sh
export NK_RCFILE_RETURN

## Updating PATH using ~/nk/Dev/bin/.path
##########################################
if test ! "$(echo "$NK_RCFILE_RETURN" | jq -r '.[0]')" = '0'; then
# just to avoid repetition

nk_rcfile_profile_path=''
nk_rcfile_rcfiles_path=''
nk_rcfile_read='None'
while IFS= read -r nk_rcfile_path; do
    case "$nk_rcfile_read" in
        'None') # Noting read yet
            nk_rcfile_profile_path="${nk_rcfile_path}"
            nk_rcfile_read='ProfilePath'
            ;;
        'ProfilePath') # Path at profile is read
            nk_rcfile_rcfiles_path="${nk_rcfile_path}"
            nk_rcfile_read='RCfilePath'
            ;;
        'RCfilePath') # Path at rcfile is also read
            break
            ;;
    esac
done < "${HOME}/nk/Dev/bin/.path"
unset nk_rcfile_read nk_rcfile_path

if test -n "$nk_rcfile_profile_path"; then
    case ":${PATH}:" in
        *":${nk_rcfile_profile_path}:"*)
            PATH="$(echo "$PATH" | awk '!x{x=sub("'"${nk_rcfile_profile_path}"'","'"${nk_rcfile_rcfiles_path}"'")}7')"
            # https://stackoverflow.com/q/148451 https://stackoverflow.com/a/18196901
            # OR simply `PATH="${PATH/"${nk_rcfile_profile_path}"/"${nk_rcfile_rcfiles_path}"}"` if in bash/zsh
            export PATH
            ;;
        *)
            echo 'nk-rcfile : Warning : Profile Path present but not set in PATH'
            export PATH="${nk_rcfile_rcfiles_path}${PATH:+:$PATH}"
    esac
else
    export PATH="${nk_rcfile_rcfiles_path}${PATH:+:$PATH}"
fi

unset nk_rcfile_profile_path nk_rcfile_rcfiles_path
# Mentioning first job (updating PATH) is done
fi; NK_RCFILE_RETURN='[0]'
# Unlike nk-profile, Detailed return is not needed. Anyway, Errors will be printed on shell.


## Adding Environmental Variables
##################################

if test ! "$(echo "$NK_RCFILE_RETURN" | jq -r '.[1]')" = '0'; then

# shellcheck disable=SC1091
. "${HOME}/nk/Setup/Sh/Envs.sh"

fi; NK_RCFILE_RETURN='[0,0]'

if test ! "$(echo "$NK_RCFILE_RETURN" | jq -r '.[2]')" = '0'; then

for nk_rcfile_sc in "${HOME}/nk/Setup/Sh/Envs/"*; do
    # shellcheck disable=SC1090
    . "$nk_rcfile_sc"
done; unset nk_rcfile_sc

fi; NK_RCFILE_RETURN='[0,0,0]'


## Adding Dev related envs like functions/aliases
##################################################

if test ! "$(echo "$NK_RCFILE_RETURN" | jq -r '.[3]')" = '0'; then

for nk_rcfile_sc in "${HOME}/nk/Dev/Envs/"*; do
    # shellcheck disable=SC1090
    . "$nk_rcfile_sc"
done; unset nk_rcfile_sc

fi; NK_RCFILE_RETURN='[0,0,0,0]'

