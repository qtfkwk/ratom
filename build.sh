#!/bin/sh

# File: build.sh
# Version: 3.0.0
# Date: 2018-10-24
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

cd $(dirname $0)
./setup.py update doc bdist_wheel
./setup.py sdist --formats=zip

