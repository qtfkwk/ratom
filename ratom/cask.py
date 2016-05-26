#!/usr/bin/env python

"""update Cask packages"""

# File: ratom/cask.py
# Version: 1.0.5
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import re

def check():
    """check if can update Cask packages"""
    if runp('which brew', True)[0] != 0:
        return False
    try:
        runp('brew cask', True)
    except:
        return False
    return True

def main(argv=None, cfg=None):
    """update Cask packages"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('cask: started')
    if not check():
        log.info('cask: failed check')
        return
    begin('Cask')
    casks = filter(lambda x: x != '', runp('brew cask list')[1].split('\n'))
    updates = []
    for cask in casks:
        c = 'brew cask info %s' % cask
        info = runp(c)[1]
        if re.search(r'Not installed', info):
            updates.append(cask)
    if len(updates) > 0:
        for cask in updates:
            run('brew cask install %s' % cask, dryrun=cfg['dryrun'])
    run('brew cask cleanup', dryrun=cfg['dryrun'])
    end()
    log.info('cask: finished')

if __name__ == '__main__':
    main()

