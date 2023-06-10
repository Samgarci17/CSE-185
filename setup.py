
from setuptools import setup, find_packages

setup(
    name = 'sbwa',
    version='0.0.2',
    description='Index database sequences in the FASTA format.',
    author='Samuel Garcia',
    author_email='sag086@ucsd.edu',
    url='https://github.com/Samgarci17/CSE-185',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            'index=sbwa.sbwa:main'
        ],
    },
)