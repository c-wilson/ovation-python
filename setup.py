#!/usr/bin/env python

from setuptools import setup

VERSION = "2.0-SNAPSHOT"
setup(name='ovation',
      version=VERSION,
      description='Ovation Python API',
      author='Physion',
      author_email='info@ovation.io',
      url='http://ovation.io',
      packages=['ovation', 'ovation.api', 'ovation.core', 'ovation.logging', 'ovation.test', 'ovation.test.util'],
      install_requires=[#"ovation-api >= {version}".format(version=VERSION),
                        "scipy >= 0.12.0",
                        "numpy >= 1.7.1",
                        "pandas >= 0.11.0",
                        "quantities >= 0.10.1",
                        ]
)