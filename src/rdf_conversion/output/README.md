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