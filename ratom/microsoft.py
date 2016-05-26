#!/usr/bin/env python

"""update Microsoft software on Mac OSX"""

# File: ratom/microsoft.py
# Version: 1.0.5
# Date: 2016-05-26
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
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('microsoft: started')
    if not check():
        log.info('microsoft: failed check')
        return
    c = 'open -W %s' % _f.replace(' ', r'\ ')
    section('Microsoft', c, dryrun=cfg['dryrun'])
    log.info('microsoft: finished')

if __name__ == '__main__':
    main()

