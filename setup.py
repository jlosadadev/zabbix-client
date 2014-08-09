#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()

setup(
    name='zabbix-client',
    version='0.1.0',
    description='Zabbix API wrapper',
    long_description=readme,
    author='Jesús Losada Novo',
    author_email='jlosadadev@gmail.com',
    url='https://github.com/jlosadadev/zabbix-client',
    license='Apache 2.0',
    packages=['zabbix_client'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Systems Administration'
    ],
    keywords=['zabbix', 'api', 'json-rpc', 'monitoring']
)
