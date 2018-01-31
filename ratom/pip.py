#!/usr/bin/env python

"""update Python packages via pip"""

# File: ratom/pip.py
# Version: 2.2.5
# Date: 2018-01-31
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
    section_begin('Python packages', backticks=False)
    c = 'pip list --not-required --outdated --format json'
    packages = [package['name'] for package in json.loads(runp(c)[1])]
    packages = filter(lambda x: not x in cfg['pip_ignore'], packages)
    if len(packages) > 0:
        sys.stdout.write('```')
        for package in packages:
            run('pip install --upgrade %s' % package, dryrun=cfg['dryrun'])
        sys.stdout.write('```')
    else:
        sys.stdout.write('Up-to-date!')
    section_end(backticks=False)
    info('pip: finished')

if __name__ == '__main__':
    main()

