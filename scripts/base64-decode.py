#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Gleb Smirnov <glebsmirnov0708@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from base64 import b64decode
from sys import stdin, stdout, stderr

try:
    result = b64decode(stdin.read()).decode()
except Exception:
    stderr.write("Invalid Base64-encoded text")
    exit(1)

stdout.write(result)
