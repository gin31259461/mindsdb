# MindsDB for SQLPredictor

## Setup

install uv package manager

```bash
# create virtual environment
python -m venv .venv

# for linux
source .venv/bin/activate

# for windows
.\.venv/Scripts/Activate.ps1

# install
pip install -U pip
pip install -U setuptools wheel
pip install -U uv
```

install mindsdb with its local development dependencies

```bash
uv pip install -e .
uv pip install -r requirements/requirements-dev.txt
```

## Run

```bash
python -m mindsdb --config config.json
```
