# FastAPI - API

## Table of content

- [FastAPI - API](#fastapi---api)
  - [Table of content](#table-of-content)
  - [Development](#development)
    - [Prerequisites](#prerequisites)
    - [Run instructions](#run-instructions)
  
## Development

### Prerequisites

- Python v3.9.12

### Run instructions

- Create a virtual environment and install dependencies

```sh
cd api
pip install virtualenv
virtualenv ./env
source env/bin/activate
pip install -r requirements.txt
```

- Load env variables

```sh
# For windows
set -a && source .env && set +a

# For linux
source .env
```

- Start the server

```sh
python src/main.py
```

- Lint src dir

```sh
flake8 src
```
