# Ontometal

An OWL ontology and ETL pipeline for metal music knowledge representation. Built on top of the [Music Ontology](http://purl.org/ontology/mo/), it models bands, releases, labels, genres and countries using data extracted from [Metal Archives](https://www.metal-archives.com/).

- **Ontology namespace**: https://w3id.org/ontometal
- **Documentation**: https://oceanberlinghieri.github.io/ontometal/
- **License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (ontology) / [Apache 2.0](LICENSE) (code)

## Architecture

The ontology is split into two layers following standard ontology engineering practice:

- **TBox (Terminological Box)**: The schema layer — classes, properties, axioms and metadata. Maintained manually in `ontology/ontometal_skeleton.ttl`.
- **ABox (Assertional Box)**: The instance layer — individuals and their property assertions (countries, genres, bands, labels, releases). Generated automatically from normalized CSV data.

The RDF conversion pipeline follows a **full-rebuild ETL** pattern:

1. **Extract** — Read normalized CSVs via repository classes.
2. **Transform** — Converter classes map each row to RDF triples using rdflib.
3. **Load** — The skeleton TBox is loaded, ABox triples are added, and the combined graph is serialized to `src/rdf_conversion/output/ontometal.ttl`.

Because `rdflib.Graph` is a set of triples, the pipeline is idempotent — running it multiple times with the same data produces the same output. Since the graph is rebuilt from the skeleton on each run, removed source data is also reflected in the output.

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

# Storing TTL file
The generated ontology file (`ontometal.ttl`) is stored using [Git LFS](https://git-lfs.github.com/) due to its size (~130MB).

```bash
sudo apt-get update && sudo apt-get install -y git-lfs
git lfs install
git lfs track "*.ttl"
```

If the TTL file already exists in commit history, migrate it:
```bash
git lfs migrate import --include="*.ttl" --include-ref=<branch>
```

## CI/CD Pipeline

The CI/CD pipeline runs on `feature/*` and `release/*` branches:

1. **Generate** — Rebuilds the ontology from normalized CSVs (`python -m src.rdf_conversion.main`)
2. **Validate** — Runs the [Robot](https://robot.obolibrary.org/) tool with the HermiT reasoner to check ontology consistency
3. **Commit** — Pushes the generated TTL file (via Git LFS) to the branch

The `develop` and `master` branches inherit the TTL file through pull request merges:

```
feature/* (generates TTL) → PR → develop (inherits TTL) → release/* (regenerates TTL) → PR → master (inherits TTL)
```

The ontology is always validated before reaching `develop` or `master`.
https://git-lfs.com/

