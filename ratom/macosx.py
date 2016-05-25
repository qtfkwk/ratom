#!/usr/bin/env python

"""update Mac OSX"""

# File: ratom/macosx.py
# Version: 1.0.2
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import logging

def check():
    """check if can update Mac OSX"""
    return runp('which softwareupdate', True)[0] == 0

def main(argv=None, cfg=None):
    """update Mac OSX"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('macosx: started')
    if not check():
        log.info('macosx: failed check')
        return
    section('Mac OSX', 'sudo softwareupdate -iav', dryrun=cfg['dryrun'])
    log.info('macosx: finished')

if __name__ == '__main__':
    main()

