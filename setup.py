#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "urltest",
    version = "0.1",
    
    packages = find_packages('src'),
    package_dir = {'':'src'},
)