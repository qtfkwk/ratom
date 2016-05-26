#!/usr/bin/env python

"""update Red Hat via yum"""

# File: ratom/yum.py
# Version: 1.0.5
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import logging

def check():
    """check if can update Red Hat via yum"""
    return runp('which yum', True)[0] == 0

def main(argv=None, cfg=None):
    """update Red Hat via yum"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('yum: started')
    if not check():
        log.info('yum: failed check')
        return
    section('yum', 'sudo yum update -y', dryrun=cfg['dryrun'])
    log.info('yum: finished')

if __name__ == '__main__':
    main()

