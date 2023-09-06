# shellcheck shell=bash
# rsync -a --delete rsync://mirrors.mit.edu/CTAN/info /some/dir

wget 'http://mirrors.ctan.org/info/symbols/math.zip'
wget 'http://mirrors.ctan.org/info/symbols/comprehensive.zip'
wget 'http://mirrors.ctan.org/info/symbols/compact.zip'
wget 'http://mirrors.ctan.org/info/symbols/blackboard.zip'
wget 'http://mirrors.ctan.org/info/symbols/text'
