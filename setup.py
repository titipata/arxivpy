#! /usr/bin/env python
from setuptools import setup

descr = '''Python wrapper for Arxiv API'''

if __name__ == "__main__":
    setup(
        name='arxivpy',
        version='0.1.dev',
        description='Python wrapper for Arxiv API',
        long_description=open('README.md').read(),
        url='https://github.com/titipata/arxivpy',
        author='Titipat Achakulvisut',
        author_email='titipata@u.northwestern.edu',
        license='(c) 2016 Titipat Achakulvisut',
        keywords='arxiv,xml,pdf',
        install_requires=['feedparser', 'python-dateutil'],
        packages=['arxivpy'],
    )
