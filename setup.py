#!/usr/bin/env python

"""
Install distmetric package. 
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="distmetric",
    version="0.0.1",
    description="A package for calculating phylogenetic tree distances",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
    	"toytree",
    	"pandas",
    	"numpy",
    ],
    entry_points={
        "console_scripts": ["distmetric = distmetric.__main__:run"],
    },
)
