#!/usr/bin/env python

"""update Mac OSX"""

# File: ratom/macosx.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Mac OSX"""
    return has('softwareupdate')

def main(argv=None, cfg=None):
    """update Mac OSX"""
    cfg = init(argv, cfg)
    info('macosx: started')
    if not check():
        info('macosx: failed check')
        return
    section('Mac OSX', 'sudo softwareupdate -iav', dryrun=cfg['dryrun'])
    info('macosx: finished')

if __name__ == '__main__':
    main()

