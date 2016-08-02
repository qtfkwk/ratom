#!/usr/bin/env python

"""update Cask packages"""

# File: ratom/cask.py
# Version: 2.0.3
# Date: 2016-08-02
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
        runp('brew cask', check=True)
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
    casks = []
    for i in runp('brew cask list')[1].split('\n'):
        if i != '':
            casks.append(i.split(' ')[0])
    info('cask: casks = %s' % casks)
    updates = []
    for cask in casks:
        c = 'brew cask info %s' % cask
        i = runp(c)[1]
        if re.search(r'Not installed', i):
            updates.append(cask)
    info('cask: updates = %s' % updates)
    if len(updates) > 0:
        for cask in updates:
            run('brew cask install %s' % cask, dryrun=cfg['dryrun'])
    run('brew cask cleanup', dryrun=cfg['dryrun'])
    section_end()
    info('cask: finished')

if __name__ == '__main__':
    main()

