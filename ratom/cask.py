#!/usr/bin/env python

"""update Cask packages"""

# File: ratom/cask.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import re

def check():
    """check if can update Cask packages"""
    if not has('brew'):
        return False
    try:
        runp('brew cask', True)
    except:
        return False
    return True

def main(argv=None, cfg=None):
    """update Cask packages"""
    cfg = init(argv, cfg)
    info('cask: started')
    if not check():
        info('cask: failed check')
        return
    section_begin('Cask')
    casks = filter(lambda x: x != '', runp('brew cask list')[1].split('\n'))
    updates = []
    for cask in casks:
        c = 'brew cask info %s' % cask
        i = runp(c)[1]
        if re.search(r'Not installed', i):
            updates.append(cask)
    if len(updates) > 0:
        for cask in updates:
            run('brew cask install %s' % cask, dryrun=cfg['dryrun'])
    run('brew cask cleanup', dryrun=cfg['dryrun'])
    section_end()
    info('cask: finished')

if __name__ == '__main__':
    main()

