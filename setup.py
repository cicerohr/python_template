import os

from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='_template',
    version='',
    packages=[''],
    url='',
    license='MIT License',
    author='Cícero',
    author_email='cicerohr@gmail.com',
    description='Template para projetos',
    long_description=read('README.md'),
)
