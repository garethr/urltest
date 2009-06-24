#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "urltest",
    version = "0.1",
    author = "Gareth Rushgrove",
    author_email = "gareth@morethanseven.net",    
    url = "http://github.com/garethr/urltest",
    packages = find_packages('src'),
    package_dir = {'':'src'},
)
