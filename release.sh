#!/bin/sh

# File: release.sh
# Version: 1.0.2
# Date: 2016-05-25
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

set -eo pipefail
cd $(dirname $0)
git clean -dxf
./setup.py update doc
./setup.py upload_sphinx
git clean -dxf
git add *
v=$(grep '^v = ' setup.py |cut -d\' -f2)
git commit -m release\ $v
git push
git tag -a $v -m release\ $v
git push origin --tags
./setup.py sdist --formats=zip upload
./setup.py bdist_wheel upload

