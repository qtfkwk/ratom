#!/usr/bin/env python

"""check for new Python versions in pyenv"""

# File: ratom/pyenv.py
# Version: 1.0.5
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can check for new Python versions in pyenv"""
    return runp('which pyenv', True)[0] == 0

def main(argv=None, cfg=None):
    """check for new Python versions in pyenv"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('pyenv: started')
    if not check():
        log.info('pyenv: failed check')
        return
    print t.bold_yellow('## Pyenv') + '\n'
    available = [x.strip() for x in runp('pyenv install -l')[1].split('\n')]
    latest = {x: None for x in ['2.7', '3.5']}
    for i in latest:
        l = len(i)
        for j in available:
            if j[:l] == i:
                latest[i] = j.strip().strip('\n')
    print 'Latest: %s\n' % ', '.join(sorted(latest.values()))
    print '```'
    run('pyenv versions')
    end()
    log.info('pyenv: finished')

if __name__ == '__main__':
    main()

