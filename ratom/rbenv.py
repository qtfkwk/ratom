#!/usr/bin/env python

"""check for new Ruby versions in rbenv"""

# File: ratom/rbenv.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can check for new Ruby versions in rbenv"""
    return has('rbenv')

def main(argv=None, cfg=None):
    """check for new Ruby versions in rbenv"""
    cfg = init(argv, cfg)
    info('rbenv: started')
    if not check():
        info('rbenv: failed check')
        return
    c = "rbenv install -l |grep '^ *2\.[34]'"
    available = [x.strip() for x in runp(c)[1].split('\n')]
    latest = {x: None for x in ['2.3']}
    for i in latest:
        l = len(i)
        for j in available:
            if j[:l] == i:
                latest[i] = j.strip().strip('\n')
    section_begin('Rbenv', 'Latest: %s\n' % ', '.join(sorted(latest.values())))
    run('rbenv versions')
    section_end()
    info('rbenv: finished')

if __name__ == '__main__':
    main()

