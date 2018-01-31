#!/usr/bin/env python

"""update GeoIP database"""

# File: ratom/geoip.py
# Version: 2.2.5
# Date: 2018-01-31
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update GeoIP database"""
    return has('geoipupdate')

def main(argv=None, cfg=None):
    """update GeoIP database"""
    cfg = init(argv, cfg)
    info('geoip: started')
    if not check():
        info('geoip: failed check')
        return
    section('GeoIP database', 'geoipupdate -v', dryrun=cfg['dryrun'], good=[0, 1])
    info('geoip: finished')

if __name__ == '__main__':
    main()

