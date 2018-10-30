#!/usr/bin/env python
from setuptools import setup


setup(
    name='mxnet-ssd',
    version=__version__,                
    description='This client library is designed to support MXNET-SSD',
    author='mperi',
    maintainer='mperi',
    url='https://github.com/mperi/mxnet-ssd/',
    license='Apache',
    packages=["mxnet-ssd"],
    long_description=open("README.rst").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'requests',
    ],
)
