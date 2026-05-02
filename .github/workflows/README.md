# CI/CD Pipeline

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
