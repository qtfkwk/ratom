#!/usr/bin/env python

"""update Debian via apt-get"""

# File: ratom/aptget.py
# Version: 3.0.0
# Date: 2018-10-24
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from .common import *

def check():
    """check if can update Debian via apt-get"""
    return has('apt-get')

def main(argv=None, cfg=None):
    """update Debian via apt-get"""
    cfg = init(argv, cfg)
    info('aptget: started')
    if not check():
        info('aptget: failed check')
        return
    c = [
        'sudo apt-get update',
        'sudo apt-get dist-upgrade -y',
        'sudo apt-get autoremove -y',
    ]
    section('apt-get', c, dryrun=cfg['dryrun'])
    info('aptget: finished')

if __name__ == '__main__':
    main()

