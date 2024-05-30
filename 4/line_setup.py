from setuptools import setup, Extension

module = Extension('line', sources=['line.c'])

setup(name='line',
      version='1.0',
      description='Line Module',
      ext_modules=[module])