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
VERBOSE = True


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


def keymaps_line(kml:list[int], lines:list[str]) :
    lines_out = []
    for line in lines :
        if len(line)==0 or line.isspace() :
            lines_out.append(''); continue
        if line.startswith('#') :
            lines_out.append(line); continue
        if not (m:=KEYCODE_MAP.match(line)) :
            lines_out.extend([
                '#MetaString#',
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
                if mk[1] != 'SKIP':
                    lines_out.append(f'{get_modifiers(mk[0])} keycode {kc} = {mk[1]}')
        else:
            if len(ks) != 1:
                raise LookupError('There must be only one keysymbole, if defined with modifiers.')
            lines_out.append(f'{ms.strip()} keycode {kc} = {ks[0]}')
    
    return lines_out

def add_meta_for_asciis(meta_:list[str], lines:list[str]):
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
                    lines_out.insert(-1, '#May overwrite/affected_by Meta Modifiers defined lines#')
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


with open('./keymaps/nk_kbd-us-alpnum.map') as f:
    lines = f.read().splitlines()

print('\n'.join(add_meta_for_asciis(['alt', 'altgr'], keymaps_line([0,1,4,5], lines))))