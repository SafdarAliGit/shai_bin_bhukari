from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shai_bin_bhukari/__init__.py
from shai_bin_bhukari import __version__ as version

setup(
	name="shai_bin_bhukari",
	version=version,
	description="this is shai_bin_bhukari",
	author="portal",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
