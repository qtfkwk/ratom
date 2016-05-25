#!/usr/bin/env python

"""imports and runs all plugins"""

# File: ratom/all.py
# Version: 1.0.3
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import cask
import clamav
import cpanm
import freebsd
import gem
import git
import homebrew
import macosx
import microsoft
import msf
import npm
import perlbrew
import pip
import pyenv
import rbenv

plugins = dict(
    cask=cask,
    clamav=clamav,
    cpanm=cpanm,
    freebsd=freebsd,
    gem=gem,
    git=git,
    homebrew=homebrew,
    macosx=macosx,
    microsoft=microsoft,
    msf=msf,
    npm=npm,
    perlbrew=perlbrew,
    pip=pip,
    pyenv=pyenv,
    rbenv=rbenv,
)

def main(argv=None, cfg=None):
    """runs all plugins"""
    if cfg == None:
        cfg = args(argv)
    log = logging.getLogger('ratom')
    log.info('all: started')
    for m in cfg['plugins']:
        if not m in plugins:
            raise UnknownModule('Unknown plugin "%s"!' % m)
        plugins[m].main(cfg=cfg)
    log.info('all: finished')

if __name__ == '__main__':
    main()

