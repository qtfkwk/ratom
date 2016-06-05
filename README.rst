* Supports Mac OSX, FreeBSD (freebsd-update, portsnap, pkg),
  Debian and derivatives (apt-get), Red Hat and derivatives (yum),
  ClamAV/freshclam, Homebrew, Cask, Perlbrew, CPAN Minus (cpanm),
  pyenv, pip, rbenv, gem, npm, Metasploit Framework, Git repositories,
  and Microsoft AutoUpdate via a plugin architecture
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
* Logs intermediate processing commands and other informational and
  error messages to the configured log location
  (``~/.ratom/ratom.log`` by default) or an argument to ``-l`` option
* Shows full configuration details if ``--show-config`` option is
  used; be sure to combine with ``-n`` if you don't want to update
  anything
* Each plugin provides a ``check`` function to determine whether to
  run and a ``main`` function that performs the update
* Full documentation in HTML (`online
  <http://pythonhosted.org/ratom>`_,
  `gzipped tar
  <https://github.com/qtfkwk/ratom/raw/master/doc/ratom-doc-html.tgz>`_)
  and PDF (`view
  <https://github.com/qtfkwk/ratom/blob/master/doc/ratom-doc.pdf>`_,
  `download
  <https://github.com/qtfkwk/ratom/raw/master/doc/ratom-doc.pdf>`_)
  via `Sphinx <http://www.sphinx-doc.org/>`_

