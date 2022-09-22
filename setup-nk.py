""" $ tree -aF ~/nk
~/nk/
:
├── .53c2375/
│   ├── secret5.sh
│   ├── secret5.py
│   :
├── .assets/
│   ├── nk.ico
│   ├── NK.ico
│   ├── nk.png
│   ├── NK.png
│   :
├── Dev/
│   ├── bin/
│   │   ├── .path
│   │   ├── .generate_path
│   │   ├── code -> ../code/bin/
│   │   :
│   ├── code -> <any_code_editor>/
│   │   :
│   ├── code-data/
│   │   :
│   ├── <any_code_editor>/ (eg: VScodium)
│   │   ├── bin/
│   │   │   :
│   │   ├── data -> ../code-data/ (for Portable Mode)
│   │   :
│   ├── Envs/
│   │   ├── Github.sh
│   │   ├── Python.sh
│   │   :
│   ├── jupyter/
│   │   ├── config/
│   │   │   :
│   │   ├── data/
│   │   │   :
│   │   :
│   ├── lobby/
│   │   :
│   :
├── nk.py
├── Setup/
│   ├── Panel/ #TODO rename Pannel to Panel in both repo and local dir
│   │   ├── Scripts/
│   │   │   :
│   │   :
│   ├── Sh
│   │   ├── zm_nk-profile.sh
│   │   ├── nk-profile.sh
│   │   ├── nk-profile.sh_notes
│   │   ├── nk-profile.sh_notes2
│   │   ├── nk-rcfile.sh
│   │   ├── Envs.sh
│   │   ├── Envs/
│   │   │   ├── PYTHONPATH.sh
│   │   │   :
│   │   :
│   :
├── setup-nk.py
:
""" #TODO https://stackoverflow.com/questions/3207728/retaining-file-permissions-with-git

import re
import os

# Adding nk to user-places
###########################

HOME_DIR = os.environ['HOME'] + '/'
USER_PLACES = HOME_DIR + '.local/share/user-places.xbel'
NK_DIR = HOME_DIR + 'nk/'

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
nk_place = TITLE_PATTERN.sub('<title>NewK</', nk_place)
nk_place = ICON_PATTERN.sub('icon name="{}"/>'.format(NK_DIR + '.assets/NewK.ico'), nk_place)
home_id = ID_PATTERN.findall(home_place[0])[0]
nk_place = ID_PATTERN.sub('<ID>{}</'.format(home_id+'0'), nk_place)
nk_place = SYSTEM_PATTERN.sub('<isSystemItem>false</', nk_place)
nk_place = HIDDEN_PATTERN.sub('<IsHidden>false</', nk_place)

if nk_place in places:
    print('I> Already Added NK to user-places')
else:
    new_places = places[:home_place.end()]+nk_place+places[home_place.end():]
    # make a backup
    os.replace(USER_PLACES, USER_PLACES+'.bak')
    # updating places
    with open(USER_PLACES, 'w') as user_places:
        user_places.write(new_places)

# Setting folder icon for ~/nk/Dev
###################################

DEV_DIR_ICON = NK_DIR + 'Dev/.directory'

DE_ICON_PATTERN = re.compile('([\s\S]*?)\[Desktop Entry\]([\s\S]*?)Icon=(.*?)\n([\s\S]*)')
DE_ALSO_PATTERN = re.compile('([\s\S]*?)\[Desktop Entry\]([\s\S]*?)(\[.+?\][\s\S]*)')
DE_ONLY_PATTERN = re.compile('([\s\S]*?)\[Desktop Entry\]([\s\S]*)')

if os.path.isfile(DEV_DIR_ICON):
    with open(DEV_DIR_ICON) as dev_dir_icon:
        dev_dir_icon_ = dev_dir_icon.read()

    if m:=DE_ICON_PATTERN.match(dev_dir_icon_):
        groups = m.groups()
        if re.match('[\s\S]*?\[.+?\][\s\S]*',groups[1]):
            groups = DE_ALSO_PATTERN.match(dev_dir_icon_).groups()
            with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
                dev_dir_icon.write(
                    groups[0] + '[Desktop Entry]' + groups[1].rstrip('\n') +\
                        '\nIcon='+NK_DIR+'.assets/NK.ico\n\n' + groups[2]
                )
        else:
            with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
                dev_dir_icon.write(
                    groups[0] + '[Desktop Entry]' + groups[1] +\
                        'Icon='+NK_DIR+'.assets/NK.ico\n' + groups[3]
                )
    elif m:=DE_ALSO_PATTERN.match(dev_dir_icon_):
        groups = m.groups()
        with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
            dev_dir_icon.write(
                groups[0] + '[Desktop Entry]' + groups[1].rstrip('\n') +\
                    '\nIcon='+NK_DIR+'.assets/NK.ico\n\n' + groups[2]
            )
    elif m:=DE_ONLY_PATTERN.match(dev_dir_icon_):
        groups = m.groups()
        with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
            dev_dir_icon.write(
                groups[0] + '[Desktop Entry]' + groups[1].rstrip('\n') +\
                    '\nIcon='+NK_DIR+'.assets/NK.ico\n'
            )
    else:
        with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
            dev_dir_icon.write('[Desktop Entry]\nIcon={}\n\n'.format(NK_DIR + '.assets/NK.ico'))
            dev_dir_icon.write(dev_dir_icon_)

else:
    with open(DEV_DIR_ICON, 'w') as dev_dir_icon:
        dev_dir_icon.write('[Desktop Entry]\nIcon={}\n'.format(NK_DIR + '.assets/NK.ico'))

# Adding nk-profile
####################

SETUP_DIR = NK_DIR + 'Setup/'
SHELL_SETUP_DIR = SETUP_DIR + 'Sh/'

NK_PROFILE_FILE = SHELL_SETUP_DIR + 'zm_nk-profile.sh'
PROFILE_D = '/etc/profile.d/'
NK_PROFILE_PATH = PROFILE_D + 'zm_nk-profile.sh'

if os.path.isfile(NK_PROFILE_PATH):
    if os.system(f'diff {NK_PROFILE_PATH} {NK_PROFILE_FILE}') == 0:
        print('I> Already Added nk-profile to /etc/profile.d')
    else:
        os.system(f'sudo cp {NK_PROFILE_FILE} {NK_PROFILE_PATH}')
else:
    os.system(f'sudo cp {NK_PROFILE_FILE} {NK_PROFILE_PATH}')

# Adding nk-rcfile
###################
## https://unix.stackexchange.com/a/44619

SHELLRC_NKRCFILE_DIV_PATTERN = re.compile('''
#nk-rcfile\{
[\s\S]*?
#nk-rcfile}
''')

# bash
BASHRC = HOME_DIR + '.bashrc'
BASHRC_NKRCFILE_DIV = '''
#nk-rcfile{
. "$HOME"/nk/Setup/Sh/nk-rcfile.sh
#nk-rcfile}
'''
if os.path.isfile(BASHRC):
    with open(BASHRC, 'r') as file:
        bashrc = file.read()

    if m:=SHELLRC_NKRCFILE_DIV_PATTERN.search(bashrc):
        if m.group(0) == BASHRC_NKRCFILE_DIV:
            print('I> Already Added nk-rcfile to ~/.bashrc')
        else:
            with open(BASHRC, 'w') as file:
                file.write(
                    SHELLRC_NKRCFILE_DIV_PATTERN.sub(
                        BASHRC_NKRCFILE_DIV, bashrc
                    )
                )
    else:
        with open(BASHRC, 'w') as file:
            file.write(bashrc)
            file.write(BASHRC_NKRCFILE_DIV)

# zsh
ZSHRC = HOME_DIR + '.zshrc'
ZSHRC_NKRCFILE_DIV = '''
#nk-rcfile{
emulate sh -c 'source '"$HOME"'/nk/Setup/Sh/nk-rcfile.sh'
#nk-rcfile}
'''
if os.path.isfile(ZSHRC):
    with open(ZSHRC, 'r') as file:
        zshrc = file.read()

    if m:=SHELLRC_NKRCFILE_DIV_PATTERN.search(zshrc):
        if m.group(0) == ZSHRC_NKRCFILE_DIV:
            print('I> Already Added nk-rcfile to ~/.zshrc')
        else:
            with open(ZSHRC, 'w') as file:
                file.write(
                    SHELLRC_NKRCFILE_DIV_PATTERN.sub(
                        ZSHRC_NKRCFILE_DIV, zshrc
                    )
                )
    else:
        with open(ZSHRC, 'w') as file:
            file.write(zshrc)
            file.write(ZSHRC_NKRCFILE_DIV)

# fish
## Skip. fish is intentionally not fully POSIX compliant

# dash
## No rc file. https://unix.stackexchange.com/a/565908 https://askubuntu.com/a/86143

# Others
## Yet to learn

# Setting CONFIG & DATA dir for Jupyter
########################################

os.makedirs(os.path.join(NK_DIR, "Dev/jupyter/config"), exist_ok=True)
os.makedirs(os.path.join(NK_DIR, "Dev/jupyter/data"), exist_ok=True)

# Installing Jupyter and SageMath
##################################

os.system('sudo pacman -S jupyter{,lab,-notebook} python-ipykernel')
os.system('sudo pacman -S sagemath{,-doc,-jupyter} cantor')
