#!/usr/bin/env python

"""update ClamAV signatures"""

# File: ratom/clamav.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update ClamAV signatures"""
    return has('freshclam')

def main(argv=None, cfg=None):
    """update ClamAV signatures"""
    cfg = init(argv, cfg)
    info('clamav: started')
    if not check():
        info('clamav: failed check')
        return
    section('ClamAV signatures', 'freshclam', dryrun=cfg['dryrun'])
    info('clamav: finished')

if __name__ == '__main__':
    main()

