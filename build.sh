#!/bin/sh

# File: build.sh
# Version: 2.1.0
# Date: 2017-12-29
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

cd $(dirname $0)
./setup.py update doc bdist_wheel sdist

