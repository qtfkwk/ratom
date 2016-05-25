#!/usr/bin/env python

"""update Git repositories"""

# File: ratom/git.py
# Version: 1.0.1
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import os

def check(p):
    """check if can update Git repositories"""
    if not os.path.isdir(p):
        return []
    return runp('ls ' + p, True)[1].split('\n')

def main(argv=None, cfg=None):
    """update Git repositories"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('git: started')
    d = '~/.ratom/git'
    p = os.path.expanduser(d)
    repos = check(p)
    if len(repos) < 1:
        log.info('git: failed check')
        return
    print t.bold_yellow('## Git repositories') + '\n'
    for repo in repos:
        if not repo:
            continue
        print t.bold_yellow('### ' + repo) + '\n\n```'
        r = p + '/' + repo.replace(' ', r'\ ')
        if os.path.islink(r):
            run('readlink %s' % r)
        run('git -C %s remote -v' % r)
        run('git -C %s pull' % r, dryrun=cfg['dryrun'])
        print '```\n'
    log.info('git: finished')

if __name__ == '__main__':
    main()

