from setuptools import setup, find_packages
from configparser import ConfigParser

config = ConfigParser()
config.read("config/ontology_config.ini")

setup(
    name="ontometal",
    version=config.get("ONTOMETAL", "VERSION"),
    description="Ontometal TBOX generator",
    author="Ocean Berlinghieri",
    author_email="berlinghieri10@gmail.com",
    url="https://github.com/oceanberlinghieri/ontometal",
    license="CC BY 4.0",
    # Package discovery
    packages=find_packages(include=["ontometal", "ontometal.*"]),
    package_dir={"": "."},
    # Python version requirement
    python_requires=">=3.10",
    entry_points={
        "console_scripts": "ontometal=ontometal.main:main",
    },
    # Dependencies
    install_requires=["rdflib>=7.0.0", "configparser>=5.0.0"],
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
)
