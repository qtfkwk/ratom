#!/usr/bin/env python

"""check for new Python versions in pyenv"""

# File: ratom/pyenv.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can check for new Python versions in pyenv"""
    return has('pyenv')

def main(argv=None, cfg=None):
    """check for new Python versions in pyenv"""
    cfg = init(argv, cfg)
    info('pyenv: started')
    if not check():
        info('pyenv: failed check')
        return
    available = [x.strip() for x in runp('pyenv install -l')[1].split('\n')]
    latest = {x: None for x in ['2.7', '3.5']}
    for i in latest:
        l = len(i)
        for j in available:
            if j[:l] == i:
                latest[i] = j.strip().strip('\n')
    section_begin('Pyenv', 'Latest: %s\n' % ', '.join(sorted(latest.values())))
    run('pyenv versions')
    section_end()
    info('pyenv: finished')

if __name__ == '__main__':
    main()

