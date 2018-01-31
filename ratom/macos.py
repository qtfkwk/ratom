#!/usr/bin/env python

"""update macOS"""

# File: ratom/macos.py
# Version: 2.2.5
# Date: 2018-01-31
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update macOS"""
    return has('softwareupdate')

def main(argv=None, cfg=None):
    """update macOS"""
    cfg = init(argv, cfg)
    info('macos: started')
    if not check():
        info('macos: failed check')
        return
    section('macOS', 'sudo softwareupdate -ia --verbose', dryrun=cfg['dryrun'])
    info('macos: finished')

if __name__ == '__main__':
    main()

