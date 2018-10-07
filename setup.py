from setuptools import setup
from setuptools import find_packages
setup(
    name='script006',
    version='0.0.1a',
    packages=find_packages('./src'),
    package_dir={'': 'src'},
    url='',
    license='',
    author='mkoshel',
    author_email='',
    description=''
)

# run me with python setup.py bdist_wheel