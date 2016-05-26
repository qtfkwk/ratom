#!/usr/bin/env python

"""update Debian via apt-get"""

# File: ratom/aptget.py
# Version: 1.0.7
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import logging

def check():
    """check if can update Debian via apt-get"""
    return runp('which apt-get', True)[0] == 0

def main(argv=None, cfg=None):
    """update Debian via apt-get"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('aptget: started')
    if not check():
        log.info('aptget: failed check')
        return
    c = [
        'sudo apt-get update',
        'sudo apt-get dist-upgrade -y',
        'sudo apt-get autoremove -y',
    ]
    section('apt-get', c, dryrun=cfg['dryrun'])
    log.info('aptget: finished')

if __name__ == '__main__':
    main()

