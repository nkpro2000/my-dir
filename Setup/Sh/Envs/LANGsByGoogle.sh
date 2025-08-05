# Environmental Variables just for Google's langs (dart,go,...)
# Will be run by ~/nk/Setup/Sh/nk-{profile,rcfile}.sh
# like `for nk_rcfile_sc in ~/nk/Setup/Sh/Envs/*; do . "$nk_rcfile_sc"; done`

# shellcheck shell=sh
:
# shellcheck disable=SC2154  # Initialized at ~/nk/Setup/Sh/nk-profile.sh
if test -n "${nk_profile}"; then

#dart{

#dart}

#pub{
export PUB_CACHE="$HOME/.pub-cache"
# can be "$HOME/.cache/pub" ## but i doubt google may hardcoded it.
#pub} https://dart.dev/tools/pub/environment-variables

#flutter{
export ANDROID_HOME="$HOME/nk/Dev/google/android/sdk"
export CHROME_EXECUTABLE=/opt/google/chrome/google-chrome
#flutter}

else

:

fi
