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

