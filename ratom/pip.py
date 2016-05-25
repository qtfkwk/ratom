#!/usr/bin/env python

"""update Python packages via pip"""

# File: ratom/pip.py
# Version: 1.0.3
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Python packages via pip"""
    return runp('which pip', True)[0] == 0

def main(argv=None, cfg=None):
    """update Python packages via pip"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('pip: started')
    if not check():
        log.info('pip: failed check')
        return
    begin('Python packages')
    run('pip install --upgrade pip', dryrun=cfg['dryrun'])
    packages = map(lambda x: x.split(' ')[0], runp('pip list')[1].split('\n'))
    packages = filter(lambda x: not x in ('', 'pip'), packages)
    for package in packages:
        run('pip install --upgrade %s' % package, dryrun=cfg['dryrun'])
    end()
    log.info('pip: finished')

if __name__ == '__main__':
    main()

