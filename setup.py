# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup (
        name         = 'sphinx-pdfembed',
        version      = '1.0',
        author       = 'Super Kogito',
        author_email = 'superkogito@gmail.com',
        description  = 'Sphinx extension to embedd a pdf files webpages',
        license      = 'MIT',
        url          = 'https://github.com/SuperKogito/sphinx-pdfembed',
        packages     = find_packages(),
        classifiers  = [
                        "Programming Language :: Python :: 3",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: OS Independent",
                       ],        
     )
