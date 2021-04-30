#!/usr/bin/env python3
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


def long_description():
    with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
        return readme.read()


setup(
    name='doppler_env',
    version='0.1.1',
    python_requires='>=3.8',
    description='Automatically inject Doppler secrets as environment variables for use during local development',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/dopplerhq/python-doppler-env',
    project_urls={
        'Bug Reports': 'https://github.com/dopplerhq/python-doppler-env/issues',
        'Source': 'https://github.com/dopplerhq/python-doppler-env',
    },
    author='Doppler',
    author_email='support@doppler.com',
    license='APL 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='doppler, environment variables, app secrets, app config, os.environ',
    packages=['doppler_env'],
    package_dir={'': 'src'},
    install_requires=['pip', 'python-dotenv'],
    extras_require={'dev': ['check-manifest'], 'test': []},
    package_data={},
    data_files=[('/', ["doppler_env.pth"])],
)
