"""
>>> import sys, pathlib
>>> sys.path.append(f'{pathlib.Path.home()}/nk/.53c2375')
>>> from secret5 import *
"""

import os
import shlex


dirname = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dirname, 'secret5.sh'), 'r') as f:
    envs = f.read().replace('export ', '')

secrets = dict()
for token in shlex.split(envs):
    parts = token.split('=', 1)
    if len(parts) == 2:
        secrets[parts[0]] = parts[1]

globals().update(secrets)
__all__ = list(secrets.keys())
