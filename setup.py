from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streambook",
    author="Alexander Rush",
    author_email="arush@cornell.edu",
    version="0.1.2",
    packages=[
        "streambook"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"streambook": []},
    setup_requires=["pytest-runner"],
    install_requires=["streamlit",
                      "jupytext",
                      "watchdog",
                      "in_place",
                      "mistune"],
    tests_require=["pytest"],
        python_requires='>=3.6',

)
