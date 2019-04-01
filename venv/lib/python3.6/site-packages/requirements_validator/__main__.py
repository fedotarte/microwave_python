#!/usr/bin/env python
"""validate `requirements.txt` file"""
import click
import requirements_validator
import os
import sys

MODULE_NAME = "requirements_validator"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path' % MODULE_NAME


@click.command()
@click.argument('path', required=False)
def _cli(path=None):
    if path is not None:
        requirements = open(path).read().splitlines()
    else:
        if not os.isatty(sys.stdin.fileno()):
            requirements = sys.stdin.read().splitlines()
        else:
            sys.exit("ERROR: stdin empty")
    invalid = requirements_validator.check(requirements)
    if invalid:
        sys.exit("ERROR: %s" % "\n".join(invalid))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
