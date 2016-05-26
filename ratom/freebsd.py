#!/usr/bin/env python

"""update FreeBSD"""

# File: ratom/freebsd.py
# Version: 1.0.5
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import re

def check():
    """check if can update FreeBSD"""
    r = set()
    if runp('which freebsd-update', True)[0] == 0:
        r.add('freebsd-update')
    if runp('which portsnap', True)[0] == 0:
        r.add('portsnap')
    if runp('which pkg', True)[0] == 0:
        r.add('pkg')
    if runp('which ckver', True) == 0:
        r.add('ckver')
    return r

def main(argv=None, cfg=None):
    """update FreeBSD"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('freebsd: started')
    which = check()
    if len(which) < 1:
        log.info('freebsd: failed check')
        return
    begin('FreeBSD')
    if 'freebsd-update' in which:
        print t.bold('$ freebsd-update fetch')
        needed = runp('freebsd-update fetch')[1]
        print needed
        print
        if not re.search(r'No updates needed to update system', needed):
            run('freebsd-update install', dryrun=cfg['dryrun'])
    if 'portsnap' in which:
        run('portsnap fetch update', dryrun=cfg['dryrun'])
    if 'pkg' in which:
        run([
            'pkg update',
            'pkg upgrade -y',
            'pkg autoremove -y',
        ], dryrun=cfg['dryrun'])
    if 'ckver' in which:
        run('ckver', dryrun=cfg['dryrun'])
    end()
    log.info('freebsd: finished')

if __name__ == '__main__':
    main()

