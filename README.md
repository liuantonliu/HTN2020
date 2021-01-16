# Hack the North - 2021
https://htn.azurewebsites.net

## Installation
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Start
```bash
$ flask run
```

## Deployment
```bash
az webapp up
```

## Logs
``` bash
az webapp log tail
```

## Tutorial
https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask
