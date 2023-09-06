# to install texlive (https://tug.org/texlive/doc/texlive-en/texlive-en.html)
# using install-tl https://tug.org/texlive/quickinstall.html (https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz)
# https://tug.org/texlive/doc/install-tl.html

# shellcheck shell=bash

. "$HOME/nk/Dev/tex/bin/teks" echo 'I> teks envs set'

perl "$HOME/nk/Dev/tex/live/.install-tl/install-tl-"*"/install-tl" -V -gui \
    -repository 'http://mirror.math.princeton.edu/pub/CTAN/systems/texlive/tlnet' \
    "$@"
#    -repository 'https://mirror.niser.ac.in/ctan/systems/texlive/tlnet'
#    -repository 'https://mirrors.mit.edu/CTAN/systems/texlive/tlnet'
##               https://ctan.org/mirrors?lang=en
#    -select-repository
#    -scheme scheme-bookpub

# https://tug.org/texlive/tlmgr.html
