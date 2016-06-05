#!/usr/bin/env python

"""update Perlbrew and check for updated Perl"""

# File: ratom/perlbrew.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Perlbrew"""
    return has('perlbrew')

def main(argv=None, cfg=None):
    """update Perlbrew and check for updated Perl"""
    cfg = init(argv, cfg)
    info('perlbrew: started')
    if not check():
        info('perlbrew: failed check')
        return
    section('Perlbrew', [
        'perlbrew self-upgrade',
        'perlbrew list',
        'perlbrew available',
    ], dryrun=cfg['dryrun'])
    info('perlbrew: finished')

if __name__ == '__main__':
    main()

