#!/usr/bin/env python

"""update Git repositories"""

# File: ratom/git.py
# Version: 2.0.0
# Date: 2016-06-05
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
    cfg = init(argv, cfg)
    info('git: started')
    d = '~/.ratom/git'
    p = os.path.expanduser(d)
    repos = check(p)
    if len(repos) < 1:
        info('git: failed check')
        return
    section_begin('Git repositories', backticks=False)
    for repo in repos:
        if not repo:
            continue
        section_begin(repo, prefix='###')
        r = p + '/' + repo
        r = os.path.realpath(r)
        r = r.replace(' ', r'\ ')
        run('git -C %s remote -v' % r)
        run('git -C %s pull' % r, dryrun=cfg['dryrun'])
        section_end()
    info('git: finished')

if __name__ == '__main__':
    main()

