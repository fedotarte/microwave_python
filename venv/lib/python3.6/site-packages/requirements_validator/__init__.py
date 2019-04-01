#!/usr/bin/env python
import public
import requests


@public.add
def check(requirements):
    """return a list of invalid requirements"""
    invalid_requirements = []
    for req in requirements:
        req = req.split("#")[0]
        if not req:
            continue
        name = req.split("=")[0].split(">")[0].split("<")[0]
        url = "https://pypi.org/project/%s/" % name
        if "==" in req:
            url = "https://pypi.org/project/%s/%s/" % tuple(req.split("=="))
        r = requests.head(url)
        if r.status_code >= 400:
            invalid_requirements.append(req)
    return invalid_requirements
