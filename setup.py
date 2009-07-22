#!/usr/bin/python

from distutils.core import setup

setup(name='turnin-ng',
      version='1.0~beta1',
      description='Turn in your assignments with turnin',
      author='Ryan Kavanagh',
      author_email='ryanakca@kubuntu.org',
      license='GNU General Public License version 2, or (at your option) ' +\
              'any later version',
      scripts=['src/bin/project', 'src/bin/turnin'],
      packages=['turnin'],
      package_dir={'turnin':'src/turnin'},
      data_files=[('/usr/local/share/man/man1/', ['doc/turnin.1', 'doc/project.1'])]
)
