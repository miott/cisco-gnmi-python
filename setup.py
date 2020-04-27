"""Derived from Flask
https://github.com/pallets/flask/blob/master/setup.py
"""

import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/cisco_gnmi/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="cisco_gnmi_miott",
    version=version,
    url="https://github.com/miott/cisco-gnmi-python.git",
    project_urls={
        "Code": "https://github.com/miott/cisco-gnmi-python.git",
        "Issue Tracker": "https://github.com/miott/cisco-gnmi-python.git/issues",
    },
    license="Apache License (2.0)",
    author="Cisco Innovation Edge",
    author_email="miott@cisco.com",
    maintainer="Cisco Innovation Edge/Michael Ott",
    maintainer_email="miott@cisco.com",
    description="This library forks gNMI functionality from https://github.com/cisco-ie/cisco-gnmi-python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Monitoring",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6, <4",
    install_requires=[
        "grpcio",
        "protobuf",
        "six",
        "cryptography",
    ],
    extras_require={
        "dev": [
            "grpcio-tools",
            "googleapis-common-protos",
            "pylint",
            "twine",
            "setuptools",
            "wheel",
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "coverage",
        ],
    },
)
