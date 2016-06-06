#!/usr/bin/env python

"""update Metasploit Framework"""

# File: ratom/msf.py
# Version: 2.0.1
# Date: 2016-06-06
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Metasploit Framework"""
    return has('msfupdate')

def main(argv=None, cfg=None):
    """update Metasploit Framework"""
    cfg = init(argv, cfg)
    info('msf: started')
    if not check():
        info('msf: failed check')
        return
    section('Metasploit Framework', 'msfupdate', dryrun=cfg['dryrun'])
    info('msf: finished')

if __name__ == '__main__':
    main()

