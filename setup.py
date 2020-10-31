import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-license",
    version="1.0.0",
    author="", # Add author name
    author_email="", # Add author email
    description="API to easily license your services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ADI10HERO/easy-license",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
)
