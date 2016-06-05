#!/usr/bin/env python

"""update Ruby gems"""

# File: ratom/npm.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Ruby gems"""
    return has('gem')

def main(argv=None, cfg=None):
    """update Ruby gems"""
    cfg = init(argv, cfg)
    info('gem: started')
    if not check():
        info('gem: failed check')
        return
    section('Ruby gems', 'gem update', dryrun=cfg['dryrun'])
    info('gem: finished')

if __name__ == '__main__':
    main()

