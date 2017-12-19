#!/bin/sh -x

# File: release.sh
# Version: 2.0.12
# Date: 2017-12-18
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
./setup.py update
#./setup.py doc upload_sphinx
# PyPI's pythonhosted documentation site appears to be deprecated; Error:
# "Upload failed (410): Uploading documentation is no longer supported, we
# recommend using https://readthedocs.org/."
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

