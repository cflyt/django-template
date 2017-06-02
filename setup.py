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
        #'git+https://nanny.netease.com/bxx/leazy-ext.git@v0.3.19#egg=leazy_ext-0.3.19',
        #'git+https://nanny.netease.com/yangjunwei/webapp2-enhance.git@v0.1.1#egg=webapp2_enhance-0.1.1',
    ]
)

