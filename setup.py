# -*- coding: utf-8 -*-
"""
This module contains the tool of birdhousebuilder.recipe.pycsw
"""
from setuptools import find_packages
from setuptools import setup

version = '0.2.0'
description = 'A Buildout recipe to install and configure pycsw Catalog Service (CSW) with Anaconda.'
long_description = (
    open('README.rst').read() + '\n' +
    open('AUTHORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

entry_point = 'birdhousebuilder.recipe.pycsw'
entry_points = {"zc.buildout": [
                            "default = %s:Recipe" % entry_point,
                          ],
                "zc.buildout.uninstall": [
                            "default = %s:uninstall" % entry_point,
                          ],
                       }

tests_require = ['zope.testing', 'zc.buildout', 'manuel']

setup(name='birdhousebuilder.recipe.pycsw',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Framework :: Buildout',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: BSD License',
      ],
      keywords='buildout recipe birdhouse pycsw geopython anaconda',
      author='Birdhouse',
      url='https://github.com/bird-house/birdhousebuilder.recipe.pycsw',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['birdhousebuilder', 'birdhousebuilder.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        # -*- Extra requirements: -*-
            		'Mako',
            		'birdhousebuilder.recipe.conda',
            		'birdhousebuilder.recipe.supervisor',
            		'birdhousebuilder.recipe.nginx',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='birdhousebuilder.recipe.pycsw.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
