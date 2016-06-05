#!/usr/bin/env python

"""update Perl modules via CPANM"""

# File: ratom/cpanm.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Perl modules via CPANM"""
    if not has('cpan-outdated', 'cpanm'):
        return False
    return True

def main(argv=None, cfg=None):
    """update Perl modules via CPANM"""
    cfg = init(argv, cfg)
    info('cpanm: started')
    if not check():
        info('cpanm: failed check')
        return
    section_begin('Perl modules')
    print t.bold('$ cpan-outdated -p')
    modules = filter(lambda x: x != '', runp('cpan-outdated -p')[1].split('\n'))
    if len(modules) > 0:
        for module in modules:
            print module
        print
        for module in modules:
            run('cpanm %s' % module, dryrun=cfg['dryrun'])
    section_end()
    info('cpanm: finished')

if __name__ == '__main__':
    main()

