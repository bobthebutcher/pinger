import os
from setuptools import setup, find_packages


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
        return f.read()


setup(
    name='pinger',
    version=read('VERSION'),
    author='Brad Searle',
    author_email='bradleysearle@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    long_description=read('README.md'),

    include_package_data=True,
    packages=find_packages(),

    install_requires=[
    ],

    entry_points={
        'console_scripts': [
            'pinger = pinger',
        ]
    },

)
