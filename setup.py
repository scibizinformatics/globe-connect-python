#!/usr/bin/env python

from distutils.core import setup

setup(name='globe-connect-python',
      version='1.0',
      description='Globe Connect for Python',
      author='Globe Labs',
      author_email='API@globelabsbeta.com',
      url='http://www.globelabs.com.ph',
      packages=['globe', 'globe.connect'],
      depends=['pycurl']
     )