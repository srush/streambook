from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streambook",
    author="Alexander Rush",
    author_email="arush@cornell.edu",
    version="0.4a1",
    packages=["streambook"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"streambook": []},
    setup_requires=["pytest-runner"],
    install_requires=[
        # Pin streamlit versions because some APIs used are internal
        "streamlit~=1.15",
        "jupytext~=1.14",
        "watchdog~=2.1",
        "in-place~=0.5",
        "mistune~=2.0",
        "typer~=0.7",
    ],
    extras_require={
        "dev": [
            "pip-tools~=6.11",
            "pytest~=7.2",
        ]
    },
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "streambook = streambook.cli:app",
        ],
    },
)
