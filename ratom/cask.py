#!/usr/bin/env python

"""update Cask packages"""

# File: ratom/cask.py
# Version: 2.0.5
# Date: 2016-08-05
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
    section_begin('Cask', backticks=False)
    section_begin('Installed', prefix='###')
    casks = []
    for i in runp('brew cask list', verbose=True)[1].split('\n'):
        if i != '':
            casks.append(i.split(' ')[0])
    info('cask: casks = %s' % casks)
    section_end()
    section_begin('Check for updates', prefix='###')
    updates = []
    for cask in casks:
        c = 'brew cask info %s' % cask
        i = runp(c, verbose=True)[1]
        if re.search(r'Not installed', i):
            updates.append(cask)
    info('cask: updates = %s' % updates)
    section_end()
    if len(updates) > 0:
        print t.bold('The following casks have updates: %s.' % \
            ', '.join(updates)) + '\n'
        section_begin('Update')
        for cask in updates:
            run('brew cask install %s' % cask, dryrun=cfg['dryrun'])
        section_end()
    else:
        print t.bold_green('All casks are up-to-date.') + '\n'
    section_begin('Cleanup', prefix='###')
    run('brew cask cleanup', dryrun=cfg['dryrun'])
    section_end()
    info('cask: finished')

if __name__ == '__main__':
    main()

