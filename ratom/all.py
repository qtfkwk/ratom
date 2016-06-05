#!/usr/bin/env python

"""imports and runs all plugins"""

# File: ratom/all.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import aptget
import cask
import clamav
import cpanm
import freebsd
import gem
import git
import homebrew
import macosx
import macosx_microsoft
import msf
import npm
import perlbrew
import pip
import pyenv
import rbenv
import yum

plugins = dict(
    aptget=aptget,
    cask=cask,
    clamav=clamav,
    cpanm=cpanm,
    freebsd=freebsd,
    gem=gem,
    git=git,
    homebrew=homebrew,
    macosx=macosx,
    macosx_microsoft=macosx_microsoft,
    msf=msf,
    npm=npm,
    perlbrew=perlbrew,
    pip=pip,
    pyenv=pyenv,
    rbenv=rbenv,
    yum=yum,
)

def main(argv=None, cfg=None):
    """runs all plugins"""
    cfg = init(argv, cfg)
    info('all: started')
    for m in cfg['plugins']:
        if not m in plugins:
            e = 'Unknown plugin "%s"!' % m
            error(e)
            raise UnknownPlugin(e)
        plugins[m].main(cfg=cfg)
    info('all: finished')

if __name__ == '__main__':
    main()

