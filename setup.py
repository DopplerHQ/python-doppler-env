#!/usr/bin/env python3
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))


def long_description():
    with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
        return readme.read()


setup(
    name='doppler_env',
    version='0.3.0',
    python_requires='>=3.6',
    description='Inject Doppler secrets as environment variables into your Python application during local development with debugging support for PyCharm and Visual Studio Code.',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/dopplerhq/python-doppler-env',
    project_urls={
        'Bug Reports': 'https://github.com/dopplerhq/python-doppler-env/issues',
        'Source': 'https://github.com/dopplerhq/python-doppler-env',
    },
    author='Ryan Blunden',
    author_email='ryan.blunden@doppler.com',
    license='APL 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='doppler, environment variables, app secrets, app config, os.environ',
    packages=['doppler_env'],
    package_dir={'': 'src'},
    install_requires=['pip', 'python-dotenv'],
    extras_require={'dev': ['check-manifest'], 'test': []},
    package_data={},
    data_files=[('/', ["doppler_env.pth"])],
)
