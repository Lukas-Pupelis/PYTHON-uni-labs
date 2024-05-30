from setuptools import setup, Extension

module = Extension('unique_chars', sources=['unique_chars.c'])

setup(name='unique_chars',
      version='1.0',
      description='Unique Characters Check Module',
      ext_modules=[module])