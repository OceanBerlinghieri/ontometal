# How to run Jupyter Notebooks on vsCode

1. Install Extensions in VS Code

Install:

- Python
- Jupyter

2. Create / Activate Virtual Environment

```shell
python3 -m venv venv
source venv/bin/activate
```
4. Install Jupyter Kernel

With venv activated:
```shell
pip install ipykernel jupyter pandas numpy
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
```

6. Verify It Uses WSL Python

Run in a notebook cell:
```python
import sys
print(sys.executable)
```