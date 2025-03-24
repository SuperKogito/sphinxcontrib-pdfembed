# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

f = open('README.md', 'r')
try:
    long_desc = f.read()
finally:
    f.close()

requires = ['Sphinx>=0.6']

setup (
        name         = 'sphinxcontrib-pdfembed',
        version      = '0.1',
        author       = 'Super Kogito',
        author_email = 'superkogito@gmail.com',
        description  = 'Sphinx extension to embedd a pdf files webpages',
        license      = 'MIT',
        url          = 'https://github.com/SuperKogito/sphinx-pdfembed',
        packages     = find_packages(),
        classifiers  = [
                        'Development Status :: 3 - Alpha',
                        'Environment :: Console',
                        'Environment :: Web Environment',
                        'Framework :: Sphinx :: Extension',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: BSD License',
                        'Operating System :: OS Independent',
                        'Programming Language :: Python',
                        'Topic :: Documentation',
                        'Topic :: Utilities',
                      ],
        platforms            = 'any',
        include_package_data = True,
        install_requires     = requires,
        namespace_packages   = ['sphinxcontrib'],
     )
