#!/usr/bin/env python

"""update Homebrew packages"""

# File: ratom/homebrew.py
# Version: 1.0.5
# Date: 2016-05-26
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
    d = cfg['dryrun']
    run('brew update', dryrun=d)
    run('pyenv global system', dryrun=d)
    run('brew upgrade --all', dryrun=d, shell=True)
    run('pyenv global %s' % v, dryrun=d)
    run('brew cleanup', dryrun=d)
    end()
    log.info('homebrew: finished')

if __name__ == '__main__':
    main()

