#!/usr/bin/env python

"""update Homebrew packages"""

# File: ratom/homebrew.py
# Version: 3.0.0
# Date: 2018-10-24
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from .common import *

def check():
    """check if can update Homebrew packages"""
    return has('brew')

import os
def _pyenv(version, dryrun=False):
    """change the pyenv version via environment variable"""
    k = 'PYENV_VERSION'
    r = os.environ[k]
    if dryrun:
        print(t.bold_red('$ export PYENV_VERSION=\'%s\'' % version))
    else:
        print(t.bold('$ export PYENV_VERSION=\'%s\'' % version) + '\n')
        os.environ[k] = version
    return r

def main(argv=None, cfg=None):
    """update Homebrew packages"""
    cfg = init(argv, cfg)
    info('homebrew: started')
    if not check():
        info('homebrew: failed check')
        return
    section_begin('Homebrew')
    v = str(runp('pyenv global')[1]).strip('\n')
    d = cfg['dryrun']
    run('brew update', dryrun=d)
    if has('pyenv'):
        pyenv_version = _pyenv('system', d)
        run('pyenv exec brew upgrade', dryrun=d, shell=True)
        _pyenv(pyenv_version, d)
    else:
        run('brew upgrade', dryrun=d, shell=True)
    run('brew cleanup', dryrun=d)
    section_end()
    info('homebrew: finished')

if __name__ == '__main__':
    main()

