#!/usr/bin/env python3

from setuptools import setup, find_packages

# package names should be camel case, according to [http://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/creation.html]
setup(name='AutomaticAPI',
	version="0.1",
	description="",
	author="Rehan Khwaja",
	author_email="rehan@khwaja.name",
	url="",
	packages=find_packages(),
	requires=["requests", "requests_oauthlib"]
	)
