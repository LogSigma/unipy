#-*- coding: utf-8 -*-
"""
Created on 2017-01-05 20:55:26
Modified on 2017-06-26 02:36:25

@author: Young Ju Kim
"""


import os
import datetime as dt
import tarfile
import distutils
import subprocess

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
from distutils.cmd import Command


__version__ = '0.1.9'

desc = """
This contains a number of useful objects for data manipulation & analysis.
"""

with open('README.rst', 'r', encoding='utf-8') as readme_file:
    long_desc = readme_file.read()


class SphinxCommand(Command):
    """Documentation Command"""

def initialize_options(self):
    """Set default values for options."""
    pass

def finalize_options(self):
    """Post-process options."""
    pass

def run(self):
    """Run command."""
    command = ['cd docs;make html;cd ..']
    # command.append(os.getcwd())
    self.announce(
        'Running command: %s' % str(command),
        level=distutils.log.INFO)
    subprocess.check_call(command)


with open('unipy/__version__.py', 'w') as f:
    version_py_string = '''#-*- coding: utf-8 -*-
# This file is automatically generated by 'setup.py'
"""
Created on 2017-01-05 20:53:15
Modified on {modified_time}

@author: Young Ju Kim
"""


__all__ = ['__version__']


__version__ = '{version}'

'''.format(modified_time=dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
           version=__version__)
    f.write(version_py_string)



def package_data_listup():

    filename = 'dataset/resources.gz/resources.tar.gz'
    tar = tarfile.open(filename)
    filelist = list(set(map(lambda x: x.split('/')[0], tar.getnames())))
    filelist.sort()
    return filelist

required_packages = [
                     'pandas >= 0.20.1',
                     'numpy >= 1.13.1',
                     'numpydoc >= 0.7.0',
                     'scipy >= 0.19.1',
                     'scikit-learn >= 0.18.0',
                     'statsmodels >= 0.8.0',
                     'matplotlib >= 2.0.2',
                     'paramiko >= 2.1.2',
                     'pandasql >= 0.7.3',
                     'seaborn >= 0.8',
                     'scikit-image >= 0.13.0',
                     'PyDrive >= 1.2.1',
                     'oauth2client >= 4.1.2',
                     'google-auth-oauthlib >= 0.2.0',
                     'pyasn1 >= 0.4.3',
                     'pyasn1-modules >= 0.2.1',
                    #'pyqt5',
                     'mglearn >= 0.1.6',
                    # 'numba >= 0.34.0',
                    # 'nomkl',  # conda
                    ]

# REQUIREMENTS.txt for [`Travis CI`, `readthedocs`]
for requirement_file in ['REQUIREMENTS.txt', 'requirements.txt']:
    with open(requirement_file, 'w') as f:
        header = '--index-url https://pypi.python.org/simple/'
        pkg_ls = '\n'.join(required_packages).replace('>=', '>=')
        f.write('\n'.join([header, pkg_ls]))

setup(name='unipy',
      version=__version__,
      description='Useful tools for Data Scientists',
      long_description=long_desc,
      url='https://unipy.readthedocs.io/en/latest/index.html',
      download_url='http://github.com/pydemia/unipy',
      author='Young Ju Kim',
      author_email='pydemia@gmail.com',
      license='MIT License',
      classifiers=[
            # How Mature: 3 - Alpha, 4 - Beta, 5 - Production/Stable
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Operating System :: OS Independent',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Natural Language :: English',
            ],
      packages=find_packages(exclude=['contrib',
                                     #  'docs',
                                      'tests']),
      cmdclass={'documentation': SphinxCommand},
      #setup_requires=required_packages,
      install_requires=required_packages,
      zip_safe=False,
      package_data={'unipy': ['*.gz', 'dataset/resources.tar.gz']}
      )
