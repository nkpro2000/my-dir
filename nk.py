import sys; sys.ps1='PY> '
import os
from pprint import pprint as pp
import Crypto.Util.number as U
import numpy as np

class Cls:
    def clear(self):
        if sys.platform.startswith('win'): os.system('cls')
        else: os.system('clear')
    ls = property(clear)
c = Cls()

__all__ = ('pp', 'U', 'c','np','os','sys')

