#!/usr/bin/env python

"""check for new Ruby versions in rbenv"""

# File: ratom/rbenv.py
# Version: 1.0.6
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can check for new Ruby versions in rbenv"""
    return runp('which rbenv', True)[0] == 0

def main(argv=None, cfg=None):
    """check for new Ruby versions in rbenv"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('rbenv: started')
    if not check():
        log.info('rbenv: failed check')
        return
    print t.bold_yellow('## Rbenv') + '\n'
    c = "rbenv install -l |grep '^ *2\.[34]'"
    available = [x.strip() for x in runp(c)[1].split('\n')]
    latest = {x: None for x in ['2.3']}
    for i in latest:
        l = len(i)
        for j in available:
            if j[:l] == i:
                latest[i] = j.strip().strip('\n')
    print 'Latest: %s\n' % ', '.join(sorted(latest.values()))
    print '```'
    run('rbenv versions')
    end()
    log.info('rbenv: finished')

if __name__ == '__main__':
    main()

