#!/usr/bin/env python

"""update Anaconda packages via conda"""

# File: ratom/conda.py
# Version: 2.1.3
# Date: 2017-12-30
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Anaconda packages via conda"""
    return has('conda')

def main(argv=None, cfg=None):
    """update Anaconda packages via conda"""
    cfg = init(argv, cfg)
    info('conda: started')
    if not check():
        info('conda: failed check')
        return
    section_begin('Anaconda packages')
    run('conda update --all', dryrun=cfg['dryrun'])
    section_end()
    info('conda: finished')

if __name__ == '__main__':
    main()

