setup(
    name='mypileup',
    version=1.0,
    description='CSE185 Demo Project',
    author='Samuel Garcia',
    author_email='sag086@ucsd.edu',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mypileup=mypileup.mypileup:main"
        ]
    }
)