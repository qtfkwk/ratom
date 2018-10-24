#!/usr/bin/env python

"""imports and runs all plugins"""

# File: ratom/all.py
# Version: 3.0.0
# Date: 2018-10-24
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

from .common import *

from . import aptget
from . import clamav
from . import conda
from . import cpanm
from . import freebsd
from . import gem
from . import geoip
from . import git
from . import homebrew
from . import macos
from . import macos_microsoft
from . import msf
from . import npm
from . import perlbrew
from . import pip
from . import pyenv
from . import rbenv
from . import yum

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

