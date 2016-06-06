#!/usr/bin/env python

"""update Microsoft software on Mac OSX"""

# File: ratom/macosx_microsoft.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

_f = '/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app'

def check():
    """check if can update Microsoft software on Mac OSX"""
    return os.path.isdir(_f)

def main(argv=None, cfg=None):
    """update Microsoft software on Mac OSX"""
    cfg = init(argv, cfg)
    info('macosx_microsoft: started')
    if not check():
        info('macosx_microsoft: failed check')
        return
    c = 'open -W %s' % _f.replace(' ', r'\ ')
    section('Microsoft AutoUpdate (Mac OSX)', c, dryrun=cfg['dryrun'])
    info('macosx_microsoft: finished')

if __name__ == '__main__':
    main()

