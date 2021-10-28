#!/usr/bin/python
# -*- coding: latin-1 -*-
from setuptools import setup, find_packages

setup( name='SampleProject',
       version='0.0.0',
       author='Leonardo Baroncelli',
       author_email='leonardo.baroncelli@inaf.it',
       packages=find_packages(),
       package_dir={ 'SampleProject': 'SampleProject'},
       include_package_data=True
     )