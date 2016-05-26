#!/usr/bin/env python

"""update ClamAV signatures"""

# File: ratom/clamav.py
# Version: 1.1.0
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update ClamAV signatures"""
    return runp('which freshclam', True)[0] == 0

def main(argv=None, cfg=None):
    """update ClamAV signatures"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('clamav: started')
    if not check():
        log.info('clamav: failed check')
        return
    section('ClamAV signatures', 'freshclam', dryrun=cfg['dryrun'])
    log.info('clamav: finished')

if __name__ == '__main__':
    main()

