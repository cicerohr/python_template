import os

from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='Template',
    version='',
    packages=[''],
    url='',
    license='MIT License',
    author='',
    author_email='your_email@domain.com',
    description='Project template',
    long_description=read('README.md'),
)
