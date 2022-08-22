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


## Envs needed to be loaded on non-login shell
### Above Envs always loaded
else

#$ sudo tree /mnt/Extended/LinuxExtRoot -pug --metafirst
# [drwxr-xr-x root  root ]  /mnt/Extended/LinuxExtRoot
# [drwxr-xr-x root  root ]  ├── home
# [drwx------ nkpro nkpro]  │   └── nkpro
# [drwxrwxrwt root  root ]  └── thome
# [drwx------ nkpro nkpro]      ├── nkpro_darling
# [drwx------ nkpro nkpro]      ├── nkpro_droid
# [drwx------ nkpro nkpro]      └── nkpro_wine

#darling{
export DPREFIX="/mnt/Extended/LinuxExtRoot/thome/${USER}_darling/.darling"
#darling}


fi
