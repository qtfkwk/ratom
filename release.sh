#!/bin/sh -x

# File: release.sh
# Version: 1.0.3
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

set -eo pipefail

cd $(dirname $0)

v=$(grep '^v = ' setup.py |cut -d\' -f2)
v_=$(echo $v |sed 's/\./\\./g')

# ensure entry in versions table
grep \|\ $v_ doc/source/index.rst

git clean -dxf

# build and upload doc
./setup.py update doc
./setup.py upload_sphinx

git clean -dxf

# github
git add *
git commit -m release\ $v
git push
git tag -a $v -m release\ $v
git push origin --tags

# pypi
./setup.py sdist --formats=zip upload
./setup.py bdist_wheel upload

