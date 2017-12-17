RATOM Documentation
+++++++++++++++++++

Overview
========

Description
-----------

RATOM stands for "Rage Against The Outdated Machine".

Its purpose is to simply update all the things that need updating.

The primary use for RATOM is under current Python 2.x on a supported
operating system that uses one or more of the supported software.

Features
--------

.. include:: ../../README.rst

Design
------

* Show all configuration, commands, and output
* Use a modular plugin architecture
* Generating a report should be easy
* Run sequentially to avoid issues
* Halt when a command fails

Installation
------------

::

    pip install ratom

Can also install from either the binary distribution (or "wheel") or
source distribution files::

    pip install ratom-2.0.11-py2-none-any.whl
    pip install ratom-2.0.11.zip

Usage
-----

::

    usage: ratom [-h] [-n] [-c PATH] [-l PATH] [--show-config]
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
                     "macos freebsd aptget yum clamav homebrew perlbrew cpanm
                     pyenv pip rbenv gem npm msf git macos_microsoft"; ignored if
                     running a plugin directly

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
   See also the `API Reference`_.

   ::

        $ python
        >>> import ratom.clamav
        >>> ratom.clamav.check()
        True
        >>> ratom.clamav.main(['-n'])
        ...
        >>> ratom.clamav.main()
        ...
        >>> import ratom.all
        >>> ratom.all.main()
        ...

Versions
--------

+---------+------------+---------------------------------------------+
| Version | Date       | Comments                                    |
+=========+============+=============================================+
| 1.0.0   | 2016-05-25 | Initial release                             |
+---------+------------+---------------------------------------------+
| 1.0.1   | 2016-05-25 | Fixed release script, rearranged            |
|         |            | documentation                               |
+---------+------------+---------------------------------------------+
| 1.0.2   | 2016-05-25 | More work on release script and             |
|         |            | documentation                               |
+---------+------------+---------------------------------------------+
| 1.0.3   | 2016-05-25 | Improved release automation                 |
+---------+------------+---------------------------------------------+
| 1.0.4   | 2016-05-26 | Documentation: moved content from readme,   |
|         |            | fixed typo, renamed apple plugin to macosx; |
|         |            | Code: run brew upgrade via shell, log       |
|         |            | exceptions as errors, log command           |
+---------+------------+---------------------------------------------+
| 1.0.5   | 2016-05-26 | Pipe stderr in runp, aptget and yum plugins |
+---------+------------+---------------------------------------------+
| 1.0.6   | 2016-05-26 | Add aptget and yum plugins to documentation |
+---------+------------+---------------------------------------------+
| 1.0.7   | 2016-05-26 | Added descriptions of aptget and yum        |
|         |            | plugins to Plugins section of documentation |
+---------+------------+---------------------------------------------+
| 1.1.0   | 2016-05-26 | Changed UnknownModule exception to          |
|         |            | UnknownPlugin                               |
+---------+------------+---------------------------------------------+
| 2.0.0   | 2016-06-05 | Replaced pyenv global commands and fixed    |
|         |            | issue with vim in homebrew plugin; using    |
|         |            | os.path.realpath instead of readlink in git |
|         |            | plugin; has function; added ckver, current, |
|         |            | latest functions to freebsd plugin; using   |
|         |            | kron instead of date command; renamed       |
|         |            | microsoft plugin to macosx_microsoft;       |
|         |            | simplified function naming, logging;        |
|         |            | updated documentation                       |
+---------+------------+---------------------------------------------+
| 2.0.1   | 2016-06-06 | Fixes for freebsd plugin                    |
+---------+------------+---------------------------------------------+
| 2.0.2   | 2016-07-18 | Fix cask plugin failing when `cask list`    |
|         |            | gives name along with " (!)"; fix clamav    |
|         |            | plugin failing due to exiting with 1 when   |
|         |            | already up-to-date                          |
+---------+------------+---------------------------------------------+
| 2.0.3   | 2016-08-02 | Added ASCII art banner; improved logging in |
|         |            | cask plugin                                 |
+---------+------------+---------------------------------------------+
| 2.0.4   | 2016-08-03 | Renamed macosx to macos & macosx_microsoft  |
|         |            | to macos_microsoft; increased verbosity of  |
|         |            | cask plugin; added banner to usage (-h)     |
+---------+------------+---------------------------------------------+
| 2.0.5   | 2016-08-05 | Fix join error in cask plugin               |
+---------+------------+---------------------------------------------+
| 2.0.6   | 2016-08-05 | Added Contact section with URLs to header   |
+---------+------------+---------------------------------------------+
| 2.0.7   | 2016-09-22 | Use `--verbose` instead of `-v` with macos  |
|         |            | plugin `softwareupdate`                     |
+---------+------------+---------------------------------------------+
| 2.0.8   | 2016-11-30 | Added `--format=legacy` to `pip list`       |
|         |            | command in pip plugin; disable uploading    |
|         |            | documentation to pythonhosted site (will    |
|         |            | transition to readthedocs)                  |
+---------+------------+---------------------------------------------+
| 2.0.9   | 2016-12-08 | Removed cask plugin; remove the `--all`     |
|         |            | option from the `brew upgrade` command; fix |
|         |            | the npm plugin; minor fixes to output       |
+---------+------------+---------------------------------------------+
| 2.0.10  | 2017-12-17 | Fix the npm plugin to avoid "broken"        |
|         |            | outdated command; fix pyenv plugin to       |
|         |            | properly show the latest stable 2.x and 3.x |
|         |            | versions of Python; other minor fixes       |
+---------+------------+---------------------------------------------+
| 2.0.11  | 2017-12-17 | Fix bug in build system preventing the      |
|         |            | banner version from being updated           |
+---------+------------+---------------------------------------------+

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

* update Perl modules via CPANM for all perlbrew perls?
* update Python modules via pip for all pyenv pythons?
* update Ruby gems for all rbenv rubys?

Plugins
=======

The subsections below list details about each individual plugin.

In general, it is the user's responsibility to handle various side
effects of individual plugins, for example some plugins may require
reprocessing terminal startup scripts (``.bashrc``, etc) or even
rebooting.
Reprocessing startup scripts can be acheived by restarting the
terminal session either by issuing ``exit`` or Ctrl+D and reopening a
terminal or logging in again, or perhaps running ``exec $SHELL``.

Also note that RATOM runs as the user that runs it, upon the
assumption that the user has the appropriate permissions, etc.
Of course, if a plugin passes its ``check`` function, but lacks
permissions to perform the update then the command *should* fail, but
this depends on the individual update utility.
If it fails (exits with a non-zero value), RATOM will halt.
If this occurs, you might have an issue of this kind, and your courses
of action include fixing permissions of the item and its files for
your user, disabling the plugin in the configuration file, or
modifying the plugin's ``check`` or ``main`` functions to work
correctly.
Some ideas for the last fix might be to check if the user has proper
permissions, has a particular UID/EUID/GID/EGID, or to run the
command(s) via ``su`` or ``sudo``.

all
---

Attempts to run all plugins listed as command line arguments, in the
plugins list in the configuration file, or in the plugins list in the
``common.defaults`` dictionary (``common.defaults['plugins']``).
Regardless where the list of plugins is found, the plugins are run in
the order given.
The default order is designed to update operating systems first, then
any other security-related items, followed by development tools and
personal tools/repositories, and finally any GUI-based update
mechanisms.
Of course, each plugin must also pass its respective ``check``
function in order to actually perform the update.
This process prevents blindly attempting to run plugins on systems
that either don't have the software they update or more importantly,
when the user doesn't want RATOM to update them.

aptget
------

Updates Debian or Debian-based system (Ubuntu, Kali...) via
``apt-get update``, ``apt-get dist-upgrade -y``, then removes
unnecessary packages via ``apt-get autoremove -y``.

clamav
------

Manually updates Clam AntiVirus signatures via ``freshclam``.
This is in contrast to using the ``freshclamd`` daemon which can
likely do a better job of keeping the signatures up-to-date.
However, running freshclam manually confirms that the signatures are
up-to-date whether the system uses the daemon or not.

cpanm
-----

Uses cpan-outdated, which is installable via
``cpanm App::cpanoutdated``, to check for outdated Perl/CPAN modules
(``cpan-outdated -p``), then updates each via ``cpanm``.
This plugin runs against the "current" Perl, without regard for or
knowledge of things like Perlbrew.

freebsd
-------

Actually attempts to update several individual FreeBSD-specific items
as a single plugin.
Supported items are freebsd-update, portsnap, and pkg.
This plugin only updates the currently-tracked branch of FreeBSD; it
does not upgrade your system to the current release branch; i.e. if
your system has 10.2-RELEASE and 10.3-RELEASE is available, it will
not upgrade to 10.3-RELEASE for you, but it will tell you.

gem
---

Runs ``gem update`` to update globally-installed gems for the
"current" selected Ruby, without regard for or knowledge of things
like rbenv.

git
---

Performs a ``git pull`` for each repository or symlink to a repository
in ``~/.ratom/git/`` after first showing the remote upstream
repository via ``git remote -v``.
The ``check`` function fails if either the ``~/.ratom/git`` directory
does not exist or it does not contain any symlinks or directories.
Each repository path is *expanded* via ``os.path.realpath`` (`doc
<https://docs.python.org/3/library/os.path.html#os.path.realpath>`_)
to operate directly against the canonical path.

homebrew
--------

Updates Homebrew via ``brew update; brew upgrade --all``, then
performs clean up via ``brew cleanup``.

It also attempts to avoid a specific issue discussed `here
<https://github.com/Homebrew/homebrew-core/issues/1165>`_ encountered
when upgrading Vim (and using pyenv) by temporarily restoring the
"system" version of Python via the PYENV_VERSION environment variable
before running the upgrade command.
Note that this has initial success but should still be considered a
work-in-progress.

macos
------

Updates macOS via the ``softwareupdate`` utility.
An update may require reboot and the output will indicate this; the
rest of the update process will continue and it is the user's
responsibility to perform the reboot.

macos_microsoft
----------------

Runs the GUI-based Microsoft AutoUpdate utility, which updates
Microsoft software installed on a macOS system.
Unfortunately, this appears to be the only way to confirm that the
software is up-to-date, since searching for a command-line utility has
so far been fruitless.
This plugin blocks while the user clicks the "Check for Updates"
button, installs any updates, then closes the GUI.

msf
---

Updates Metasploit Framework via ``msfupdate``.

npm
---

Checks for updates, attempts to update, and confirms updates of global
NPM (Node.js) modules.

perlbrew
--------

Updates Perlbrew and shows the installed versions of Perl and
available versions of Perl; does not install any version of Perl for
you.

pip
---

Upgrades the ``pip`` package first, then attempts upgrading all other
installed packages.

pyenv
-----

Shows the installed versions of Python and the latest versions in the
2.7 and 3.5 branches; does not install any version of Python for you.

rbenv
-----

Show the installed versions of Ruby and the latest version in the 2.3
branch; does not install any version of Ruby for you.

yum
---

Updates Red Hat or a derivative (Fedora, CentOS...) via
``yum update -y``.

API Reference
=============

ratom.common
------------

.. automodule:: ratom.common
   :members:

Plugins
-------

ratom.all
'''''''''

.. automodule:: ratom.all
   :members:

ratom.aptget
''''''''''''

.. automodule:: ratom.aptget
   :members:

ratom.clamav
''''''''''''

.. automodule:: ratom.clamav
   :members:

ratom.cpanm
'''''''''''

.. automodule:: ratom.cpanm
   :members:

ratom.freebsd
'''''''''''''

.. automodule:: ratom.freebsd
   :members:

ratom.gem
'''''''''

.. automodule:: ratom.gem
   :members:

ratom.git
'''''''''

.. automodule:: ratom.git
   :members:

ratom.homebrew
''''''''''''''

.. automodule:: ratom.homebrew
   :members:

ratom.macos
''''''''''''

.. automodule:: ratom.macos
   :members:

ratom.macos_microsoft
''''''''''''''''''''''

.. automodule:: ratom.macos_microsoft
   :members:

ratom.msf
'''''''''

.. automodule:: ratom.msf
   :members:

ratom.npm
'''''''''

.. automodule:: ratom.npm
   :members:

ratom.perlbrew
''''''''''''''

.. automodule:: ratom.perlbrew
   :members:

ratom.pip
'''''''''

.. automodule:: ratom.pip
   :members:

ratom.pyenv
'''''''''''

.. automodule:: ratom.pyenv
   :members:

ratom.rbenv
'''''''''''

.. automodule:: ratom.rbenv
   :members:

ratom.yum
'''''''''

.. automodule:: ratom.yum
   :members:

