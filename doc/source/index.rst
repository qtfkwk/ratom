RATOM Documentation
+++++++++++++++++++

Overview
========

.. include:: ../../README.rst

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

apple
-----

Updates Apple Mac OSX via the ``softwareupdate`` utility.
An update may require reboot and the output will indicate this; the
rest of the update process will continue and it is the user's
responsibility to perform the reboot.

cask
----

Updates Homebrew casks by running ``brew cask info`` for each
installed cask package as an intermediate command to determine whether
there is an update available.
If so, it runs ``brew cask install`` to install the updated cask.
Finally, ``brew cask cleanup`` is run to remove temporary files and
perform general maintainance tasks.

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
Supported items are freebsd-update, portsnap, pkg, and a custom
utility called ckver, that queries the freebsd.org website to compare
the latest release version to the current running version on the
system.
This plugin only updates the currently-tracked branch of FreeBSD; it
does not upgrade your system to the current release branch; i.e. if
your system has 10.2-RELEASE and 10.3-RELEASE is available, it will
not upgrade to 10.3-RELEASE for you, but ckver will tell you if a new
release is avaiable.

gem
---

Runs ``gem update`` to update globally-installed gems for the
"current" selected Ruby, without regard for or knowledge of things
like rbenv.

git
---

Performs a ``git pull`` for each repository or symlink to a repository
in ``~/.ratom/git/`` after first showing where the symlink points (if
it's a symlink) and the set of tracked repositories via
``git remote -v``.
The ``check`` function fails if either the ``~/.ratom/git`` directory
does not exist or it does not contain any repositories.

homebrew
--------

Updates Homebrew via ``brew update; brew upgrade --all``, then
performs clean up via ``brew cleanup``.

It also attempts to avoid specific issues encountered when upgrading
vim by restoring the "system" version of Python via pyenv before
running the upgrade command.
This has had mixed success, has some unintentional temporary
system-wide side effects, and should be considered a work-in-progress.

microsoft
---------

Runs the GUI-based Microsoft AutoUpdate utility, which updates
Microsoft software installed on a Mac OSX system.
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

API Reference
=============

ratom.common
------------

.. automodule:: ratom.common
   :members:

ratom.all
---------

.. automodule:: ratom.all
   :members:

Plugins
-------

ratom.cask
''''''''''

.. automodule:: ratom.cask
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

ratom.macosx
''''''''''''

.. automodule:: ratom.macosx
   :members:

ratom.microsoft
'''''''''''''''

.. automodule:: ratom.microsoft
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

