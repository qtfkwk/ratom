#!/usr/bin/env python

"""update Ruby gems"""

# File: ratom/npm.py
# Version: 1.0.4
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Ruby gems"""
    return runp('which gem', True)[0] == 0

def main(argv=None, cfg=None):
    """update Ruby gems"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('gem: started')
    if not check():
        log.info('gem: failed check')
        return
    section('Ruby gems', 'gem update', dryrun=cfg['dryrun'])
    log.info('gem: finished')

if __name__ == '__main__':
    main()

