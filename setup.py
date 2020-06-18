# -*- coding: utf-8 -*-
from distutils.core import setup

from setuptools import find_packages

LONGDOC = """
python project template
"""

setup(name='hello-python',
      version='1.0.0',
      description='hello python',
      long_description=LONGDOC,
      author='Daphnis',
      author_email='daphnisz@163.com',
      url='https://github.com/xx',
      license="MIT",
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Natural Language :: Chinese (Traditional)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Topic :: python template'
      ],
      keywords='template',
      packages=find_packages('hello-python'),
      package_dir={'': 'hello-python'},
      package_data={'hello': ['*.*', 'info/*']}
      )
