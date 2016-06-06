#!/usr/bin/env python

"""update Python packages via pip"""

# File: ratom/pip.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Python packages via pip"""
    return has('pip')

def main(argv=None, cfg=None):
    """update Python packages via pip"""
    cfg = init(argv, cfg)
    info('pip: started')
    if not check():
        info('pip: failed check')
        return
    section_begin('Python packages')
    run('pip install --upgrade pip', dryrun=cfg['dryrun'])
    packages = map(lambda x: x.split(' ')[0], runp('pip list')[1].split('\n'))
    packages = filter(lambda x: not x in ('', 'pip'), packages)
    for package in packages:
        run('pip install --upgrade %s' % package, dryrun=cfg['dryrun'])
    section_end()
    info('pip: finished')

if __name__ == '__main__':
    main()

