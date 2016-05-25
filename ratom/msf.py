#!/usr/bin/env python

"""update Metasploit Framework"""

# File: ratom/msf.py
# Version: 1.0.0
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Metasploit Framework"""
    return runp('which msfupdate', True)[0] == 0

def main(argv=None, cfg=None):
    """update Metasploit Framework"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('msf: started')
    if not check():
        log.info('msf: failed check')
        return
    section('Metasploit Framework', 'msfupdate', dryrun=cfg['dryrun'])
    log.info('msf: finished')

if __name__ == '__main__':
    main()

