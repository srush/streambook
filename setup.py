from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streambook",
    author="Alexander Rush",
    author_email="arush@cornell.edu",
    version="0.3",
    packages=["streambook"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"streambook": []},
    setup_requires=["pytest-runner"],
    install_requires=["streamlit", "jupytext", "watchdog", "in_place", "mistune", "typer"],
    tests_require=["pytest"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "streambook = streambook.cli:app",
        ],
    },
)
