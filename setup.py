#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cs-models',
    version='0.0.1',
    packages=['cs_models'],
    include_package_data=True,
    license='MPL 2.0',

    author='Timothée Mazzucotelli',
    author_email='timothee.mazzucotelli@gmail.com',
    url='https://github.com/Pawamoy/django-cs-models',

    install_requires=['future'],

    keywords="complex system hierarchy models",
    description="A Django app that helps you creating models "
                "within a Complex System architecture",
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        'Development Status :: 4 - Beta',
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ]
)
