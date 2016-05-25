#!/usr/bin/env python

"""update Homebrew packages"""

# File: ratom/homebrew.py
# Version: 1.0.2
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

def check():
    """check if can update Homebrew packages"""
    return runp('which brew', True)[0] == 0

def main(argv=None, cfg=None):
    """update Homebrew packages"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('homebrew: started')
    if not check():
        log.info('homebrew: failed check')
        return
    begin('Homebrew')
    v = runp('pyenv global')[1].strip('\n')
    run([
        'brew update',
        'pyenv global system',
        'brew upgrade --all',
        'pyenv global %s' % v,
        'brew cleanup',
    ], dryrun=cfg['dryrun'])
    end()
    log.info('homebrew: finished')

if __name__ == '__main__':
    main()

