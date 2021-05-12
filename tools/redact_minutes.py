#!/usr/bin/env python3

"""Simple tool to redact HPC carpentry meeting minutes

Usage:

    python3 redact_minutes.py MEETING_MINUTE.md

This tool will back up the original minute as `MEETING_MINUTE.md.orig`.
Safety checks are in place to refuse overwriting either the backup (original)
or the redacted copy if those files exist.
"""

import os
import re
import sys


def read_minute(fn):
    with open(fn, 'r') as F:
        Lines = list(map(lambda s: s.rstrip('\n\r'), F.readlines()))
    return Lines


def write_minute(fn, Lines):
    with open(fn, 'w') as F:
        F.write('\n'.join(Lines))
        F.write('\n')


def scan_lines(Lines, i, match_func):
    while not match_func(Lines[i]):
        i += 1
    return i


def redact(Lines):
    """Main redaction routine.
    This saves the redacted text lines into a new list (the function's return value).
    """
    i = 0
    rslt = []
    while i < len(Lines):
        if Lines[i].startswith('Both meetings will use [Google Meet]('):
            # skip all these lines ... until we encounter two spoilers mentioned below
            i = scan_lines(Lines, i, lambda s: s.startswith(':::spoiler You can also call in by phone'))
            i = scan_lines(Lines, i, lambda s: s == ':::')
            i = scan_lines(Lines, i, lambda s: s.startswith(':::spoiler Backup venue in case nobody can enter'))
            i = scan_lines(Lines, i, lambda s: s == ':::')
            rslt.append('Both meetings will use [Google Meet -URL redacted-].')
        elif Lines[i] == ':::info' and Lines[i+1].startswith('This document is synchronized as you type,'):
            # skip all these lines ... until we encounter two spoilers mentioned below
            i = scan_lines(Lines, i, lambda s: s == ':::')
            i = scan_lines(Lines, i, lambda s: s.startswith(':::danger'))
            i = scan_lines(Lines, i, lambda s: s == ':::')
            # no text added
        else:
            rslt.append(Lines[i])
        i += 1
    return rslt


def main_redact(fn):
    """Main redaction subprogram.
    This function reads in the original text from an input file,
    backs up the original input file by appending the '.orig' suffix.
    Then performs the redaction, and saves the output file to under the original name.
    If the original name has '.orig' already, it strips that suffix.
    For safety, this subprogram will throw an error if the destination file exists.
    """
    Lines = read_minute(fn)

    if not fn.endswith('.orig'):
        fn_output = fn
        fn_backup = fn + '.orig'
        if os.path.exists(fn_backup):
            raise FileExistsError('Backup file ' + fn_backup + ' exists, cannot continue.')
        os.rename(fn, fn_backup)
    else:
        fn_output = fn[:-5]
        if os.path.exists(fn_output):
            raise FileExistsError('Output file ' + fn_output + ' exists, cannot continue.')

    Lines_redacted = redact(Lines)
    write_minute(fn_output, Lines_redacted)


if __name__ == '__main__':
    main_redact(sys.argv[1])
