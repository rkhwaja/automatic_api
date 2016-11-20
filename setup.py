#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.rst") as f:
	long_description = f.read()

# package names should be camel case, according to [http://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/creation.html]
setup(name='AutomaticAPI',
	version="0.2",
	description="Python support for the Automatic API which is documented at https://developer.automatic.com/documentation/",
	long_description=long_description,
	author="Rehan Khwaja",
	author_email="rehan@khwaja.name",
	url="https://github.com/rkhwaja/automatic_api",
	packages=find_packages(),
	install_requires=["requests", "requests_oauthlib"],
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3.5"
	],
	keywords="",
)
