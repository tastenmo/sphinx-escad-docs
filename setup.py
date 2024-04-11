# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup, find_packages

directory = os.path.dirname(os.path.abspath(__file__))


README_PATH = os.path.join(directory, 'README.rst')


setup(
    name='sphinx-escad-docs',
    version='0.0.1',
    download_url='https://github.com/tastenmo/sphinx-escad-docs.git',
    license='MIT',
    author='Martin Heubuch',
    author_email='martin.heubuch@escad.de',
    description='An easy to use PDF Builder for Sphinx with a modern PDF-Theme.',
    long_description=open(README_PATH, encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_escaddocs',
              'sphinx_escaddocs.builders',
              'sphinx_escaddocs.directives',
              'sphinx_escaddocs.themes/escaddocs_theme',
              'sphinx_escaddocs.writers'
              ],
    package_data={'sphinx_escaddocs/themes/escaddocs_theme': [
        'theme.conf',
        '*.html',
        'static/styles/*.css',
        'static/js/*.js',
        'static/fonts/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx.html_themes': [
            'escaddocs_theme = sphinx_escaddocs.themes.escaddocs_theme',
        ],
        'sphinx.builders': [
            'escaddocs = sphinx_escaddocs.builders.escaddocs',
        ]
    },
    install_requires=[
        'sphinx',
        'weasyprint',       # the used PDF builder
        'libsass',           # needed to generate css on the fly
        'beautifulsoup4',    # needed for HTML manipulations
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
