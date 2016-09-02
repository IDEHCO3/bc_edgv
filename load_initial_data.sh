#!/bin/bash

python3 manage.py loaddata hydra/fixtures/default.json
python3 manage.py loaddata bcim/fixtures/context.json
python3 manage.py loaddata bcim/fixtures/hydra.json

