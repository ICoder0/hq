from setuptools import setup, find_packages
from platform import python_version_tuple


def requirements():
    with open('requirements.txt', 'r') as fileobj:
        requirements = [line.strip() for line in fileobj]

        version = python_version_tuple()

        if version[0] == 2 and version[1] == 6:
            requirements.append("argparse==1.4.0")
        if version[0] == 3:
            requirements.append("argparse==1.1")
        return requirements


def long_description():
    with open('README.md', 'rb') as fileobj:
        return fileobj.read().decode('utf8')


setup(
    name='hq',
    version='0.1.8',
    author='bofa1ex',
    url='https://github.com/ICoder0/hq',
    author_email='bofa1exx@gmail.com',
    description='HTML parser using Xpath expression then dump as json.',
    long_description=long_description(),
    packages=find_packages(),
    install_requires=requirements(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'hq=hq.hq:hq',
        ],
    }
)
