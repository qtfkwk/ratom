#!/usr/bin/env python

# File: setup.py
# Version: 1.0.4
# Date: 2016-05-26
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

import setuptools

v = '1.0.4'

cfg = dict(
    name='ratom',
    version=v,
    author='qtfkwk',
    author_email='qtfkwk+ratom@gmail.com',
    description='Rage Against The Outdated Machine',
    long_description=open('README.rst', 'rb').read(),
    packages=setuptools.find_packages(),
    install_requires=[
        'blessings',
    ],
    url='https://github.com/qtfkwk/ratom',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'ratom = ratom.all:main',
        ],
    },
)

if __name__ == '__main__':
    import ratom
    import sys
    a = sys.argv[1:]
    if 'update' in a:
        import datetime
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        files = 'ratom/*.py setup.py *.sh'
        doc = 'doc/source/index.rst'
        conf = 'doc/source/conf.py'
        c = [
            r"sed -i _ 's/^# Date: .*$/# Date: %s/' %s" % (today, files),
            r"sed -i _ 's/^# Version: .*$/# Version: %s/' %s" % (v, files),
            r"sed -i _ 's/ratom-[0-9]*\.[0-9]*\.[0-9]*/ratom-%s/' %s" % (v, doc),
            r"sed -i _ 's/[0-9]*\.[0-9]*\.[0-9]/%s/' %s" % (v, conf),
            r"rm -f ratom/*.py_ setup.py_ *.sh_ %s_ %s_" % (doc, conf),
        ]
        for i in c:
            print ratom.t.bold('$ ' + i)
            ratom.run_(i, shell=True)
        sys.argv = filter(lambda x: x != 'update', sys.argv)
        if len(sys.argv) < 2:
            sys.exit(0)
    if 'doc' in a:
        c = [
            r'make -C doc html latexpdf',
            r'cp -R doc/build/html doc/ratom-doc-html',
            r'tar czf doc/ratom-doc-html.tgz -C doc ratom-doc-html',
            r'cp doc/build/latex/ratom.pdf doc/ratom-doc.pdf',
        ]
        for i in c:
            print ratom.t.bold('$ ' + i)
            ratom.run_(i)
        sys.argv = filter(lambda x: x != 'doc', sys.argv)
        if len(sys.argv) < 2:
            sys.exit(0)
    setuptools.setup(**cfg)

