#!/usr/bin/env python

"""update Red Hat via yum"""

# File: ratom/yum.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Red Hat via yum"""
    return has('yum')

def main(argv=None, cfg=None):
    """update Red Hat via yum"""
    cfg = init(argv, cfg)
    info('yum: started')
    if not check():
        info('yum: failed check')
        return
    section('yum', 'sudo yum update -y', dryrun=cfg['dryrun'])
    info('yum: finished')

if __name__ == '__main__':
    main()

