#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.api.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
version = open("VERSION").read()
desc = open("README.md").read()

setup(
    name='mapzen.whosonfirst.api',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.api'],
    version=version,
    description='',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-api',
    install_requires=[
        'flamework.api',
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-flamework-api/tarball/master#egg=flamework-api-0.41',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-api/releases/tag/' + version,
    license='BSD')
