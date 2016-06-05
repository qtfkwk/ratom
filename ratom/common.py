"""Common things shared across RATOM"""

# File: ratom/common.py
# Version: 2.0.0
# Date: 2016-06-05
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

# Variables

__version__ = '2.0.0'
directory = '~/.ratom'
conf = directory + '/config.json'
defaults = dict(
    log=directory + '/ratom.log',
    plugins=[
        'macosx',
        'freebsd',
        'aptget',
        'yum',
        'clamav',
        'homebrew',
        'cask',
        'perlbrew',
        'cpanm',
        'pyenv',
        'pip',
        'rbenv',
        'gem',
        'npm',
        'msf',
        'git',
        'macosx_microsoft',
    ],
)
log = None

# Standard modules

import argparse
import copy
import json
import logging
import os
import re
import shlex
import subprocess
import sys

# unbuffered stdout
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# better json.dumps
def json_dumps(obj):
    r = json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')) + '\n'
    return r

# External modules

import blessings
import bs4
import kron
import requests

t = blessings.Terminal()

# Functions

def error(msg):
    """print error message to log if we are logging"""
    if log:
        log.error(msg)

def fetch(uri, params=None, soup=True):
    """fetch data from a web URI via requests and return a BeautifulSoup object
    or the data if soup is False"""
    r = requests.get(uri, params)
    if r.status_code != requests.codes.ok:
        raise Exception("Couldn't get \"%s\"! Error: \"%s\"!" \
            % (r.url, r.status_code))
    return bs4.BeautifulSoup(r.text, 'lxml') if soup else r.text

def has(*commands):
    """test if command(s) are in PATH"""
    r = True
    for c in commands:
        if runp('which ' + c, True)[0] != 0:
            r = False
            break
    return r

def header(r, c, cfg, show_config=False):
    """print the header

    * ``r``: running configuration dictionary
    * ``c``: configuration file path
    * ``cfg``: configuration dictionary from the configuration file
    * ``show_config``: shows full configuration details if true
    """
    print t.bold_green('# Rage Against The Outdated Machine, v' + __version__) \
        + '\n'
    print kron.timestamp().str(fmt='national') + '\n'
    if r['dryrun']:
        print t.bold_on_red('**THIS IS A DRY RUN!**') + '\n'
    if show_config:
        section_begin('Configuration', backticks=False)
        section_begin('Command', backticks=False, prefix='###')
        print '``%s``\n' % ' '.join(sys.argv)
        section_begin('File', backticks=False, prefix='###')
        print '``' + c + '``\n'
        print '```\n' + json_dumps(cfg) + '```\n'
        section_begin('Running', prefix='###')
        print json_dumps(r).strip('\n')
        section_end()

def info(msg):
    """print informational message to log if we are logging"""
    if log:
        log.info(msg)

def init(argv=None, cfg=None):
    """process the arguments and configuration file, set up
    logging, and print the header

    * ``argv``: passed to ``parse_args`` method of
      ``argparse.ArgumentParser`` instance; uses ``sys.argv`` if None
    * ``cfg``: avoids rerunning if ``cfg`` is already defined
    """

    if cfg != None:
        return cfg

    # process args
    p = argparse.ArgumentParser()
    g = p.add_argument_group('ratom options')
    g.add_argument('-n', action='store_true',
        help='Dry run; don\'t actually update anything')
    g.add_argument('-c', metavar='PATH',
        help='Use alternate configuration file; default: ' + conf)
    g.add_argument('-l', metavar='PATH',
        help='Log to PATH; default: ' + defaults['log'])
    g.add_argument('--show-config', action='store_true',
        help='Show full configuration details')
    g.add_argument('plugin', nargs='*',
        help='Specific plugin(s) to run in the specified order; ' + \
        'default: "' + ' '.join(defaults['plugins']) + '"; ' + \
        'ignored if running a plugin directly')
    a = p.parse_args(argv)

    # load/save config file
    d = os.path.expanduser(directory)
    if not os.path.isdir(d):
        os.makedirs(d)
    c = os.path.expanduser(conf)
    if os.path.isfile(c):
        h = open(c, 'rb')
        cfg = json.load(h)
        h.close()
    else:
        cfg = copy.deepcopy(defaults)
        h = open(c, 'wb')
        h.write(json_dumps(cfg) + '\n')
        h.close()
    r = copy.deepcopy(cfg)

    # args override config file
    if a.c != None:
        c = os.path.expanduser(a.c)
        h = open(c, 'rb')
        cfg = json.load(h)
        r = copy.deepcopy(cfg)
        h.close()
    if a.l != None:
        r['log'] = a.l
    r['log'] = os.path.expanduser(r['log'])
    r['dryrun'] = a.n
    if len(a.plugin) > 0:
        r['plugins'] = a.plugin

    # set up logging
    logging.basicConfig(filename=r['log'], level=logging.INFO, \
        format='%(asctime)s -- %(message)s', \
        datefmt='%Y-%m-%d %H:%M:%S %Z')
    global log
    log = logging.getLogger('ratom')
    info('command: `%s`' % ' '.join(sys.argv))
    info('arguments: %s' % a)
    info('configuration from %s: %s' % (c, cfg))
    info('running configuration: %s' % r)
    if r['dryrun']:
        info('THIS IS A DRY RUN!')

    # print the header
    header(r, c, cfg, a.show_config)

    return r

def replace(replacements, s):
    """make all replacements in a string"""
    for r in replacements:
        s = re.sub(r[0], r[1], s)
    return s

def run(c, prompt='$ ', dryrun=False, shell=False):
    """print and run one or more commands

    * ``c``: command or list of commands
    * ``prompt``: prompt to display when printing the command
    * ``dryrun``: just prints the command if true
    * ``shell``: passed to ``run_``
    """
    if not isinstance(c, list):
        c = [c]
    for i in c:
        info('running `%s`' % i)
        if dryrun:
            print t.bold_red(prompt + i)
        else:
            print t.bold(prompt + i)
            run_(i, shell)
            print

def run_(c, shell=False):
    """just run a command

    * ``c``: command
    * ``shell``: run via shell if true; avoid when possible, but necessary for
      things like ``*`` expansion
    """
    if shell:
        p = subprocess.Popen(c, shell=True)
    else:
        p = subprocess.Popen(shlex.split(c))
    r = p.wait()
    if r != 0:
        e = 'Command "%s" exited with %d!' % (c, r)
        error(e)
        raise CommandFailed(e)
    return r

def runp(c, check=False, verbose=False):
    """run a command and return the exit code, stdout and stderr back
    to the caller

    * ``c``: command
    * ``check``: don't raise an exception if true; for use only by ``check``
      functions
    * ``verbose``: print command and output if true
    """
    if verbose:
        print t.bold('$ ' + c)
    info('running `%s`' % c)
    pipe = subprocess.PIPE
    p = subprocess.Popen(shlex.split(c), stdout=pipe, stderr=pipe)
    (out, err) = p.communicate()
    r = p.wait()
    if verbose:
        print err
        print out
    if r != 0 and not check:
        e = 'Intermediate command "%s" exited with %d!' % (c, r)
        error(e)
        raise IntermediateCommandFailed(e)
    return (r, out, err)

def section(n, c, dryrun=False):
    """shorthand for a simple section

    * ``n``: name
    * ``c``: command or list of commands
    * ``dryrun``: passed to ``run`` function
    """
    section_begin(n)
    run(c, dryrun=dryrun)
    section_end()

def section_begin(m, a='', backticks=True, prefix='##'):
    """begin a section in the standard way

    * ``m``: header text
    * ``a``: additional content
    * ``backticks``: prints backticks for beginning a code block
    * ``prefix``: override the default header prefix
    """
    print t.bold_yellow(prefix + ' ' + m) + '\n'
    if a != '':
        print a.strip('\n') + '\n'
    if backticks:
        print '```'

def section_end():
    """end a section in the standard way"""
    print '```\n'

# Classes

class Error(Exception):
    """general error exception"""
    pass

class UnknownPlugin(Error):
    """encountered an unknown plugin"""
    pass

class CommandFailed(Error):
    """command exited with non-zero return code"""
    pass

class IntermediateCommandFailed(CommandFailed):
    """intermediate command exited with non-zero return code"""
    pass

