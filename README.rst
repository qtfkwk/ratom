Description
-----------

RATOM stands for "Rage Against The Outdated Machine".

Its purpose is to simply update all the things that need updating.

The primary use for RATOM is under current Python 2.x on a supported
operating system that uses one or more of the supported software.

Features
--------

* Supports Mac OSX, FreeBSD (freebsd-update, portsnap, pkg),
  ClamAV/freshclam, Homebrew, Cask, Perlbrew, CPAN Minus, pyenv, pip,
  rbenv, gem, npm, Metasploit Framework, Git repositories, and
  Microsoft AutoUpdate via a plugin architecture
* Markdown-formatted output with all update and informational commands
  shown with their output and in pretty terminal colors via the
  `blessings <https://pypi.python.org/pypi/blessings>`_ package; also
  allows subsequent processing by redirecting or piping
* Dry run mode (``-n``) processes configuration file and command line
  arguments, performs checks and intermediate processing, prints
  commands to show what will run given configuration and system
  settings, but doesn't actually update anything
* Configuration via ``~/.ratom/config.json`` or an argument to ``-c``
  option; allows switching the ordering of plugins (not recommended),
  explicit enabling or disabling of plugins, and specifying a
  different path for the log file
* Logs intermediate processing commands and other informational
  messages to the configured log location (``~/.ratom/ratom.log`` by
  default) or an argument to ``-l`` option
* Shows full configuration details if ``--show-config`` option is used
* Each plugin provides a ``check`` function to determine whether to
  run and a ``main`` function that performs the update
* Full documentation `online <http://pythonhosted.org/ratom>`_, or as
  `HTML (gzipped tar)
  <https://github.com/qtfkwk/ratom/raw/master/doc/ratom-doc-html.tgz>`_
  or PDF (`view
  <https://github.com/qtfkwk/ratom/blob/master/doc/ratom-doc.pdf>`_,
  `download
  <https://github.com/qtfkwk/ratom/raw/master/doc/ratom-doc.pdf>`_)
  via `Sphinx <http://www.sphinx-doc.org/>`_

Design
------

* Show all configuration, commands, and output

    * intermediate commands are shown in the log versus the output for
      brevity's sake

* Use a modular plugin architecture, not only for code organization,
  but to easily support more software
* Generating a report should be easy
* Run sequentially to avoid issues
* Halt when a command fails

Installation
------------

::

    pip install ratom

Can also install from either the binary distribution (or "wheel") or
source distribution files::

    pip install ratom-1.0.0-py2-none-any.whl
    pip install ratom-1.0.0.zip

Usage
-----

::

    usage: all.py [-h] [-n] [-c PATH] [-l PATH] [--show-config]
                  [plugin [plugin ...]]
    
    optional arguments:
      -h, --help     show this help message and exit
    
    ratom options:
      -n             Dry run; don't actually update anything
      -c PATH        Use alternate configuration file; default:
                     ~/.ratom/config.json
      -l PATH        Log to PATH; default: ~/.ratom/ratom.log
      --show-config  Show full configuration details
      plugin         Specific plugin(s) to run in the specified order; default:
                     "macosx freebsd clamav homebrew cask perlbrew cpanm pyenv pip
                     rbenv gem npm msf git microsoft"; ignored if running a plugin
                     directly

Examples
--------

RATOM can be used in a few ways...

1. Install with pip and run via the installed ``ratom`` shim
2. Clone the Git repository or unzip the source distribution and run
   either ``ratom/all.py`` or one of the plugins directly
3. Do #2 but also add symlinks to somewhere in your PATH::

        cd ~/bin
        ln -s path/to/ratom/ratom/all.py ratom

4. Use the Python REPL (or programtically from other Python code).
   Import ``ratom.all`` or a specific plugin, then call a ``main``
   function and pass any arguments in command-line fashion via the
   ``argv`` argument or a configuration dictionary via the ``cfg``
   argument.
   Note that if you want to call a ``check`` function, you'll need to
   import ``raton.common``.
   See also the `API Reference`_.

   ::

        $ python
        >>> import ratom.all
        >>> ratom.all.main()
        ...
        >>> ratom.clamav.main()
        ...
        >>> import ratom.clamav
        >>> ratom.clamav.main()
        ...
        >>> ratom.clamav.main(['-n'])
        ...
        >>> import ratom.common
        >>> ratom.clamav.check()
        True

Versions
--------

+---------+------------+--------------------------------------+
| Version | Date       | Comments                             |
+=========+============+======================================+
| 1.0.0   | 2016-05-25 | Initial release                      |
+---------+------------+--------------------------------------+
| 1.0.1   | 2016-05-25 | Fixed release script, rearranged     |
|         |            | documentation                        |
+---------+------------+--------------------------------------+

Issues
------

Please report issues via
`Github Issues <https://github.com/qtfkwk/ratom/issues>`_.

Better yet, fork the Github repository, fix the issue, and send a PR
(pull request)!

Contact
-------

* `Github <https://github.com/qtfkwk/ratom>`_
* `PyPI <https://pypi.python.org/pypi/ratom>`_
* `Documentation <http://pythonhosted.org/ratom>`_

To do
-----

* support Debian/Ubuntu (apt-get), Red Hat/Fedora/CentOS (yum)...
* run ``brew upgrade --all`` with the pyenv version set to
  'system' without using ``pyenv global``
* update Perl modules via CPANM for all perlbrew perls?
* update Python modules via pip for all pyenv pythons?
* update Ruby gems for all rbenv rubys?

