# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "molepro-reasoner-api"
VERSION = "2.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.0.0",
    "swagger-ui-bundle==0.0.2",
    "python_dateutil==2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Systems Molecular Data Provider for NCATS Biomedical Translator Reasoners",
    author_email="translator@broadinstitute.org",
    url="",
    keywords=["OpenAPI", "Systems Molecular Data Provider for NCATS Biomedical Translator Reasoners"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Molecular Data Provider for NCATS Biomedical Translator Reasoners
    """
)

