# .map vs .inc

#SKIPLINES:

#nk-kbdmap-include-n-: #nk-kbdmap-exclude-PATTERN:
#DEFINE:
#KEYMAPS: done    (only on .map files, .inc will be pasted then KEYMAPS)
#META_: done

#PATH:

import re

KEYSYM = re.compile(r'(0x[0-9abcdef]{4})\t([0-9a-zA-Z_-]+)')
KEYSYM_SYNONYMS = re.compile(r'([0-9a-zA-Z_-]+) +for +([0-9a-zA-Z_-]+)')

MODIFIRES = ['shift', 'altgr', 'control', 'alt', 'shiftl', 'shiftr', 'ctrll', 'ctrlr', 'capsshift']

KEYCODE_MAP = re.compile(r'([ a-z]*?)keycode +([0-9]+) += +([ 0-9a-zA-Z+_-]+)')


def get_modifiers(w):
    if w==0: return 'plain'

    modifiers = []
    for i,j in zip(bin(w)[:1:-1], MODIFIRES):
        if i == '1':
            modifiers.append(j)

    modifiers_order = [3, 1, 4, 2, -1, -2, -3, -4, -10]
    modifiers.sort(key= lambda x:modifiers_order[MODIFIRES.index(x)])

    return ' '.join(modifiers)


with open('./docs/dumpkeys-l_notes') as f:
    dl = f.read().splitlines()

keysyms = []
keysym_synonyms = []
for i in dl:
    if m:=KEYSYM.match(i) :
        keysyms.append(m.groups())
    elif m:=KEYSYM_SYNONYMS.match(i) :
        keysym_synonyms.append(m.groups())


def parse_keymap_file(lines) :
    keymaps_line = list(range(256))
    keycode_map_ = []
    keycode_maps = []
    for line in lines:
        try:
            if len(line) > 0:
                if line.startswith('#KEYMAPS:'):
                    keymaps_line = []
                    for i in line[9:].split(','):
                        if (j:=i.find('-')) != -1:
                            keymaps_line.extend(range(int(i[:j]), int(i[j+1:])+1))
                        else:
                            keymaps_line.append(int(i))
                elif line.startswith('#META_:'):
                    keycode_map_ = []
                    for i in line [7:].split():
                        keycode_map_.append(f'#META_:{i}')
                elif line[0] != '#':
                    if m:=KEYCODE_MAP.match(line) :
                        keycode_maps.append(m.groups())
                    else:
                        keycode_map_.append(line.strip())
        except Exception as e:
            print(f'?> Error : {e} \n?> \'-> Caused by line : {line}')
            raise e

    return keymaps_line, keycode_map_, keycode_maps

def gen_keymaps(kl, kmaps_, kmaps) :
    keymaps = [*(x for x in kmaps_ if not x.startswith('#META_:')), '','']
    for i in kmaps:
        if i[0]:
            print(i) #format here
        else:
            for j in zip(kl, i[2].split()):
                if j[1]!='SKIP':
                    keymaps.append(f'{get_modifiers(j[0])} keycode {i[1]} = {j[1]}')

                    m_k = j[1].lstrip('+')
                    for s in keysym_synonyms:
                        if s[0] == m_k:
                            m_k = s[1]
                    if f'Meta_{m_k}' in (x[1] for x in keysyms):
                        for k in kmaps_:
                            if k.startswith('#META_:'):
                                keymaps.append(f'    {k[7:]} {get_modifiers(j[0]).replace("plain","")} '\
                                    +f'keycode {i[1]} = Meta_{m_k}')

        keymaps.append('')

    return '\n'.join(keymaps)





with open('./keymaps/nk_kbd-us-alpnum.map') as f:
    lines = f.read().splitlines()

r = parse_keymap_file(lines)
print(gen_keymaps(*r))
