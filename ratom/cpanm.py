#!/usr/bin/env python

"""update Perl modules via CPANM"""

# File: ratom/cpanm.py
# Version: 1.0.4
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Perl modules via CPANM"""
    if runp('which cpan-outdated', True)[0] != 0:
        return False
    if runp('which cpanm', True)[0] != 0:
        return False
    return True

def main(argv=None, cfg=None):
    """update Perl modules via CPANM"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('cpanm: started')
    if not check():
        log.info('cpanm: failed check')
        return
    begin('Perl modules')
    print t.bold('$ cpan-outdated -p')
    modules = filter(lambda x: x != '', runp('cpan-outdated -p')[1].split('\n'))
    if len(modules) > 0:
        for module in modules:
            print module
        print
        for module in modules:
            run('cpanm %s' % module, dryrun=cfg['dryrun'])
    end()
    log.info('cpanm: finished')

if __name__ == '__main__':
    main()

