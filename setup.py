import glob
import os
from setuptools import setup

import textractplus

# get all of the scripts
scripts = glob.glob("bin/*")

# read in the description from README
with open("README.rst") as stream:
    long_description = stream.read()

github_url = 'https://github.com/VaibhavHaswani/textract-plus'


def parse_requirements(requirements_filename):
    """read in the dependencies from the requirements files
    """
    dependencies, dependency_links = [], []
    requirements_dir = os.path.dirname(requirements_filename)
    with open(requirements_filename, 'r') as stream:
        for line in stream:
            line = line.strip()
            if line.startswith("-r"):
                filename = os.path.join(requirements_dir, line[2:].strip())
                _dependencies, _dependency_links = parse_requirements(filename)
                dependencies.extend(_dependencies)
                dependency_links.extend(_dependency_links)
            elif line.startswith("http"):
                dependency_links.append(line)
            else:
                package = line.split('#')[0]
                if package:
                    dependencies.append(package)
    return dependencies, dependency_links


requirements_filename = os.path.join("requirements", "python")
dependencies, dependency_links = parse_requirements(requirements_filename)


setup(
    name=textractplus.__name__,
    version="0.1",
    description="A fork from textract with extended extension support and features. No more muss. No more fuss.",
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Vaibhav Haswani',
    author_email='vaibhavhaswani@gmail.com',
    keywords = ['TEXT EXTRACTION', 'TEXTRACT', 'DOCUMENT PARSING'],
    license='MIT',
    scripts=scripts,
    packages=[
        'textractplus',
        'textractplus.parsers',
    ],
    install_requires=dependencies,
    extras_require={
        "pocketsphinx": ["pocketsphinx==0.1.15"]
    },
    dependency_links=dependency_links,
    zip_safe=False,
)
