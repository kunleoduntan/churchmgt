from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in churchmgt/__init__.py
from churchmgt import __version__ as version

setup(
	name="churchmgt",
	version=version,
	description="App for church management",
	author="kunleoduntan",
	author_email="kunleoduntan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
