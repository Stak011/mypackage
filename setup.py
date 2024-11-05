from setuptools import setup, find_packages

setup(
    name='Stak',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Stak011/sorty',
    author='Akinkunmi',
    author_email='ioakinkunmi@gmail.com'
)