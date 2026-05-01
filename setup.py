from setuptools import setup, find_packages

setup(
    name="ontometal",
    version="1.0.0",
    description="Ontometal ETL pipeline",
    author="Ocean Berlinghieri",
    author_email="berlinghieri10@gmail.com",
    url="https://github.com/oceanberlinghieri/ontometal",
    license="Apache 2.0",
    # Package discovery
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # Include non-Python files
    package_data={
        "": ["*.ttl", "*.rdfs", "*.csv", "*.xml"],
    },
    include_package_data=True,
    # Python version requirement
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "ontometal=etl.main:main",
            "conversion=rdf_conversion.main:main",
        ],
    },
    # Dependencies
    install_requires=[
        "pandas>=3.0.2",
        "rdflib>=7.0.0",
    ],
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
)
