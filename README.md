# Ontometal

An OWL ontology metal music knowledge representation. Built on top of the [Music Ontology](http://purl.org/ontology/mo/), it models bands, releases, labels, genres and countries.

- **Ontology namespace**: https://w3id.org/ontometal
- **Documentation**: https://oceanberlinghieri.github.io/ontometal/
- **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Architecture

The ontology is divided in three builders which get structure and metadata from entities defined.

- Classes
- Data properties
- Object properties

All together generate the **TBOX** of the ontology: The schema layer — classes, properties, axioms and metadata.

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
ontometal
```
