#!/usr/bin/env python

"""update Microsoft software on macOS"""

# File: ratom/macos_microsoft.py
# Version: 2.2.5
# Date: 2018-01-31
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

_f = '/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app'

def check():
    """check if can update Microsoft software on macOS"""
    return os.path.isdir(_f)

def main(argv=None, cfg=None):
    """update Microsoft software on macOS"""
    cfg = init(argv, cfg)
    info('macos_microsoft: started')
    if not check():
        info('macos_microsoft: failed check')
        return
    c = 'open -W %s' % _f.replace(' ', r'\ ')
    section('Microsoft AutoUpdate (macOS)', c, dryrun=cfg['dryrun'])
    info('macos_microsoft: finished')

if __name__ == '__main__':
    main()

