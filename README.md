# MindsDB for SQLPredictor

## Setup

install uv package manager

```bash
# create virtual environment
python -m venv .venv

# activate environment

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

activate environment again!!

## Run

```bash
python -m mindsdb --config config.json --no_studio
```

## Run MindsDB in Docker

<!-- markdownlint-disable MD013 -->

```bash
docker pull mindsdb/mindsdb:v24.10.3.0

docker run --name sqlpredictor -v mdb_data:/root -p 47334:47334 -p 47335:47335 -p 47336:47336  mindsdb/mindsdb:v24.10.3.0 
```
