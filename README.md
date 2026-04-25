# Ontometal

An OWL ontology and ETL pipeline for metal music knowledge representation. Built on top of the [Music Ontology](http://purl.org/ontology/mo/), it models bands, releases, labels, genres and countries using data extracted from [Metal Archives](https://www.metal-archives.com/).

- **Ontology namespace**: https://w3id.org/ontometal
- **Documentation**: https://oceanberlinghieri.github.io/ontometal/
- **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (ontology) / [Apache 2.0](LICENSE) (code)

# Running

## Prerequisites
- Python >= 3.10
- pip

## Install

### (Recommended) Create a virtual environment
```bash
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -e .
```

For development (tests, linting):
```bash
pip install -e ".[dev]"
```

## Execute
```bash
python -m src.etl.main
```