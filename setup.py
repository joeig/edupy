from codecs import open
from os import path

from setuptools import setup, find_packages

from memodrop.__about__ import *

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    url=__url__,
    author=__author__,
    python_requires='>=3.6, <4',
    packages=find_packages(exclude=['docs']),
    include_package_data=True,
    install_requires=[
        'Django~=2.2',
        'django-bootstrap4==0.0.8',
        'django-fa~=1.0.0',
        'django-jsonview~=1.2',
        'django-markdown-deux~=1.0',
        'django-q~=1.0',
        'django-sendmail-backend~=0.1',
        'django-watchman~=0.17',
        'djangorestframework~=3.9',
        'markdown2~=2.3',
        'numpy~=1.16',
        'pytz==2019.1',
    ],
    extras_require={
        'dev': [
            'bumpversion~=0.5',
            'coverage~=4.5',
            'PyYAML~=5.1',
            'setuptools~=41.0',
            'flake8~=3.7',
        ],
    },
)
