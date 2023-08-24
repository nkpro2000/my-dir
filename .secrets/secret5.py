# To load secret as variables to python script.
# Used like:
"""
>>> import sys, pathlib
>>> sys.path.append(f'{pathlib.Path.home()}/nk/.secrets')
>>> from secret5 import *
"""

import os
import shlex

#TODO better to have secrets in seprate file and secret5.{sh,py} will parse and export them

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
