import setuptools;

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hq',
    version='0.1.4',
    author='bofa1ex',
    url='https://github.com/ICoder0/hq',
    author_email='bofa1exx@gmail.com',
    description='HTML parser using Xpath expression then dump as json.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
         "setuptools",
         "lxml"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'hq=hq:hq',
        ]
    }
)
