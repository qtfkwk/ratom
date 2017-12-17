#!/bin/sh

# File: build.sh
# Version: 2.0.10
# Date: 2017-12-17
# Author: qtfkwk <qtfkwk+ratom@gmail.com>
# Copyright: (C) 2016 by qtfkwk
# License: BSD 2-Clause License (https://opensource.org/licenses/BSD-2-Clause)

cd $(dirname $0)
./setup.py update doc bdist_wheel sdist

