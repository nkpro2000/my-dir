# shellcheck shell=bash
# rsync -a --delete rsync://mirrors.mit.edu/CTAN/info ./info-archive

wget 'http://mirrors.ctan.org/info/symbols/math.zip'
wget 'http://mirrors.ctan.org/info/symbols/comprehensive.zip'
wget 'http://mirrors.ctan.org/info/symbols/compact.zip'
wget 'http://mirrors.ctan.org/info/symbols/blackboard.zip'
wget 'http://mirrors.ctan.org/info/symbols/text'

# rsync -a --delete --exclude=.svn tug.org::tldevsrc/Build/source ./texlive-svn #https://www.tug.org/texlive/svn/
wget 'http://mirrors.ctan.org/systems/texlive/Source/texlive-20230311-source.tar.xz'
git clone https://github.com/latex3/latex3.git

### Some snippets
## ~/nk/Dev/tex/live/curr/texmf-dist/tex/latex/base/latex.ltx
# \@onlypreamble\set@mathaccent
# \def\DeclareMathSymbol#1#2#3#4{%
#   \expandafter\in@\csname sym#3\expandafter\endcsname
#      \expandafter{\group@list}%
#   \ifin@
#     \begingroup
#       \count\z@=#4\relax
#       \count\tw@\count\z@
#       \divide\count\z@\sixt@@n
#       \count@\count\z@
#       \multiply\count@\sixt@@n
#       \advance\count\tw@-\count@
#       \if\relax\noexpand#1% is command?
#         \edef\reserved@b{\expandafter\noexpand
#                          \csname\expandafter\@gobble\string#1\space\endcsname}%
#         \edef\reserved@a
#           {\noexpand\in@{\expandafter\@gobble\string\mathchar}%
#                         {\meaning#1\expandafter\meaning\reserved@b}}%
#         \reserved@a
#         \global\expandafter\let\reserved@b\@undefined
#         \ifin@
#           \expandafter\set@mathsymbol
#              \csname sym#3\endcsname#1#2%
#              {\hexnumber@{\count\z@}\hexnumber@{\count\tw@}}%
#           \@font@info{Redeclaring math symbol \string#1}%
#         \else
#           \expandafter\ifx
#             \csname\expandafter\@gobble\string#1\endcsname
#             \relax
#             \expandafter\set@mathsymbol
#                \csname sym#3\endcsname#1#2%
#                {\hexnumber@{\count\z@}\hexnumber@{\count\tw@}}%
#           \else
#             \@latex@error{Command `\string#1' already defined}\@eha
#           \fi
#         \fi
#       \else
#         \expandafter\set@mathchar
#           \csname sym#3\endcsname#1#2
#           {\hexnumber@{\count\z@}\hexnumber@{\count\tw@}}%
#       \fi
#     \endgroup
#   \else
#     \@latex@error{Symbol font `#3' is not defined}\@eha
#   \fi
# }
# \@onlypreamble\DeclareMathSymbol
# \def\set@mathchar#1#2#3#4{%
#   \global\mathcode`#2="\mathchar@type#3\hexnumber@#1#4\relax}
# \@onlypreamble\set@mathchar
# \def\set@mathsymbol#1#2#3#4{%
#   \global\mathchardef#2"\mathchar@type#3\hexnumber@#1#4\relax}
# \@onlypreamble\set@mathsymbol
# \def\DeclareMathDelimiter#1{%
#   \if\relax\noexpand#1%
#     \expandafter\@DeclareMathDelimiter
#   \else
#     \expandafter\@xxDeclareMathDelimiter
#   \fi
#   #1}
# \@onlypreamble\DeclareMathDelimiter
# \def\@xxDeclareMathDelimiter#1#2#3#4{%
#    \begingroup
#     \let\mathalpha\mathord
#     \ifnum7=\mathchar@type{#2}%
#       \endgroup
#       \expandafter\@firstofone
#     \else
#       \endgroup
#       \DeclareMathSymbol#1{#2}{#3}{#4}%
#       \expandafter\@firstoftwo
#     \fi
#     {\@xDeclareMathDelimiter#1}{#2}{#3}{#4}}
#
## ~/nk/Dev/tex/live/2023/texmf-dist/tex/latex/base/fontmath.ltx
# \DeclareMathSymbol{\alpha}{\mathord}{letters}{"0B}
# \DeclareMathSymbol{\beta}{\mathord}{letters}{"0C}
# \DeclareMathSymbol{\gamma}{\mathord}{letters}{"0D}
# \DeclareMathSymbol{\delta}{\mathord}{letters}{"0E}
# \DeclareMathSymbol{\epsilon}{\mathord}{letters}{"0F}
# \DeclareMathSymbol{\zeta}{\mathord}{letters}{"10}
# \DeclareMathSymbol{\eta}{\mathord}{letters}{"11}
# \DeclareMathSymbol{\theta}{\mathord}{letters}{"12}
# \DeclareMathSymbol{\iota}{\mathord}{letters}{"13}
# \DeclareMathSymbol{\kappa}{\mathord}{letters}{"14}
# \DeclareMathSymbol{\lambda}{\mathord}{letters}{"15}
# \DeclareMathSymbol{\mu}{\mathord}{letters}{"16}
# \DeclareMathSymbol{\nu}{\mathord}{letters}{"17}
# \DeclareMathSymbol{\xi}{\mathord}{letters}{"18}
# \DeclareMathSymbol{\pi}{\mathord}{letters}{"19}
# \DeclareMathSymbol{\rho}{\mathord}{letters}{"1A}
# \DeclareMathSymbol{\sigma}{\mathord}{letters}{"1B}
# \DeclareMathSymbol{\tau}{\mathord}{letters}{"1C}
# \DeclareMathSymbol{\upsilon}{\mathord}{letters}{"1D}
# \DeclareMathSymbol{\phi}{\mathord}{letters}{"1E}
# \DeclareMathSymbol{\chi}{\mathord}{letters}{"1F}
# \DeclareMathSymbol{\psi}{\mathord}{letters}{"20}
# \DeclareMathSymbol{\omega}{\mathord}{letters}{"21}
# \DeclareMathSymbol{\varepsilon}{\mathord}{letters}{"22}
# \DeclareMathSymbol{\vartheta}{\mathord}{letters}{"23}
# \DeclareMathSymbol{\varpi}{\mathord}{letters}{"24}
# \DeclareMathSymbol{\varrho}{\mathord}{letters}{"25}
# \DeclareMathSymbol{\varsigma}{\mathord}{letters}{"26}
# \DeclareMathSymbol{\varphi}{\mathord}{letters}{"27}
# \DeclareMathSymbol{\Gamma}{\mathalpha}{operators}{"00}
# \DeclareMathSymbol{\Delta}{\mathalpha}{operators}{"01}
# \DeclareMathSymbol{\Theta}{\mathalpha}{operators}{"02}
# \DeclareMathSymbol{\Lambda}{\mathalpha}{operators}{"03}
# \DeclareMathSymbol{\Xi}{\mathalpha}{operators}{"04}
# \DeclareMathSymbol{\Pi}{\mathalpha}{operators}{"05}
# \DeclareMathSymbol{\Sigma}{\mathalpha}{operators}{"06}
# \DeclareMathSymbol{\Upsilon}{\mathalpha}{operators}{"07}
# \DeclareMathSymbol{\Phi}{\mathalpha}{operators}{"08}
# \DeclareMathSymbol{\Psi}{\mathalpha}{operators}{"09}
# \DeclareMathSymbol{\Omega}{\mathalpha}{operators}{"0A}
# \DeclareMathSymbol{\aleph}{\mathord}{symbols}{"40}
# \DeclareMathSymbol{\imath}{\mathord}{letters}{"7B}
# \DeclareMathSymbol{\jmath}{\mathord}{letters}{"7C}
# \DeclareMathSymbol{\ell}{\mathord}{letters}{"60}
# \DeclareMathSymbol{\wp}{\mathord}{letters}{"7D}
# \DeclareMathSymbol{\Re}{\mathord}{symbols}{"3C}
# \DeclareMathSymbol{\Im}{\mathord}{symbols}{"3D}
# \DeclareMathSymbol{\partial}{\mathord}{letters}{"40}
# \DeclareMathSymbol{\infty}{\mathord}{symbols}{"31}
# \DeclareMathSymbol{\prime}{\mathord}{symbols}{"30}
# \DeclareMathSymbol{\emptyset}{\mathord}{symbols}{"3B}
# \DeclareMathSymbol{\nabla}{\mathord}{symbols}{"72}
# \DeclareMathSymbol{\top}{\mathord}{symbols}{"3E}
# \DeclareMathSymbol{\bot}{\mathord}{symbols}{"3F}
# \DeclareMathSymbol{\triangle}{\mathord}{symbols}{"34}
# \DeclareMathSymbol{\forall}{\mathord}{symbols}{"38}
# \DeclareMathSymbol{\exists}{\mathord}{symbols}{"39}
# \DeclareMathSymbol{\neg}{\mathord}{symbols}{"3A}
# \DeclareMathSymbol{\lnot}{\mathord}{symbols}{"3A}
# \DeclareMathSymbol{\flat}{\mathord}{letters}{"5B}
# \DeclareMathSymbol{\natural}{\mathord}{letters}{"5C}
# \DeclareMathSymbol{\sharp}{\mathord}{letters}{"5D}
# \DeclareMathSymbol{\clubsuit}{\mathord}{symbols}{"7C}
# \DeclareMathSymbol{\diamondsuit}{\mathord}{symbols}{"7D}
# \DeclareMathSymbol{\heartsuit}{\mathord}{symbols}{"7E}
# \DeclareMathSymbol{\spadesuit}{\mathord}{symbols}{"7F}
## Info from ChatGPT https://chat.openai.com/share/2bf2c539-df0d-454f-8043-3f48b33ee72b
