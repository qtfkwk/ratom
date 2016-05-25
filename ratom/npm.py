#!/usr/bin/env python

"""update global NPM modules"""

# File: ratom/npm.py
# Version: 1.0.1
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update global NPM modules"""
    return runp('which npm', True)[0] == 0

def main(argv=None, cfg=None):
    """update global NPM modules"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('npm: started')
    if not check():
        log.info('npm: failed check')
        return
    begin('NPM')
    run('npm outdated -g')
    run('npm update -g', dryrun=cfg['dryrun'])
    run('npm outdated -g')
    end()
    log.info('npm: finished')

if __name__ == '__main__':
    main()

