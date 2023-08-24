# To update shell envs (related to nk) in login SHELL.
# Like Env variables, updating PATH, etc.,
# Will be run by /etc/profile.d/zm_nk-profile.sh
# like `. ~/nk/Setup/Sh/nk-profile.sh`

# shellcheck shell=sh
:
# shellcheck disable=SC2034  # To let other scripts know nk-profile is running them
nk_profile="${HOME}/nk/Setup/Sh/nk-profile.sh"

## Adding nk/Dev bin and sub bins to PATH
##########################################
export NK_PROFILE_RETURN='[1,1,1]'
NK_PROFILE_RETURN_1='0'
if test -f "${HOME}/nk/Dev/bin/.path" -a -r "${HOME}/nk/Dev/bin/.path"; then
# write and execute permission is not needed on ~/nk/Dev/bin/.path,
# since this script not intended to edit or execute it.

    IFS= read -r nk_profile_path < "${HOME}/nk/Dev/bin/.path" # first line is profile path
    #                        needed read permission on ~/nk/Dev/bin/.path

    NK_PROFILE_RETURN_1='[1]'
    NK_PROFILE_RETURN_1_1='0'
    if test -n "${nk_profile_path}"; then

        NK_PROFILE_RETURN_1_1='[1]'
        NK_PROFILE_RETURN_1_1_1='0'
        #case "${PATH}" in # just in case
        #    "${nk_profile_path}"*)

        # Present anywhere in PATH is OK
        case ":${PATH}:" in # just in case
            *":${nk_profile_path}:"*)
                NK_PROFILE_RETURN_1_1_1='1'
                ;;
            *)
                export PATH="${nk_profile_path}${PATH:+:$PATH}"
        esac; NK_PROFILE_RETURN_1_1="[${NK_PROFILE_RETURN_1_1_1}]"; unset NK_PROFILE_RETURN_1_1_1

    else NK_PROFILE_RETURN_1_1='1'
    fi; NK_PROFILE_RETURN_1="[${NK_PROFILE_RETURN_1_1}]"; unset NK_PROFILE_RETURN_1_1

    unset nk_profile_path

else NK_PROFILE_RETURN_1='1'
fi; NK_PROFILE_RETURN="[${NK_PROFILE_RETURN_1},1,1]"


## Adding Environmental Variables
##################################

NK_PROFILE_RETURN_2='0'
if test -f "${HOME}/nk/Setup/Sh/Envs.sh" -a -r "${HOME}/nk/Setup/Sh/Envs.sh"; then
# write permission is not needed, since writing to this file is not required.
# execute permission is not needed, since using . not executing script
## . just Read and execute commands from FILENAME in the current shell.
    # shellcheck disable=SC1091
    . "${HOME}/nk/Setup/Sh/Envs.sh" # needed read permission on ~/nk/Setup/Sh/Envs.sh
else NK_PROFILE_RETURN_2='1'
fi; NK_PROFILE_RETURN="[${NK_PROFILE_RETURN_1},${NK_PROFILE_RETURN_2},1]"

NK_PROFILE_RETURN_3='0'
if test -d "${HOME}/nk/Setup/Sh/Envs" -a -r "${HOME}/nk/Setup/Sh/Envs" -a -x "${HOME}/nk/Setup/Sh/Envs"; then
# write permission is not needed on ~/nk/Setup/Sh/Envs/, since this script not intended to create a new
#   file or directory in ~/nk/Setup/Sh/Envs/.

    for nk_profile_sc in "${HOME}/nk/Setup/Sh/Envs/"*; do # needed read permission on ~/nk/Setup/Sh/Envs/
        if test -f "$nk_profile_sc" -a -r "$nk_profile_sc"; then # needed executable permission on ~/nk/Setup/Sh/Envs/
        # write and execute permission is not needed, for the same reason as ~/nk/Setup/Sh/Envs.sh
            # shellcheck disable=SC1090
            . "$nk_profile_sc" # needed read permission on "$nk_profile_sc"
        fi
    done
    unset nk_profile_sc

else NK_PROFILE_RETURN_3='1'
fi; NK_PROFILE_RETURN="[${NK_PROFILE_RETURN_1},${NK_PROFILE_RETURN_2},${NK_PROFILE_RETURN_3}]"



unset nk_profile NK_PROFILE_RETURN_1 NK_PROFILE_RETURN_2 NK_PROFILE_RETURN_3
