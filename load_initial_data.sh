#!/bin/bash

python manage.py loaddata hydra/fixtures/default.json
python manage.py loaddata bcim/fixtures/context.json
python manage.py loaddata bcim/fixtures/hydra.json

