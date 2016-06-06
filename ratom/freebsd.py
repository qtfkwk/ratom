#!/usr/bin/env python

"""update FreeBSD"""

# File: ratom/freebsd.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import re

def check():
    """check if can update FreeBSD"""
    return filter(has, [
        'freebsd-update',
        'portsnap',
        'pkg',
    ])

def current():
    if has('freebsd-version'):
        return runp('freebsd-version')[1].split('-')[0]
    else:
        return 'n/a'

def latest():
    return replace([(r'\n', ''), (r'Production:\xa0', ''), (r'\s', '')], \
        fetch('https://www.freebsd.org').find('ul', \
        id='frontreleaseslist').find('li').text).split(',')[0]

def ckver():
    running = current()
    available = latest()
    r = 'Running: %s, Available: %s\n' % (running, available)
    if running != available:
        r += '\nUpgrade via:\n\n```\n'
        r += 'freebsd-update upgrade -r %s-RELEASE\n' % available
        r += 'freebsd-update install\n'
        r += 'shutdown -r now\n'
        r += 'freebsd-update install\n'
        r += 'freebsd-update install\n'
        r += 'shutdown -r now\n'
        r += '```\n\n'
    return r

def main(argv=None, cfg=None):
    """update FreeBSD"""
    cfg = init(argv, cfg)
    info('freebsd: started')
    which = check()
    if len(which) < 1:
        info('freebsd: failed check')
        return
    section_begin('FreeBSD', ckver())
    d = cfg['dryrun']
    if 'freebsd-update' in which:
        needed = runp('freebsd-update fetch', dryrun=d, verbose=True)[1]
        if not (d or re.search(r'No updates needed to update system', needed)):
            run('freebsd-update install', dryrun=d)
    if 'portsnap' in which:
        run('portsnap fetch update', dryrun=cfg['dryrun'])
    if 'pkg' in which:
        run([
            'pkg update',
            'pkg upgrade -y',
            'pkg autoremove -y',
        ], dryrun=cfg['dryrun'])
    section_end()
    info('freebsd: finished')

if __name__ == '__main__':
    main()

