# Will be run by /etc/profile.d/zm_nk-profile.sh
# like `. ~/nk/Setup/Sh/nk-profile.sh`

# shellcheck shell=sh
:
# shellcheck disable=SC2034  # To let other scripts know nk-profile is running them
nk_profile="${HOME}/nk/Setup/Sh/nk-profile.sh"

## Adding nk/Dev bin and sub bins to PATH
##########################################
nk_profile_path="${HOME}/nk/Dev/bin"

if test -d "${HOME}/nk/Dev/bin" -a -r "${HOME}/nk/Dev/bin" -a -x "${HOME}/nk/Dev/bin"; then
# write permission is not needed on ~/nk/Dev/bin/, since this script not intended to create a new
#   file or directory in ~/nk/Dev/bin/.

    for nk_profile_fd in "${HOME}/nk/Dev/bin/"*; do # needed read permission on ~/nk/Dev/bin/
        if test -d "$nk_profile_fd" -a -x "$nk_profile_fd"; then # needed executable permission on ~/nk/Dev/bin/
        # write permission is not needed on "$nk_profile_fd", for the same reason as ~/nk/Dev/bin/.
        #TODO read, x - sudo
        #TODO remove x perm test and use cd for test -L file only

            nk_profile_exclude='False'
            if test -f "${HOME}/nk/Dev/bin/.exclude_in_profile" -a -r "${HOME}/nk/Dev/bin/.exclude_in_profile"; then
            #TODO why not include_in_profile, so not required read perm on ~/nk/Dev/bin/, since no gloging just matching
            # write and executable permission are not needed as it is not intended.
                while IFS= read -r nk_profile_ep; do
                    if test "$nk_profile_fd" = "${HOME}/nk/Dev/bin/$nk_profile_ep"; then
                        nk_profile_exclude='True'
                        break
                    fi
                done < "${HOME}/nk/Dev/bin/.exclude_in_profile" # needed read permission on ~/nk/Dev/bin/.exclude_in_profile
            fi
            if test "$nk_profile_exclude" = 'False'; then
                nk_profile_path="${nk_profile_path}:$(cd "$nk_profile_fd" && pwd -P)"; # needed executable permission on "$nk_profile_fd"
            fi

        fi
    done
    unset nk_profile_exclude
    unset nk_profile_ep
    unset nk_profile_fd

    #case "${PATH}" in # just in case
    #    "${nk_profile_path}"*)

    # Present anywhere in PATH is OK
    case ":${PATH}:" in # just in case
        *":${nk_profile_path}:"*)
            ;;
        *)
            PATH="${nk_profile_path}${PATH:+:$PATH}"
    esac
    export PATH

fi

unset nk_profile_path


## Adding nk/.53c2375 Secrets to ENV
#####################################

# Just add it in specific programming language environments
# Eg: adding ~/nk/.53c2375 to PYTHONPATH by adding it in ~/nk/Setup/Sh/Envs/PYTHONPATH.sh


## Adding Environmenal Variables
#################################

if test -f "${HOME}/nk/Setup/Sh/Envs.sh" -a -r "${HOME}/nk/Setup/Sh/Envs.sh"; then
# write permission is not needed, since writing to this file is not required.
# execute permission is not needed, since using . not executing script
## . just Read and execute commands from FILENAME in the current shell.
    # shellcheck disable=SC1091
    . "${HOME}/nk/Setup/Sh/Envs.sh" # needed read permission on ~/nk/Setup/Sh/Envs.sh
fi

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

fi



unset nk_profile
