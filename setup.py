import os
from setuptools import setup

setup(packages=['RGHAFS20'],
      package_dir={'' : 'src'},
      name='RGHAFS20',
      version=os.environ['PKG_VERSION'],
      # package_data = {'RGHAFS20': ['data/*']},
      zip_safe=False)