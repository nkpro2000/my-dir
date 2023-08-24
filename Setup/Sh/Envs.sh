# Environmental Variables
# Will be run by ~/nk/Setup/Sh/nk-{profile,rcfile}.sh
# like `. ~/nk/Setup/Sh/Envs.sh`

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
export PUB_CACHE="$HOME/.pub-cache"

export ANDROID_HOME=/opt/android-sdk
export CHROME_EXECUTABLE=/opt/google/chrome/google-chrome
#flutter}


echo "pf $0"

## Envs needed to be loaded on non-login shell
### Above Envs always loaded
else

echo "rc $0"


. "${HOME}/nk/.secrets/.53c2375.sh"


fi
