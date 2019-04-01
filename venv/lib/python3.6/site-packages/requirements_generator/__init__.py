#!/usr/bin/env python
import os
import public
import sys
import subprocess


def getname(line):
    """return a list of requirements names without versions and comments"""
    delimeters = ["=", "<", ">", "#"]
    for delimeter in delimeters:
        line = line.split(delimeter)[0]
    return line.rstrip()


def getnames(requirements):
    """return a list of requirements names without versions and comments"""
    names = []
    for r in requirements:
        names.append(getname(r))
    return list(filter(None, sorted(names)))


@public.add
class Requirements(list):
    """requirements class. methods: `load`, `replace`, `save`, `scan`"""

    def load(self, path):
        """load requirements from a file"""
        requirements = open(path).read().splitlines()
        self += requirements
        self[:] = list(sorted(self))
        return self

    def remove(self, line):
        """remove line (if exists)"""
        if line in self:
            list.remove(self, line)
        return self

    def replace(self, data):
        """replace requirements in a file"""
        for old, new in data.items():
            self[:] = [new if getname(r).lower() == old.lower() else r for r in self]
        return self

    def save(self, path=None, v=True):
        """save requirements to a file. Set `v` to `False` to suppress verions"""
        if not path:
            path = "requirements.txt"
        path = os.path.abspath(os.path.expanduser(path))
        dirname = os.path.dirname(path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        string = "\n".join(self)
        if not v:
            string = "\n".join(getnames(list(self)))
        open(path, "w").write(string)
        return self

    def scan(self, path=None, v=True):
        """scan a directory for a  requirements. Set `v` to `False` to suppress versions"""
        if not path:
            path = "."
        args = [sys.executable, "-m", "pipreqs.pipreqs", "--print", path]
        out = subprocess.check_output(args, stderr=subprocess.PIPE).decode("utf-8").rstrip()
        requirements = out.splitlines()
        requirements = list(filter(lambda r: "==info" not in r, requirements))
        if not v:
            requirements = getnames(requirements)
        self[:] = requirements
        return self


@public.add
def replace(path, data):
    """replace requirements in a file"""
    return Requirements().load(path).replace(data).save(path)


@public.add
def scan(path=None, v=True):
    """scan a directory and return a `Requirements` object/list. Set `v` to `False` to suppress versions"""
    return Requirements().scan(path, v)
