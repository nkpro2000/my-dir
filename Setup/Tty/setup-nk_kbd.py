# .map vs .inc #YET2DO

#SKIPLINES: done

#nk-kbdmap-include-n-: #nk-kbdmap-exclude-PATTERN:
#DEFINE: done
#KEYMAPS: done
#META_: done

#PATH:

import os
import re
import shlex
import shutil

HOME_DIR = os.environ['HOME'] + '/'
NK_DIR = HOME_DIR + 'nk/'
TTY_SETUP_DIR = NK_DIR + 'Setup/Tty/'
TTY_SETUP_DIR = NK_DIR + 'Lobby/my-dir/Setup/Tty/'
KEYMAPS_DIR = TTY_SETUP_DIR + 'keymaps/'
KEYMAPS_TMP_DIR = TTY_SETUP_DIR + 'keymaps/tmp/'
DEFAULT_KBD_KEYMAP_DIR = '/usr/share/kbd/keymaps/'

KEYSYM = re.compile(r'(0x[0-9abcdef]{4})\t([0-9a-zA-Z_-]+)')
KEYSYM_SYNONYMS = re.compile(r'([0-9a-zA-Z_-]+) +for +([0-9a-zA-Z_-]+)')

MODIFIRES = ['shift', 'altgr', 'control', 'alt', 'shiftl', 'shiftr', 'ctrll', 'ctrlr', 'capsshift']

KEYCODE_MAP = re.compile(r'([ a-z]*?)keycode +([0-9]+) += +([ 0-9a-zA-Z+_-]+)')
VERBOSE = True


def get_modifiers(w:int) -> str:
    if w==0: return 'plain'

    modifiers = []
    for i,j in zip(bin(w)[:1:-1], MODIFIRES):
        if i == '1':
            modifiers.append(j)

    modifiers_order = [3, 1, 4, 2, -1, -2, -3, -4, -10]
    modifiers.sort(key= lambda x:modifiers_order[MODIFIRES.index(x)])

    return ' '.join(modifiers)


with open(TTY_SETUP_DIR + 'docs/dumpkeys-l_notes') as f:
    dl = f.read().splitlines()

keysyms : list[tuple[str, str]] = []
keysym_synonyms : list[tuple[str, str]] = []
for i in dl:
    if m:=KEYSYM.match(i) :
        keysyms.append(m.groups())
    elif m:=KEYSYM_SYNONYMS.match(i) :
        keysym_synonyms.append(m.groups())


def do_skiplines(skips:list[tuple[int, int|str]], lines:list[str]) -> list[str]:
    for i,n in skips:
        if type(n) == int:
            if n > 0:
                lines[i:i+n+1] = [None]*(n+1)
            elif n < 0:
                lines[i+n:i+1] = [None]*(-n+1)
            else: # n==0 # Just to skip the #SKIPLINES:...
                lines[i] = None
        elif n == 'AllAbove':
            lines[:i+1] = [None]*(i+1)
        else: # n=='AllBelow'
            lines[i:] = [None]*len(lines[i:])
    
    return [x for x in lines if x is not None]

def skiplines():
    for file in os.listdir(KEYMAPS_DIR):
        if os.path.isdir(KEYMAPS_DIR + file):
            continue # Skip dirs tmp/
        if not (file.endswith('.map') or file.endswith('.inc')):
            continue # Skip other files like .map_notes
        with open(KEYMAPS_DIR + file) as f:
            lines = f.read().splitlines(keepends=True)
        skiplines = []
        for i, line in enumerate(lines):
            if line.startswith('#SKIPLINES:'):
                n = line.split()[0][11:]
                if n == '': n = 'AllBelow'
                elif n == '-': n = 'AllAbove'
                elif n.isdigit(): n = int(n)
                elif n.startswith('-') and n[1:].isdigit(): n = int(n)
                elif n in ('AllBelow', 'AllAbove'): n = n
                else:
                    raise LookupError('Mentioned argument is unknown. Acceptable args are:' + \
                                        "'', 'AllBelow', '-', 'AllAbove', [0-9]+, \-[0-9]+")
                skiplines.append((i, n))
        lines = do_skiplines(skiplines, lines)
        with open(KEYMAPS_TMP_DIR + file, 'w') as f:
            f.write(''.join(lines))


def parse_include_exclude(): pass
def do_include_exclude(): pass
def include_exclude(lines:list[str]) -> list[str]:
    lines_out = lines#[]

    #YET2DO

    return lines_out


def replace_defines(lines:list[str]) -> list[str]:
    lines_out = [] 
    
    defines = []
    for line in lines:
        if line.startswith('#DEFINE:'):
            a,b = line[8:].split()[:2]
            defines.append((re.compile('(?<!\S)'+re.escape(a)+'(?!\S)'), b)) #Look4Doc#
    
    for line in lines:
        if line.startswith('#DEFINE:'):
            continue # Removing #DEFINE: , as no use after this.
        if not line.startswith('#'):
            for pat,rpl in defines:
                line = pat.sub(rpl, line)
        lines_out.append(line)
    
    return lines_out


def keymaps_line(kml:list[int], lines:list[str]) -> list[str]:
    lines_out = []
    for line in lines :
        if len(line)==0 or line.isspace() :
            lines_out.append(''); continue
        if line.startswith('#') :
            lines_out.append(line); continue
        if not (m:=KEYCODE_MAP.match(line)) :
            lines_out.extend([
                '#MetaString#', #Look4Doc#
                line.strip()
            ])
            if VERBOSE:
                print('|> #MetaString#', line.strip())
            continue
        
        ms, kc, ks = m.groups()
        ks = ks.split()
        if len(ms)==0 or ms.isspace():
            if len(ks) > len(kml):
                raise LookupError('Keysymbols beyond columns specified in keymapsline.')
            for mk in zip(kml, ks):
                if mk[1] != 'SKIP': #Look4Doc#
                    lines_out.append(f'{get_modifiers(mk[0])} keycode {kc} = {mk[1]}')
        else:
            if len(ks) != 1:
                raise LookupError('There must be only one keysymbole, if defined with modifiers.')
            lines_out.append(f'{ms.strip()} keycode {kc} = {ks[0]}')
    
    return lines_out

def add_meta_for_asciis(meta_:list[str], lines:list[str]) -> list[str]:
    lines_out = []
    for line in lines:
        if (m:=KEYCODE_MAP.match(line)) :
            ms, kc, ks = m.groups()
            ks = ks.split()
            if len(ks) != 1:
                # All keycode maps must be defined with modifiers,
                # since this fn is called after above fn `keymaps_line`.
                raise LookupError('There must be only one keysymbole, if defined with modifiers.')
            lines_out.append(line)
            
            m_k = ks[0].lstrip('+')
            ms = ms.strip()
            ms = ' '+ms if ms != 'plain' else ''
            for m_ in meta_:
                if m_ in ms:
                    lines_out.insert(-1, '#May overwrite/affected_by Meta Modifiers defined lines#') #Look4Doc#
                    if VERBOSE:
                        print('|> #May overwrite/affected_by Meta Modifiers defined lines#')
                        print('|> ' + line)
                    break # Don't redefine.
            else:
                for s in keysym_synonyms:
                    if s[0] == m_k:
                        m_k = s[1]
                if f'Meta_{m_k}' in (x[1] for x in keysyms):
                    for m_ in meta_:
                        lines_out.append(f'  {m_}{ms} keycode {kc} = Meta_{m_k}')
        else:
            lines_out.append(line)
    
    return lines_out


# Cleaning temp folder
shutil.rmtree(KEYMAPS_TMP_DIR + 'out', ignore_errors=True)
for file in os.listdir(KEYMAPS_TMP_DIR):
    os.remove(KEYMAPS_TMP_DIR + file)

# * Skiplines according to `#SKIPLINES:`
skiplines()

# * Open all files and parse&do other special tags.
for file in os.listdir(KEYMAPS_TMP_DIR):
    if not (file.endswith('.map') or file.endswith('.inc')):
        continue # Skip other files like .map_notes
    with open(KEYMAPS_TMP_DIR + file) as f:
        lines = f.read().splitlines()
    
    ## * Parse include and exclude tags and insert lines accordingly.
    lines = include_exclude(lines)
    
    ## * Replace defined tokens
    lines = replace_defines(lines)
    
    ## * Define keysym for keycodes according to #KEYMAPS: .
    ### * Parsing #KEYMAPS: .
    keymaps_lines = [(None, list(range(256)))]
    for i, line in enumerate(lines):
        if line.startswith('#KEYMAPS:'):
            keymaps_lines.append((i, []))
            try:
                for c in line[9:].split(','): #Look4Doc#
                    if (r:=c.find('-')) != -1:
                        keymaps_lines[-1][1].extend(range(int(c[:r]), int(c[r+1:])+1))
                    else:
                        keymaps_lines[-1][1].append(int(c))
            except Exception as e:
                print(f'?> Error : {e} \n?> \'-> Caused by line : {line}')
                raise e
    ### * Mention range for #KEYMAPS: .
    for i, to_ in enumerate(keymaps_lines[1:]+[(None, None)]):
        from_ = keymaps_lines[i][0]
        keymaps_lines[i] = ((None if from_ is None else (from_+1), to_[0]), keymaps_lines[i][1])
        # Removing #KEYMAPS: , as no use after this.     ^^^^^^^
    ### * Define lines accordingly.
    lines_ = []
    for kml in keymaps_lines:
        lines_.extend(keymaps_line(kml[1], lines[kml[0][0]:kml[0][1]]))
    lines = lines_
    
    ## * Define meta_ accroding to #META_: .
    ### * Parsing #META_: .
    meta_lines = [(None, [])]
    for i, line in enumerate(lines):
        if line.startswith('#META_:'):
            meta_lines.append((i, line[7:].split())) #Look4Doc#
    ### * Mention range for #META_: .
    for i, to_ in enumerate(meta_lines[1:]+[(None, None)]):
        from_ = meta_lines[i][0]
        meta_lines[i] = ((from_, to_[0]), meta_lines[i][1])
        # Don't Removing #META_: , may help why these mapping lines there.
    ### * Define lines accordingly.
    lines_ = []
    for kml in meta_lines:
        if len(kml[1]) > 0:
            lines_.extend(add_meta_for_asciis(kml[1], lines[kml[0][0]:kml[0][1]]))
        else:
            lines_.extend(lines[kml[0][0]:kml[0][1]])
    lines = lines_
    
    ## * Put the keymap files in the location mentioned in #PATH: .
    paths = []
    lines_ = []
    for line in lines:
        if line.startswith('#PATH:'):
            paths.append(shlex.split(line[6:])[0]) #Look4Doc#
            # Removing #PATH: .
        else:
            lines_.append(line)
    lines = lines_
    for path in paths: #Look4Doc#
        if path.startswith('/'):
            path_ = path
        elif path.startswith('.'):
            path_ = KEYMAPS_DIR + path
        else:
            path_ = DEFAULT_KBD_KEYMAP_DIR + path
        path_ = KEYMAPS_TMP_DIR + 'out' + path_
        # Put the output file in tmp/out/ then can be converted and moved
        # to right location, using other script with right permissions.
        try:
            os.makedirs(os.path.dirname(path_), exist_ok=True)
            with open(os.path.join(path_, file), 'w') as f:
                f.write('\n'.join(lines) + '\n')
        except Exception as e:
            print(e)

# * Put the keymap files in their locations.
script = r'''
cd '''+ KEYMAPS_TMP_DIR+'out/' + r'''

for file in $(find ./ -type f -name '*.map'| cut -d. -f2-); do
    gzip "./$file" && mv "./${file}.gz" "${file}.gz"
    #mv "./$file" "$file"
done

for file in $(find ./ -type f -name '*.inc'| cut -d. -f2-); do
    mv "./$file" "$file"
done

'''
with open(KEYMAPS_TMP_DIR+'move_script.sh', 'w') as f:
    f.write(script)
os.system('sudo bash '+ KEYMAPS_TMP_DIR+'move_script.sh')
os.system('sudo -K')
