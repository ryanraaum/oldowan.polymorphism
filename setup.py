from setuptools import setup, find_packages
import sys, os

desc_lines = open('README', 'r').readlines()

version_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'oldowan','polymorphism', 'VERSION'))
version = version_file.read().strip()
version_file.close()

setup(name='oldowan.polymorphism',
      version=version,
      description=desc_lines[0],
      long_description=''.join(desc_lines[2:]),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Scientific/Engineering :: Bio-Informatics"
      ],
      keywords='',
      platforms=['Any'],
      author='Ryan Raaum',
      author_email='code@raaum.org',
      url='http://www.raaum.org/software/oldowan',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages = ['oldowan'],
      include_package_data=False,
      data_files=[("oldowan/polymorphism", ["oldowan/polymorphism/VERSION"])],
      zip_safe=False,
      test_suite = 'nose.collector',
      )
