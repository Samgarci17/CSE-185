import os
from setuptools import setup, find_packages

curdir = os.path.abspath(os.path.dirname(__file__))
MAJ = 0
MIN = 0
REV = 0
VERSION = '%d.%d.%d' % (MAJ, MIN, REV)
with open(os.path.join(curdir, 'sbwa/version.py'), 'w') as fout:
    fout.write(
        "\n".join(["",
                "# THIS FILE IS GENERATED FROM SETUP.PY",
                "version = '{version}'",
                "__version__ = version"]).format(version=VERSION)
    )
setup(
    name = 'sbwa',
    version='1.0.0',
    description='Index database sequences in the FASTA format.',
    author='Samuel Garcia',
    author_email='sag086@ucsd.edu',
    url='https://github.com/Samgarci17/CSE-185',
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            'sbwa=sbwa.sbwa:main'
        ],
    },
)