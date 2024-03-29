# Loadkeys

> Extracted from : https://deskthority.net/wiki/Loadkeys
> Learned from : https://github.com/haata/KeyboardLayouts.git

**loadkeys** is a program that reads a file or set of files used to assign a keymap for the console. Console being the terminal **above** the X Server.

These maps are usually located under <tt>kbd/keymaps/<arch></tt> (e.g. <tt>/usr/share/kbd/keymaps/<arch></tt>) and are just gzips of the loadkey files that are used as input for the loadkeys program.

## loadkeys keymap

The keymap file is a keycode assignment of the all of letters/modifiers that activate when the keycode is signalled by the kernel to generate a key event. In other words, each key on the keyboard is assigned a keycode by the kernel driver, which is signalled by the keyboard device, which corresponds to the letter/modifier that has been assigned.

## Keycode Assignment Syntax

Using the 'a' character as an example to map to the A key on a US ANSI QWERTY keyboard.

**Note**: Keycodes can vary between kernel versions/types.

```bash
keycode 30 = a
```

The keyword **keycode** refers to keycode #30 and assigns the **a** character to the keycode.
**A**, the shifted version of **a**, is automagically added to the keymap table (internally within the kernel, in its giant lookup table).

## Basic Layered Definitions

The shift layer can also be hardcoded, using the **a A** example again.

```bash
keycode 30 = a A
```

This defines **a** as the base symbol to the keycode 30, as well as adding the **A** whenever a shift of 1 is applied to the keymap table. This shift of 1 should not be confused with the shift on your keyboard.

More shift levels can be applied to each keycode.

```bash
keycode 6 = five percent euro yen
```

This is an example from the Colemak keymap by Shai Coleman. Keycode 6 (which is the 5 key) has the character **5** by default, **%** when shifted once, **€** when shifted twice, and **¥** when shifted three times. A 2 shift is associated to the AltGr, and 3 shift is Shift+AltGr for Colemak. Each type of shift is given a certain weighting, and allows for many levels of keymappings.

Another important thing to note is how **five** is used instead of **5**. Each character/function has a label associated with it. There is a **list** of all usable symbols <tt>dumpkeys --long-info</tt>, unfortunately, there is no description of what the symbols do, and their functions needs to be guessed...
There are multiple labels per key (Numerical, Octal, etc.), please refer to <tt>man keymaps</tt> for more details.

## Modifier Definitions

The definition for the Left Shift key on most keyboards.

```bash
keycode 42 = Shift
```

#### Note
> * It is generally a BAD idea to layer things onto "modifier" keys as it doesn't always work as you might expect it
> * Please note **Shift** instead of **shift**, the keymaps are case sensitive and **shift** means something else and is not a modifier label to assign to a keycode

For convenience, a list of known modifiers (Arch Linux kernel 2.6.36):  
> Alt  
> AltGr  
> Control  
> Shift  
> ShiftL  
> ShiftR  
> CtrlL  
> CtrlR  
> CapsShift  

Besides **CapsShift**, which has unknown usage, each of these modifiers represents a **shift** amount.

Each **modifier** has a shift weight associated with it, as noted in the below table (can also be found in <tt>man keymaps</tt>):

 Modifier  | Weight  
 ----------|:------:
 Shift 	   |  1  
 AltGr     |  2  
 Control   |  4  
 Alt       |  8  
 ShiftL    |  16  
 ShiftR    |  32  
 CtrlL     |  64  
 CtrlR     | 128  
 CapsShift | 256  

This weighting scheme directly translates into the internal kernel keymap table. Thus it is quite easy to figure out the combinations of modifiers.

For example, if `Shift` is activated, then a weight of 1 is applied to all of the keys pressed while the weighting is active.
If `Control` and `Alt` are activated, then a weight of 12 is applied to all of the keys pressed while the weighting is active.

Thus a weighting of 0 is the default weighting column in the keymap table (also known as `plain`).

From testing, a max weighting of 255 may be applied (as the table has 256 columns). Which leaves no room for `CapsShift`...

## Specific Layout Definitions

Rather than stacking the assigned functions like this arbitrary command,

```bash
keycode 1 = a b d s h e t five eight X N S A
```

which makes it difficult to figure out the actual keys to press to get the final 'A', keycodes can be defined by their shift level.

```bash
 plain                   keycode  30 = a
 shift                   keycode  30 = A
       altgr             keycode  30 = aacute
 shift altgr             keycode  30 = Aacute
             control     keycode  30 = Control_a
 shift       control     keycode  30 = VoidSymbol
       altgr control     keycode  30 = VoidSymbol
 shift altgr control     keycode  30 = VoidSymbol
                     alt keycode  30 = Meta_a
 shift               alt keycode  30 = Meta_A
       altgr         alt keycode  30 = VoidSymbol
             control alt keycode  30 = Meta_Control_a
 shift altgr         alt keycode  30 = VoidSymbol
       altgr control alt keycode  30 = VoidSymbol
 shift       control alt keycode  30 = VoidSymbol
 shift altgr control alt keycode  30 = VoidSymbol
```

It is still possible to use the previous method to set a higher level shift.

```bash
keycode 30 = a A VoidSymbol VoidSymbol VoidSymbol V
```

### Control_a
This is a define to programs that we want to signal <tt>Control+a</tt> to the given program, say vim/emacs. Each of these defines are part of a list, but anyone you try should work.

### Meta_a
Due to emacs really needing Meta, Alt is typically defined as Meta on modern keyboards. Again, another modifier label.

### Meta_Control_a
Yes, it's possible to chain up modifiers as well. But again, there needs to be a label defined in the kernel for this (most should work, but it's possible for some not to work).

### VoidSymbol
No action should be done on this keycode action. This is very important if you are trying to override a previous layout.
As a quick tip, any keycode that is not define (or was previously not defined) is set to VoidSymbol by default.

### shift, shiftl, shiftr, ctrl, ctrll, ctrlr, alt and altgr
`shift` is not the same as `Shift`. `shift` defines the keymap weighting when `Shift` is activated. altgr, control, alt, shiftl, shiftr, ctrll, and ctrlr all behave the same way, and are just different shift levels (similar names are just used to confuse you and give some indication of where they may be mapped to).

### plain
`plain` is redundant, and not needed. However it often makes configuration files easier to read (and doing things like regex).

## Locks

All of the modifiers has their own "Lock" function. It works as expected, and sets the current weight to whatever lock is activated. To remove a lock, just signal that modifier again.

### Normal Locks
> Shift_Lock  
> AltGr_Lock  
> Control_Lock  
> Alt_Lock  
> ShiftL_Lock  
> ShiftR_Lock  
> CtrlL_Lock  
> CtrlR_Lock  
> CapsShift_Lock (Unsure of what this actually does...)  

Now, there are some *other* types of lock function symbols, such as `Caps_Lock` and `Num_Lock`

### Special Locks
> Num_Lock  
> Scroll_Lock  
> Caps_Lock  
> Bare_Num_Lock  

### Typewriter Style Locks
> Caps_On  
> Uncaps_Shift  

## Latches

Latches are like locks except that the mod unlocks as soon as one non-modifier key is pressed.

> SShift  
> SAltGr  
> SControl  
> SAlt  
> SShiftL  
> SShiftR  
> SCtrlL  
> SCtrlR  
> SCapsShift (Unsure of what this actually does...)  

## Number Pad

The symbols used for the keypad are a little bit different.
The notation is simple, a standard numpad can be seen below.

> KP_1 → 1  
> KP_2 → 2  
> KP_3 → 3  
> KP_4 → 4  
> KP_5 → 5  
> KP_6 → 6  
> KP_7 → 7  
> KP_8 → 8  
> KP_9 → 9  
> KP_0 → 0  
> KP_Add → +  
> KP_Subtract → -  
> KP_Multiply → *  
> KP_Divide → /  
> KP_Enter → Enter  
> KP_Period → .  

## Includes

An interesting attribute of LoadKeys is that each layout that is loaded modifies the previously defined one.
This means that it is possible to layer these keymap definitions right inside the keymap definition by using `include` statements. It should be noted that where the include is inserted into the keymap could possibly change the result, as the included keymap will overwrite any of the changes up to that point.

```bash
include "<path to the keymap>"
```

## Compose

Compose is a function that allows users to chain together symbols in order to represent others (digraphs). Not really that common for English, but is for some of the European languages. Compose also for the combination of 2 characters to be turned into another character. For example **~** + **A** = **Ã**. This is the same as using <tt>Ctrl+K</tt> in vi/vim.

```bash
compose '~' 'A' to 'Ã'
```

In order to use the Compose functionality, a key must be defined as **Compose**.

```bash
keycode 23 = Compose
```

## Super and Hyper

#TODO

## Strings

It is possible to predefine sets of character output as a keysym. This is often used from the F1-12 keys. Please note that the keysym much already be defined (there are a lot of unused ones, so this is typically not an issue). In the below case **F100** is used.

```bash
string F100 = "Output"
keycode 20 = F100
```

For more details on special characters please refer to `man keymaps`.

## Comments

Bash style comments are used with either "#"'s or "!"'s.

```bash
# Here is a comment
keycode 30 = a A # Another comment
! Comment as well
```

## Useful Tools

* **loadkeys** - It's how you set your keymap (remember to run as root)
* **dumpkeys** - Can give you a dump of your current keymap, as well as all of the possible keysyms (doesn't tell you what they do unfortunately)
* **showkey** - Nice tool for determining keycodes and key outputs. If a key doesn't output anything but it should (e.g. Not an FN key) then read the man page, as you need to specify some kernel boot opitions

## Useful man pages

- man keymaps
- man loadkeys
- man dumpkeys
- man showkey

## Complex Example

HaaTa created a very complex layering system using loadkeys. It is recommended to use regex to make modifications. A template is also provided.
The layout files are extremely long, but are well commented. There may be keycode numbering differences to your kernel version.

HaaTa's complex multi-layered loadkey layouts [https://github.com/haata/KeyboardLayouts/tree/master/loadkeys](https://github.com/haata/KeyboardLayouts/tree/master/loadkeys "HaaTa's complex multi-layered loadkey layouts")

## Keysym Glossary

A basic listing of keysyms and definitions as based off of kbd 1.15.2-1 (Arch Linux). (TODO definitions)

### Symbols List

 (numeric value, symbol, definition)  
 0x0000	nul  
 0x0001	Control_a  
 0x0002	Control_b  
 0x0003	Control_c  
 0x0004	Control_d  
 0x0005	Control_e  
 0x0006	Control_f  
 0x0007	Control_g  
 0x0008	BackSpace  
 0x0009	Tab  
 0x000a	Linefeed  
 0x000b	Control_k  
 0x000c	Control_l  
 0x000d	Control_m  
 0x000e	Control_n  
 0x000f	Control_o  
 0x0010	Control_p  
 0x0011	Control_q  
 0x0012	Control_r  
 0x0013	Control_s  
 0x0014	Control_t  
 0x0015	Control_u  
 0x0016	Control_v  
 0x0017	Control_w  
 0x0018	Control_x  
 0x0019	Control_y  
 0x001a	Control_z  
 0x001b	Escape  
 0x001c	Control_backslash  
 0x001d	Control_bracketright  
 0x001e	Control_asciicircum  
 0x001f	Control_underscore  
 0x0020	space  
 0x0021	exclam  
 0x0022	quotedbl  
 0x0023	numbersign  
 0x0024	dollar  
 0x0025	percent  
 0x0026	ampersand  
 0x0027	apostrophe  
 0x0028	parenleft  
 0x0029	parenright  
 0x002a	asterisk  
 0x002b	plus  
 0x002c	comma  
 0x002d	minus  
 0x002e	period  
 0x002f	slash  
 0x0030	zero  
 0x0031	one  
 0x0032	two  
 0x0033	three  
 0x0034	four  
 0x0035	five  
 0x0036	six  
 0x0037	seven  
 0x0038	eight  
 0x0039	nine  
 0x003a	colon  
 0x003b	semicolon  
 0x003c	less  
 0x003d	equal  
 0x003e	greater  
 0x003f	question  
 0x0040	at  
 0x0041	A  
 0x0042	B  
 0x0043	C  
 0x0044	D  
 0x0045	E  
 0x0046	F  
 0x0047	G  
 0x0048	H  
 0x0049	I  
 0x004a	J  
 0x004b	K  
 0x004c	L  
 0x004d	M  
 0x004e	N  
 0x004f	O  
 0x0050	P  
 0x0051	Q  
 0x0052	R  
 0x0053	S  
 0x0054	T  
 0x0055	U  
 0x0056	V  
 0x0057	W  
 0x0058	X  
 0x0059	Y  
 0x005a	Z  
 0x005b	bracketleft  
 0x005c	backslash  
 0x005d	bracketright  
 0x005e	asciicircum  
 0x005f	underscore  
 0x0060	grave  
 0x0061	a  
 0x0062	b  
 0x0063	c  
 0x0064	d  
 0x0065	e  
 0x0066	f  
 0x0067	g  
 0x0068	h  
 0x0069	i  
 0x006a	j  
 0x006b	k  
 0x006c	l  
 0x006d	m  
 0x006e	n  
 0x006f	o  
 0x0070	p  
 0x0071	q  
 0x0072	r  
 0x0073	s  
 0x0074	t  
 0x0075	u  
 0x0076	v  
 0x0077	w  
 0x0078	x  
 0x0079	y  
 0x007a	z  
 0x007b	braceleft  
 0x007c	bar  
 0x007d	braceright  
 0x007e	asciitilde  
 0x007f	Delete  
 0x00a0	nobreakspace  
 0x00a1	exclamdown  
 0x00a2	cent  
 0x00a3	sterling  
 0x00a4	currency  
 0x00a5	yen  
 0x00a6	brokenbar  
 0x00a7	section  
 0x00a8	diaeresis  
 0x00a9	copyright  
 0x00aa	ordfeminine  
 0x00ab	guillemetleft  
 0x00ac	notsign  
 0x00ad	hyphen  
 0x00ae	registered  
 0x00af	macron  
 0x00b0	degree  
 0x00b1	plusminus  
 0x00b2	twosuperior  
 0x00b3	threesuperior  
 0x00b4	acute  
 0x00b5	mu  
 0x00b6	paragraph  
 0x00b7	periodcentered  
 0x00b8	cedilla  
 0x00b9	onesuperior  
 0x00ba	masculine  
 0x00bb	guillemetright  
 0x00bc	onequarter  
 0x00bd	onehalf  
 0x00be	threequarters  
 0x00bf	questiondown  
 0x00c0	Agrave  
 0x00c1	Aacute  
 0x00c2	Acircumflex  
 0x00c3	Atilde  
 0x00c4	Adiaeresis  
 0x00c5	Aring  
 0x00c6	AE  
 0x00c7	Ccedilla  
 0x00c8	Egrave  
 0x00c9	Eacute  
 0x00ca	Ecircumflex  
 0x00cb	Ediaeresis  
 0x00cc	Igrave  
 0x00cd	Iacute  
 0x00ce	Icircumflex  
 0x00cf	Idiaeresis  
 0x00d0	ETH  
 0x00d1	Ntilde  
 0x00d2	Ograve  
 0x00d3	Oacute  
 0x00d4	Ocircumflex  
 0x00d5	Otilde  
 0x00d6	Odiaeresis  
 0x00d7	multiply  
 0x00d8	Ooblique  
 0x00d9	Ugrave  
 0x00da	Uacute  
 0x00db	Ucircumflex  
 0x00dc	Udiaeresis  
 0x00dd	Yacute  
 0x00de	THORN  
 0x00df	ssharp  
 0x00e0	agrave  
 0x00e1	aacute  
 0x00e2	acircumflex  
 0x00e3	atilde  
 0x00e4	adiaeresis  
 0x00e5	aring  
 0x00e6	ae  
 0x00e7	ccedilla  
 0x00e8	egrave  
 0x00e9	eacute  
 0x00ea	ecircumflex  
 0x00eb	ediaeresis  
 0x00ec	igrave  
 0x00ed	iacute  
 0x00ee	icircumflex  
 0x00ef	idiaeresis  
 0x00f0	eth  
 0x00f1	ntilde  
 0x00f2	ograve  
 0x00f3	oacute  
 0x00f4	ocircumflex  
 0x00f5	otilde  
 0x00f6	odiaeresis  
 0x00f7	division  
 0x00f8	oslash  
 0x00f9	ugrave  
 0x00fa	uacute  
 0x00fb	ucircumflex  
 0x00fc	udiaeresis  
 0x00fd	yacute  
 0x00fe	thorn  
 0x00ff	ydiaeresis  
 0x0100	F1  
 0x0101	F2  
 0x0102	F3  
 0x0103	F4  
 0x0104	F5  
 0x0105	F6  
 0x0106	F7  
 0x0107	F8  
 0x0108	F9  
 0x0109	F10  
 0x010a	F11  
 0x010b	F12  
 0x010c	F13  
 0x010d	F14  
 0x010e	F15  
 0x010f	F16  
 0x0110	F17  
 0x0111	F18  
 0x0112	F19  
 0x0113	F20  
 0x0114	Find  
 0x0115	Insert  
 0x0116	Remove  
 0x0117	Select  
 0x0118	Prior  
 0x0119	Next  
 0x011a	Macro  
 0x011b	Help  
 0x011c	Do  
 0x011d	Pause  
 0x011e	F21  
 0x011f	F22  
 0x0120	F23  
 0x0121	F24  
 0x0122	F25  
 0x0123	F26  
 0x0124	F27  
 0x0125	F28  
 0x0126	F29  
 0x0127	F30  
 0x0128	F31  
 0x0129	F32  
 0x012a	F33  
 0x012b	F34  
 0x012c	F35  
 0x012d	F36  
 0x012e	F37  
 0x012f	F38  
 0x0130	F39  
 0x0131	F40  
 0x0132	F41  
 0x0133	F42  
 0x0134	F43  
 0x0135	F44  
 0x0136	F45  
 0x0137	F46  
 0x0138	F47  
 0x0139	F48  
 0x013a	F49  
 0x013b	F50  
 0x013c	F51  
 0x013d	F52  
 0x013e	F53  
 0x013f	F54  
 0x0140	F55  
 0x0141	F56  
 0x0142	F57  
 0x0143	F58  
 0x0144	F59  
 0x0145	F60  
 0x0146	F61  
 0x0147	F62  
 0x0148	F63  
 0x0149	F64  
 0x014a	F65  
 0x014b	F66  
 0x014c	F67  
 0x014d	F68  
 0x014e	F69  
 0x014f	F70  
 0x0150	F71  
 0x0151	F72  
 0x0152	F73  
 0x0153	F74  
 0x0154	F75  
 0x0155	F76  
 0x0156	F77  
 0x0157	F78  
 0x0158	F79  
 0x0159	F80  
 0x015a	F81  
 0x015b	F82  
 0x015c	F83  
 0x015d	F84  
 0x015e	F85  
 0x015f	F86  
 0x0160	F87  
 0x0161	F88  
 0x0162	F89  
 0x0163	F90  
 0x0164	F91  
 0x0165	F92  
 0x0166	F93  
 0x0167	F94  
 0x0168	F95  
 0x0169	F96  
 0x016a	F97  
 0x016b	F98  
 0x016c	F99  
 0x016d	F100  
 0x016e	F101  
 0x016f	F102  
 0x0170	F103  
 0x0171	F104  
 0x0172	F105  
 0x0173	F106  
 0x0174	F107  
 0x0175	F108  
 0x0176	F109  
 0x0177	F110  
 0x0178	F111  
 0x0179	F112  
 0x017a	F113  
 0x017b	F114  
 0x017c	F115  
 0x017d	F116  
 0x017e	F117  
 0x017f	F118  
 0x0180	F119  
 0x0181	F120  
 0x0182	F121  
 0x0183	F122  
 0x0184	F123  
 0x0185	F124  
 0x0186	F125  
 0x0187	F126  
 0x0188	F127  
 0x0189	F128  
 0x018a	F129  
 0x018b	F130  
 0x018c	F131  
 0x018d	F132  
 0x018e	F133  
 0x018f	F134  
 0x0190	F135  
 0x0191	F136  
 0x0192	F137  
 0x0193	F138  
 0x0194	F139  
 0x0195	F140  
 0x0196	F141  
 0x0197	F142  
 0x0198	F143  
 0x0199	F144  
 0x019a	F145  
 0x019b	F146  
 0x019c	F147  
 0x019d	F148  
 0x019e	F149  
 0x019f	F150  
 0x01a0	F151  
 0x01a1	F152  
 0x01a2	F153  
 0x01a3	F154  
 0x01a4	F155  
 0x01a5	F156  
 0x01a6	F157  
 0x01a7	F158  
 0x01a8	F159  
 0x01a9	F160  
 0x01aa	F161  
 0x01ab	F162  
 0x01ac	F163  
 0x01ad	F164  
 0x01ae	F165  
 0x01af	F166  
 0x01b0	F167  
 0x01b1	F168  
 0x01b2	F169  
 0x01b3	F170  
 0x01b4	F171  
 0x01b5	F172  
 0x01b6	F173  
 0x01b7	F174  
 0x01b8	F175  
 0x01b9	F176  
 0x01ba	F177  
 0x01bb	F178  
 0x01bc	F179  
 0x01bd	F180  
 0x01be	F181  
 0x01bf	F182  
 0x01c0	F183  
 0x01c1	F184  
 0x01c2	F185  
 0x01c3	F186  
 0x01c4	F187  
 0x01c5	F188  
 0x01c6	F189  
 0x01c7	F190  
 0x01c8	F191  
 0x01c9	F192  
 0x01ca	F193  
 0x01cb	F194  
 0x01cc	F195  
 0x01cd	F196  
 0x01ce	F197  
 0x01cf	F198  
 0x01d0	F199  
 0x01d1	F200  
 0x01d2	F201  
 0x01d3	F202  
 0x01d4	F203  
 0x01d5	F204  
 0x01d6	F205  
 0x01d7	F206  
 0x01d8	F207  
 0x01d9	F208  
 0x01da	F209  
 0x01db	F210  
 0x01dc	F211  
 0x01dd	F212  
 0x01de	F213  
 0x01df	F214  
 0x01e0	F215  
 0x01e1	F216  
 0x01e2	F217  
 0x01e3	F218  
 0x01e4	F219  
 0x01e5	F220  
 0x01e6	F221  
 0x01e7	F222  
 0x01e8	F223  
 0x01e9	F224  
 0x01ea	F225  
 0x01eb	F226  
 0x01ec	F227  
 0x01ed	F228  
 0x01ee	F229  
 0x01ef	F230  
 0x01f0	F231  
 0x01f1	F232  
 0x01f2	F233  
 0x01f3	F234  
 0x01f4	F235  
 0x01f5	F236  
 0x01f6	F237  
 0x01f7	F238  
 0x01f8	F239  
 0x01f9	F240  
 0x01fa	F241  
 0x01fb	F242  
 0x01fc	F243  
 0x01fd	F244  
 0x01fe	F245  
 0x01ff	F246  
 0x0200	VoidSymbol  
 0x0201	Return  
 0x0202	Show_Registers  
 0x0203	Show_Memory  
 0x0204	Show_State  
 0x0205	Break  
 0x0206	Last_Console  
 0x0207	Caps_Lock  
 0x0208	Num_Lock  
 0x0209	Scroll_Lock  
 0x020a	Scroll_Forward  
 0x020b	Scroll_Backward  
 0x020c	Boot  
 0x020d	Caps_On  
 0x020e	Compose  
 0x020f	SAK  
 0x0210	Decr_Console  
 0x0211	Incr_Console  
 0x0212	KeyboardSignal  
 0x0213	Bare_Num_Lock  
 0x0300	KP_0  
 0x0301	KP_1  
 0x0302	KP_2  
 0x0303	KP_3  
 0x0304	KP_4  
 0x0305	KP_5  
 0x0306	KP_6  
 0x0307	KP_7  
 0x0308	KP_8  
 0x0309	KP_9  
 0x030a	KP_Add  
 0x030b	KP_Subtract  
 0x030c	KP_Multiply  
 0x030d	KP_Divide  
 0x030e	KP_Enter  
 0x030f	KP_Comma  
 0x0310	KP_Period  
 0x0311	KP_MinPlus  
 0x0400	dead_grave  
 0x0401	dead_acute  
 0x0402	dead_circumflex  
 0x0403	dead_tilde  
 0x0404	dead_diaeresis  
 0x0405	dead_cedilla  
 0x0500	Console_1  
 0x0501	Console_2  
 0x0502	Console_3  
 0x0503	Console_4  
 0x0504	Console_5  
 0x0505	Console_6  
 0x0506	Console_7  
 0x0507	Console_8  
 0x0508	Console_9  
 0x0509	Console_10  
 0x050a	Console_11  
 0x050b	Console_12  
 0x050c	Console_13  
 0x050d	Console_14  
 0x050e	Console_15  
 0x050f	Console_16  
 0x0510	Console_17  
 0x0511	Console_18  
 0x0512	Console_19  
 0x0513	Console_20  
 0x0514	Console_21  
 0x0515	Console_22  
 0x0516	Console_23  
 0x0517	Console_24  
 0x0518	Console_25  
 0x0519	Console_26  
 0x051a	Console_27  
 0x051b	Console_28  
 0x051c	Console_29  
 0x051d	Console_30  
 0x051e	Console_31  
 0x051f	Console_32  
 0x0520	Console_33  
 0x0521	Console_34  
 0x0522	Console_35  
 0x0523	Console_36  
 0x0524	Console_37  
 0x0525	Console_38  
 0x0526	Console_39  
 0x0527	Console_40  
 0x0528	Console_41  
 0x0529	Console_42  
 0x052a	Console_43  
 0x052b	Console_44  
 0x052c	Console_45  
 0x052d	Console_46  
 0x052e	Console_47  
 0x052f	Console_48  
 0x0530	Console_49  
 0x0531	Console_50  
 0x0532	Console_51  
 0x0533	Console_52  
 0x0534	Console_53  
 0x0535	Console_54  
 0x0536	Console_55  
 0x0537	Console_56  
 0x0538	Console_57  
 0x0539	Console_58  
 0x053a	Console_59  
 0x053b	Console_60  
 0x053c	Console_61  
 0x053d	Console_62  
 0x053e	Console_63  
 0x0600	Down  
 0x0601	Left  
 0x0602	Right  
 0x0603	Up  
 0x0700	Shift  
 0x0701	AltGr  
 0x0702	Control  
 0x0703	Alt  
 0x0704	ShiftL  
 0x0705	ShiftR  
 0x0706	CtrlL  
 0x0707	CtrlR  
 0x0708	CapsShift  
 0x0800	Meta_nul  
 0x0801	Meta_Control_a  
 0x0802	Meta_Control_b  
 0x0803	Meta_Control_c  
 0x0804	Meta_Control_d  
 0x0805	Meta_Control_e  
 0x0806	Meta_Control_f  
 0x0807	Meta_Control_g  
 0x0808	Meta_BackSpace  
 0x0809	Meta_Tab  
 0x080a	Meta_Linefeed  
 0x080b	Meta_Control_k  
 0x080c	Meta_Control_l  
 0x080d	Meta_Control_m  
 0x080e	Meta_Control_n  
 0x080f	Meta_Control_o  
 0x0810	Meta_Control_p  
 0x0811	Meta_Control_q  
 0x0812	Meta_Control_r  
 0x0813	Meta_Control_s  
 0x0814	Meta_Control_t  
 0x0815	Meta_Control_u  
 0x0816	Meta_Control_v  
 0x0817	Meta_Control_w  
 0x0818	Meta_Control_x  
 0x0819	Meta_Control_y  
 0x081a	Meta_Control_z  
 0x081b	Meta_Escape  
 0x081c	Meta_Control_backslash  
 0x081d	Meta_Control_bracketright  
 0x081e	Meta_Control_asciicircum  
 0x081f	Meta_Control_underscore  
 0x0820	Meta_space  
 0x0821	Meta_exclam  
 0x0822	Meta_quotedbl  
 0x0823	Meta_numbersign  
 0x0824	Meta_dollar  
 0x0825	Meta_percent  
 0x0826	Meta_ampersand  
 0x0827	Meta_apostrophe  
 0x0828	Meta_parenleft  
 0x0829	Meta_parenright  
 0x082a	Meta_asterisk  
 0x082b	Meta_plus  
 0x082c	Meta_comma  
 0x082d	Meta_minus  
 0x082e	Meta_period  
 0x082f	Meta_slash  
 0x0830	Meta_zero  
 0x0831	Meta_one  
 0x0832	Meta_two  
 0x0833	Meta_three  
 0x0834	Meta_four  
 0x0835	Meta_five  
 0x0836	Meta_six  
 0x0837	Meta_seven  
 0x0838	Meta_eight  
 0x0839	Meta_nine  
 0x083a	Meta_colon  
 0x083b	Meta_semicolon  
 0x083c	Meta_less  
 0x083d	Meta_equal  
 0x083e	Meta_greater  
 0x083f	Meta_question  
 0x0840	Meta_at  
 0x0841	Meta_A  
 0x0842	Meta_B  
 0x0843	Meta_C  
 0x0844	Meta_D  
 0x0845	Meta_E  
 0x0846	Meta_F  
 0x0847	Meta_G  
 0x0848	Meta_H  
 0x0849	Meta_I  
 0x084a	Meta_J  
 0x084b	Meta_K  
 0x084c	Meta_L  
 0x084d	Meta_M  
 0x084e	Meta_N  
 0x084f	Meta_O  
 0x0850	Meta_P  
 0x0851	Meta_Q  
 0x0852	Meta_R  
 0x0853	Meta_S  
 0x0854	Meta_T  
 0x0855	Meta_U  
 0x0856	Meta_V  
 0x0857	Meta_W  
 0x0858	Meta_X  
 0x0859	Meta_Y  
 0x085a	Meta_Z  
 0x085b	Meta_bracketleft  
 0x085c	Meta_backslash  
 0x085d	Meta_bracketright  
 0x085e	Meta_asciicircum  
 0x085f	Meta_underscore  
 0x0860	Meta_grave  
 0x0861	Meta_a  
 0x0862	Meta_b  
 0x0863	Meta_c  
 0x0864	Meta_d  
 0x0865	Meta_e  
 0x0866	Meta_f  
 0x0867	Meta_g  
 0x0868	Meta_h  
 0x0869	Meta_i  
 0x086a	Meta_j  
 0x086b	Meta_k  
 0x086c	Meta_l  
 0x086d	Meta_m  
 0x086e	Meta_n  
 0x086f	Meta_o  
 0x0870	Meta_p  
 0x0871	Meta_q  
 0x0872	Meta_r  
 0x0873	Meta_s  
 0x0874	Meta_t  
 0x0875	Meta_u  
 0x0876	Meta_v  
 0x0877	Meta_w  
 0x0878	Meta_x  
 0x0879	Meta_y  
 0x087a	Meta_z  
 0x087b	Meta_braceleft  
 0x087c	Meta_bar  
 0x087d	Meta_braceright  
 0x087e	Meta_asciitilde  
 0x087f	Meta_Delete  
 0x0900	Ascii_0  
 0x0901	Ascii_1  
 0x0902	Ascii_2  
 0x0903	Ascii_3  
 0x0904	Ascii_4  
 0x0905	Ascii_5  
 0x0906	Ascii_6  
 0x0907	Ascii_7  
 0x0908	Ascii_8  
 0x0909	Ascii_9  
 0x090a	Hex_0  
 0x090b	Hex_1  
 0x090c	Hex_2  
 0x090d	Hex_3  
 0x090e	Hex_4  
 0x090f	Hex_5  
 0x0910	Hex_6  
 0x0911	Hex_7  
 0x0912	Hex_8  
 0x0913	Hex_9  
 0x0914	Hex_A  
 0x0915	Hex_B  
 0x0916	Hex_C  
 0x0917	Hex_D  
 0x0918	Hex_E  
 0x0919	Hex_F  
 0x0a00	Shift_Lock  
 0x0a01	AltGr_Lock  
 0x0a02	Control_Lock  
 0x0a03	Alt_Lock  
 0x0a04	ShiftL_Lock  
 0x0a05	ShiftR_Lock  
 0x0a06	CtrlL_Lock  
 0x0a07	CtrlR_Lock  
 0x0a08	CapsShift_Lock  
 0x0c00	SShift  
 0x0c01	SAltGr  
 0x0c02	SControl  
 0x0c03	SAlt  
 0x0c04	SShiftL  
 0x0c05	SShiftR  
 0x0c06	SCtrlL  
 0x0c07	SCtrlR  
 0x0c08	SCapsShift  
 0x0e00	Brl_blank  
 0x0e01	Brl_dot1  
 0x0e02	Brl_dot2  
 0x0e03	Brl_dot3  
 0x0e04	Brl_dot4  
 0x0e05	Brl_dot5  
 0x0e06	Brl_dot6  
 0x0e07	Brl_dot7  
 0x0e08	Brl_dot8  
 0x0e09	Brl_dot9  
 0x0e0a	Brl_dot10  

### Synonyms

 Control_h       for BackSpace  
 Control_i       for Tab  
 Control_j       for Linefeed  
 Home            for Find  
 End             for Select  
 PageUp          for Prior  
 PageDown        for Next  
 multiplication  for multiply  
 pound           for sterling  
 pilcrow         for paragraph  
 Oslash          for Ooblique  
 Shift_L         for ShiftL  
 Shift_R         for ShiftR  
 Control_L       for CtrlL  
 Control_R       for CtrlR  
 AltL            for Alt  
 AltR            for AltGr  
 Alt_L           for Alt  
 Alt_R           for AltGr  
 AltGr_L         for Alt  
 AltGr_R         for AltGr  
 AltLLock        for Alt_Lock  
 AltRLock        for AltGr_Lock  
 SCtrl           for SControl  
 Spawn_Console   for KeyboardSignal  
 Uncaps_Shift    for CapsShift  
 lambda          for lamda  
 Lambda          for Lamda  
 xi              for ksi  
 Xi              for Ksi  
 chi             for khi  
 Chi             for Khi  
 tilde           for asciitilde  
 circumflex      for asciicircum  
 dead_ogonek     for dead_cedilla  
 dead_caron      for dead_circumflex  
 dead_breve      for dead_tilde  
 dead_doubleacute for dead_tilde  
 Idotabove       for Iabovedot  
 dotlessi        for idotless  
 no-break_space  for nobreakspace  
 paragraph_sign  for section  
 soft_hyphen     for hyphen  
 bielorussian_cyrillic_capital_letter_i for ukrainian_cyrillic_capital_letter_i  
 cyrillic_capital_letter_kha for cyrillic_capital_letter_ha  
 cyrillic_capital_letter_ge for cyrillic_capital_letter_ghe  
 cyrillic_capital_letter_ia for cyrillic_capital_letter_ya  
 cyrillic_capital_letter_iu for cyrillic_capital_letter_yu  
 cyrillic_capital_letter_yeri for cyrillic_capital_letter_yeru  
 cyrillic_capital_letter_reversed_e for cyrillic_capital_letter_e  
 cyrillic_capital_letter_ii for cyrillic_capital_letter_i  
 cyrillic_capital_letter_short_ii for cyrillic_capital_letter_short_i  
 bielorussian_cyrillic_small_letter_i for ukrainian_cyrillic_small_letter_i  
 cyrillic_small_letter_kha for cyrillic_small_letter_ha  
 cyrillic_small_letter_ge for cyrillic_small_letter_ghe  
 cyrillic_small_letter_ia for cyrillic_small_letter_ya  
 cyrillic_small_letter_iu for cyrillic_small_letter_yu  
 cyrillic_small_letter_yeri for cyrillic_small_letter_yeru  
 cyrillic_small_letter_reversed_e for cyrillic_small_letter_e  
 cyrillic_small_letter_ii for cyrillic_small_letter_i  
 cyrillic_small_letter_short_ii for cyrillic_small_letter_short_i  
 rightanglequote for guillemetright  
