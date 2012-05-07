# Copyright (C) 2011-2012 Ralph Bean
# License: http://www.gnu.org/licenses/gpl-2.0.txt GPL version 2 or higher

from setuptools import setup, find_packages
import sys, os

import multiprocessing, logging

version = '0.1.3'

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

setup(name='virtualenvcontext',
      version=version,
      description="switch virtualenvs with a python context manager",
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
      ],
      keywords='',
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='http://github.com/ralphbean/virtualenvcontext',
      license='GPLv2+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      test_suite='nose.collector',
      tests_requires=[
          'nose',
      ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'virtualenvwrapper',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
     )
