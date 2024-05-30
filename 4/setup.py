from setuptools import setup, Extension

module = Extension('unique', sources=['unique_characters.c'])

setup(
    name='unique',
    version='1.0',
    description='Module for checking unique characters in a string and custom UniqueString type.',
    ext_modules=[module],
)