# Environmental Variables

# shellcheck shell=sh
:
## Envs needed to be loaded by login shell
# shellcheck disable=SC2154  # Initialized at ~/nk/Setup/Sh/nk-profile.sh
if test -n "${nk_profile}"; then

#jupyterDir{
export JUPYTER_CONFIG_DIR="$HOME/nk/Dev/jupyter/config"
export JUPYTER_DATA_DIR="$HOME/nk/Dev/jupyter/data"
#jupyterDir}

#flutter{
export ANDROID_HOME=/opt/android-sdk
export CHROME_EXECUTABLE=/opt/google/chrome/google-chrome
#flutter}

#darling{
#export DPREFIX=/run/media/nkpro/Extended/darling/nkpro/.darling
#darling}


## Envs needed to be loaded on non-login shell
### Above Envs always loaded
else

#darling{
export DPREFIX=/run/media/nkpro/Extended/darling/nkpro/.darling
#darling}


fi
