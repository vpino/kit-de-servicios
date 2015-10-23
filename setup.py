#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="kds",
    packages=find_packages(),
    version="1.0",
    install_requires=[
        "django >= 1.7",
    ],
    package_data = {
        '': [".txt", ".png", ".html", ".css", ".jpeg", ".js"]
    },
    zip_safe=False,
    include_package_data=True
)
