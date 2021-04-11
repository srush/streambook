from setuptools import setup

setup(
    name="streambook",
    version="0.1",
    packages=[
        "streambook"
    ],
    package_data={"streambook": []},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
