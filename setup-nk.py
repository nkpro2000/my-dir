#TODO add shebang with proper python env. First think method for python version management for nkDev
# This is the first file to run after cloning so that all are configured as intended.
# See comments ######### for steps involved in this process done by this script.
# Will be run user like `python setup-nk.py` after cloning this repo in ~/nk .
""" $ tree -aF ~/nk
~/nk/
:
├── .assets/
│   ├── NewK.ico
│   ├── Dev.ico
│   ├── Dev.png
│   ├── Notes.ico
│   ├── Notes.png
│   ├── nk_.ico
│   ├── nk_.png
│   ├── .others/
│   :
├── .logs/
│   :
├── .secrets/       #TODO Think about better method to store secrets
│   ├── .gen
│   ├── secret5.sh
│   ├── secret5.py
│   :
├── Dev/
│   ├── .ssh/
│   │   :
│   ├── bin/
│   │   ├── .path
│   │   ├── .generate_path
│   │   ├── code -> <any_code_editor>
│   │   ├── <any_code_editor>/ (eg: VScodium)
│   │   │   ├── bin/
│   │   │   │   :
│   │   │   ├── data -> ../../code/data (for Portability)
│   │   │   :
│   │   ├── flutter/
│   │   │   ├── bin/
│   │   │   │   ├── cache/
│   │   :   :   :   :
│   ├── code/
│   │   ├── data/
│   │   │   ├── data -> ../../code/data
│   │   │   :           (to copy back to ../../bin/code/)
│   │   :
│   ├── Envs/
│   │   ├── Github.sh
│   │   ├── Net.sh
│   │   ├── Python.sh
│   │   ├── Shell.sh
│   │   :
│   ├── jupyter/
│   │   ├── .pyvenv/ ...
│   │   ├── bin/
│   │   │   ├── jupy
│   │   │   :
│   │   ├── config/ ...
│   │   ├── data/ ...
│   │   ├── py/ ...
│   │   ├── ipy/ ...
│   │   ├── mpl/ ...
│   │   ├── sage/ ...
│   │   :
│   ├── tex/
│   │   ├── .install-tl/
│   │   │   ├── install.sh
│   │   │   └── install-tl-20230831/ ...
│   │   ├── bin/
│   │   │   ├── teks
│   │   │   :
│   │   ├── live/
│   │   │   ├── 2023/
│   │   │   │   ├── bin/ ...
│   │   │   │   ├── texmf-config/ ...
│   │   │   │   ├── texmf-dist/ ...
│   │   │   │   └── texmf-var/ ...
│   │   │   ├── texmf-local/ ...
│   │   │   ├── curr -> 2023
│   │   │   ├── home2023/
│   │   │   │   ├── texmf-config/ ...
│   │   │   │   └── texmf-var/ ...
│   │   │   ├── homecurr -> home2023
│   │   │   └── texmf/ ...
│   │   :
│   ├── google/
│   │   ├── dart/
│   │   │   ├── flutter/
│   │   │   :   :
│   │   ├── go/
│   │   :   :
│   ├── lobby/
│   │   :
│   ├── .directory
│   :
├── Notes/
│   ├── .directory
│   :
├── Setup/
│   ├── Dolphin/
│   │   ├── dirs-info.toml
│   │   ├── dirs-info_.toml
│   │   :
│   ├── Panel/
│   │   ├── Scripts/
│   │   │   :
│   │   :
│   ├── Sh/
│   │   ├── zm_nk-profile.sh
│   │   ├── nk-profile.sh
│   │   ├── nk-profile.sh_notes
│   │   ├── nk-profile.sh_notes2
│   │   ├── nk-rcfile.sh
│   │   ├── Envs.sh
│   │   ├── Envs/
│   │   │   ├── PYTHON.sh
│   │   │   ├── LANGsByGoogle.sh
│   │   │   :
│   │   :
│   ├── Tty/  #Yet2Do so much
│   │   :
│   ├── Others/
│   │   :
│   ├── .directory
│   :
├── nk.py
├── setup-nk.py
├── .directory
:
""" #TODO https://stackoverflow.com/questions/3207728/retaining-file-permissions-with-git

import re
import os
import toml
from glob import glob

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

# Setting folder icon for dirs
###############################

NK_DIR_FILE = NK_DIR + '.directory'
DEV_DIR_FILE = NK_DIR + 'Dev/.directory'
NOTES_DIR_FILE = NK_DIR + 'Notes/.directory'
SETUP_DIR_FILE = NK_DIR + 'Setup/.directory'

def set_folder_icon (dir_file_path, icon_path):

    DE_ICON_PATTERN = re.compile('([\s\S]*?)\[Desktop Entry\]([\s\S]*?)Icon=(.*?)\n([\s\S]*)')
    DE_ALSO_PATTERN = re.compile('([\s\S]*?)\[Desktop Entry\]([\s\S]*?)(\[.+?\][\s\S]*)')
    DE_ONLY_PATTERN = re.compile('([\s\S]*?)\[Desktop Entry\]([\s\S]*)')

    if os.path.isfile(dir_file_path):
        with open(dir_file_path) as dir_file:
            dir_file_ = dir_file.read()

        if m:=DE_ICON_PATTERN.match(dir_file_):
            groups = m.groups()
            if re.match('[\s\S]*?\[.+?\][\s\S]*',groups[1]):
                groups = DE_ALSO_PATTERN.match(dir_file_).groups()
                with open(dir_file_path, 'w') as dir_file:
                    dir_file.write(
                        groups[0] + '[Desktop Entry]' + groups[1].rstrip('\n') +\
                            '\nIcon='+NK_DIR+'.assets/'+icon_path+'\n\n' + groups[2]
                    )
            else:
                with open(dir_file_path, 'w') as dir_file:
                    dir_file.write(
                        groups[0] + '[Desktop Entry]' + groups[1] +\
                            'Icon='+NK_DIR+'.assets/'+icon_path+'\n' + groups[3]
                    )
        elif m:=DE_ALSO_PATTERN.match(dir_file_):
            groups = m.groups()
            with open(dir_file_path, 'w') as dir_file:
                dir_file.write(
                    groups[0] + '[Desktop Entry]' + groups[1].rstrip('\n') +\
                        '\nIcon='+NK_DIR+'.assets/'+icon_path+'\n\n' + groups[2]
                )
        elif m:=DE_ONLY_PATTERN.match(dir_file_):
            groups = m.groups()
            with open(dir_file_path, 'w') as dir_file:
                dir_file.write(
                    groups[0] + '[Desktop Entry]' + groups[1].rstrip('\n') +\
                        '\nIcon='+NK_DIR+'.assets/'+icon_path+'\n'
                )
        else:
            with open(dir_file_path, 'w') as dir_file:
                dir_file.write('[Desktop Entry]\nIcon={}\n\n'.format(NK_DIR + '.assets/'+icon_path))
                dir_file.write(dir_file_)

    else:
        with open(dir_file_path, 'w') as dir_file:
            dir_file.write('[Desktop Entry]\nIcon={}\n'.format(NK_DIR + '.assets/'+icon_path))

NK_ICON = 'NewK.ico'
#DEV_ICON = 'NK.ico'
DEV_ICON = 'Dev.ico'
NOTES_ICON = 'Notes.ico'
SETUP_ICON = 'nk_.ico'
#SETUP_ICON = 'nk.ico'

set_folder_icon(NK_DIR_FILE, NK_ICON)
set_folder_icon(DEV_DIR_FILE, DEV_ICON)
set_folder_icon(NOTES_DIR_FILE, NOTES_ICON)
set_folder_icon(SETUP_DIR_FILE, SETUP_ICON)

SETUP_DOLPHIN = NK_DIR + 'Setup/Dolphin/'
with open(SETUP_DOLPHIN+'dirs-info.toml') as file:
    dirs_icon = toml.load(file)

def get_path_icon (dirs_icon):
    l=[]
    for i in dirs_icon.values():
        if 'path' in i.keys():
            if 'icon' in i.keys():
                l.append(i)
        else:
            l.extend(get_path_icon(i))
    return l

for i in get_path_icon(dirs_icon['nk']):
    set_folder_icon(NK_DIR+i['path']+'/.directory', i['icon'])
    os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{NK_DIR+i['path']+'/.directory'}'")

for i in get_path_icon(dirs_icon['nk-Dev']):
    set_folder_icon(NK_DIR+'Dev/'+i['path']+'/.directory', i['icon'])
    os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{NK_DIR+'Dev/'+i['path']+'/.directory'}'")

for i in get_path_icon(dirs_icon['nk-Notes']):
    set_folder_icon(NK_DIR+'Notes/'+i['path']+'/.directory', i['icon'])
    os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{NK_DIR+'Notes/'+i['path']+'/.directory'}'")

for i in get_path_icon(dirs_icon['home']):
    set_folder_icon(HOME_DIR+i['path']+'/.directory', i['icon'])
    os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{HOME_DIR+i['path']+'/.directory'}'")

for j in [*glob(SETUP_DOLPHIN+'dirs-info-*.toml'), *glob(SETUP_DOLPHIN+'dirs-info_*.toml')]:
    with open(j) as file:
        dirs_icon = toml.load(file)

    for i in get_path_icon(dirs_icon.get('nk', dict())):
        set_folder_icon(NK_DIR+i['path']+'/.directory', i['icon'])
        os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{NK_DIR+i['path']+'/.directory'}'")

    for i in get_path_icon(dirs_icon.get('home', dict())):
        set_folder_icon(HOME_DIR+i['path']+'/.directory', i['icon'])
        os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{HOME_DIR+i['path']+'/.directory'}'")

    for i in get_path_icon(dirs_icon.get('root', dict())):
        set_folder_icon(i['path']+'/.directory', i['icon'])
        os.system(f"sed 's#{'Icon='+NK_DIR+'.assets/'}#Icon=#g' -i '{i['path']+'/.directory'}'")

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

for i in ['config', 'data', 'ipy', 'mpl', 'sage']:
    os.makedirs(os.path.join(NK_DIR, f"Dev/jupyter/{i}"), exist_ok=True)

# Setting CONFIG & DATA dir for TeX
####################################

for i in ['live/texmf', 'live/texmf-local', 'repo/books']:
    os.makedirs(os.path.join(NK_DIR, f"Dev/tex/{i}"), exist_ok=True)

# Setting dirs related to Google langs and others
##################################################

for i in ['dart/flutter', 'go']:
    os.makedirs(os.path.join(NK_DIR, f"Dev/google/{i}"), exist_ok=True)

# Installing Jupyter and SageMath
##################################

os.system('sudo pacman -S sagemath python-ipykernel')

os.system('sudo -K')


#TODO add script to ignorespace from history and add ghs in history ignore
