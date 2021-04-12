from setuptools import setup
from streambook.version import __version__

setup(
    name="streambook",
    version=__version__,
    packages=[
        "streambook"
    ],
    package_data={"streambook": []},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
