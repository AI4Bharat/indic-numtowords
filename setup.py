from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="indic_numtowords",
    version='1.0.1',
    description="A module to convert numbers to words for Indian languages and English.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AI4Bharat/indic-numtowords",
    project_urls={
        'Source Code': 'https://github.com/AI4Bharat/indic-numtowords',
        'Report Issues': 'https://github.com/AI4Bharat/indic-numtowords/issues',
    },
    author="AI4Bhārat",
    author_email="opensource@ai4bharat.org",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries"
    ],
)