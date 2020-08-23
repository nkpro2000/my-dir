""" $ tree -aF ~/nk
~/nk/
:
├── assets/
│   ├── nk.ico
│   ├── NK.ico
│   ├── nk.png
│   ├── NK.png
│   :
├── Dev/
│   ├── bin/
│   |   ├── code -> ../code/bin/
│   │   :
│   ├── code -> <any_code_editor>/
│   ├── <any_code_editor>/ (eg: VScodium)
│   │   :
│   ├── lobby/
│   :
├── nk.py
├── setup-nk.py
:
"""

import re
import os

# Adding nk to user-places
###########################

HOME_DIR = os.environ['HOME']
USER_PLACES = os.path.join(HOME_DIR, '.local/share/user-places.xbel')
NK_DIR = os.path.join(HOME_DIR, 'nk')

PLACE_PATTERN = re.compile(r' <bookmark [\s\S]*? <\/bookmark>\n')
FILE_PATTERN = re.compile(r'href="(\S*?)">')
TITLE_PATTERN = re.compile(r'<title>(\S*?)<\/')
ICON_PATTERN = re.compile(r'icon name="(\S*?)"\/>')
ID_PATTERN = re.compile(r'<ID>(\S*?)<\/')
SYSTEM_PATTERN = re.compile(r'<isSystemItem>(\S*?)<\/')
HIDDEN_PATTERN = re.compile(r'<IsHidden>(\S*?)<\/')

with open(USER_PLACES, 'r') as user_places:
    places = user_places.read()

home_place = PLACE_PATTERN.search(places)
nk_place = FILE_PATTERN.sub('href="file://{}">'.format(NK_DIR), home_place[0])
nk_place = TITLE_PATTERN.sub('<title>NK</', nk_place)
nk_place = ICON_PATTERN.sub('icon name="{}"/>'.format(os.path.join(NK_DIR, 'assets/nk.ico')), nk_place)
home_id = ID_PATTERN.findall(home_place[0])[0]
nk_place = ID_PATTERN.sub('<ID>{}</'.format(home_id+'0'), nk_place)
nk_place = SYSTEM_PATTERN.sub('<isSystemItem>false</', nk_place)
nk_place = HIDDEN_PATTERN.sub('<IsHidden>false</', nk_place)

if nk_place in places:
    print('Already Added NK to user-palces')
else:
    new_places = places[:home_place.end()]+nk_place+places[home_place.end():]
    # make a backup
    os.replace(USER_PLACES, USER_PLACES+'.bak')
    # updating places
    with open(USER_PLACES, 'w') as user_places:
        user_places.write(new_places)

# Setting folder icon for ~/nk/Dev
###################################

DEV_DIR_ICON = os.path.join(NK_DIR, 'Dev/.directory')

with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
    dev_dir_icon.write('[Desktop Entry]\nIcon={}\n'.format(os.path.join(NK_DIR, 'assets/NK.ico')))

# Adding nkDev to ~/.bashrc
############################

BASHRC = os.path.join(HOME_DIR, '.bashrc')

nkDev = r'''
#nkDev{
path="$HOME/nk/Dev/bin"
for fd in $HOME/nk/Dev/bin/*; do
    if [ -d "$fd" ]; then 
        path+=":$(realpath "$fd")";
    fi
done
export PATH="$path:$PATH"
#nkDev}
'''

with open(BASHRC) as bashrc:
    bashrc_ = bashrc.read()

if nkDev in bashrc_:
    print('Already Added nkDev to ~/.bashrc')
else:
    with open(BASHRC, 'a') as bashrc:
        bashrc.write(nkDev)
