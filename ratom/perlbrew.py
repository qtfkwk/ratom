#!/usr/bin/env python

"""update Perlbrew and check for updated Perl"""

# File: ratom/perlbrew.py
# Version: 1.0.2
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Perlbrew"""
    return runp('which perlbrew', True)[0] == 0

def main(argv=None, cfg=None):
    """update Perlbrew and check for updated Perl"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('perlbrew: started')
    if not check():
        log.info('perlbrew: failed check')
        return
    section('Perlbrew', [
        'perlbrew self-upgrade',
        'perlbrew list',
        'perlbrew available',
    ], dryrun=cfg['dryrun'])
    log.info('perlbrew: finished')

if __name__ == '__main__':
    main()

