#!/usr/bin/env python

"""imports and runs all plugins"""

# File: ratom/all.py
# Version: 2.2.5
# Date: 2018-01-31
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from common import *

import aptget
import clamav
import conda
import cpanm
import freebsd
import gem
import geoip
import git
import homebrew
import macos
import macos_microsoft
import msf
import npm
import perlbrew
import pip
import pyenv
import rbenv
import yum

plugins = dict(
    aptget=aptget,
    clamav=clamav,
    conda=conda,
    cpanm=cpanm,
    freebsd=freebsd,
    gem=gem,
    geoip=geoip,
    git=git,
    homebrew=homebrew,
    macos=macos,
    macos_microsoft=macos_microsoft,
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

