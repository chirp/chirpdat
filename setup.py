#!/usr/bin/env python

from setuptools import setup

__version__ = '1.0.1'

setup(
    name='chirpdat',
    version=__version__,
    description='chirpdat',
    long_description='Share files of any size with Chirp and dat',
    license='MIT',
    author='Asio Ltd.',
    author_email='developers@chirp.io',
    url='https://developers.chirp.io',
    install_requires=['chirpsdk==3.4.1', 'configparser==3.5.0'],
    include_package_data=True,
    keywords=['dat', 'chirp', 'sharing'],
    scripts=['chirpdat'],
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Communications',
        'Development Status :: 4 - Beta',
        'Environment :: Console'
    ]
)
