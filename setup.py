#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import setuptools

def version():
    #return __import__('FPAdmin.__init__').__version__
    return '1.1'

if sys.version_info < (2, 6):
    raise RuntimeError('python 2.6 or greater is required')

setuptools.setup(
    name='lteadmin',
    version=version(),
    description='admin system',
    author='cf.com',
    author_email='',
    platforms=['linux'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    scripts=[],
    install_requires=[
        #'gevent==1.0.2',
    ],
    dependency_links=[
    ]
)

