import setuptools

setuptools.setup(
    name = 'sbwa',
    version='1.0.0',
    description='Index database sequences in the FASTA format.',
    author='Samuel Garcia',
    author_email='sag086@ucsd.edu',
    url='https://github.com/Samgarci17/CSE-185',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            'sbwa=sbwa.sbwa:main'
        ],
    },
)