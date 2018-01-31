#!/usr/bin/env python

"""update global NPM modules"""

# File: ratom/npm.py
# Version: 2.2.5
# Date: 2018-01-31
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update global NPM modules"""
    return has('npm')

def main(argv=None, cfg=None):
    """update global NPM modules"""
    cfg = init(argv, cfg)
    info('npm: started')
    if not check():
        info('npm: failed check')
        return
    section_begin('NPM')
    #if run('npm outdated -g', dryrun=cfg['dryrun'], good=(0, 1)) in (0, []):
    #    run('npm update -g', dryrun=cfg['dryrun'])
    #    run('npm outdated -g', dryrun=cfg['dryrun'], good=1)
    run('npm update -g', dryrun=cfg['dryrun'])
    section_end()
    info('npm: finished')

if __name__ == '__main__':
    main()

