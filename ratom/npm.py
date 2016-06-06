#!/usr/bin/env python

"""update global NPM modules"""

# File: ratom/npm.py
# Version: 2.0.1
# Date: 2016-06-06
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
    run('npm outdated -g')
    run('npm update -g', dryrun=cfg['dryrun'])
    run('npm outdated -g', dryrun=cfg['dryrun'])
    section_end()
    info('npm: finished')

if __name__ == '__main__':
    main()

