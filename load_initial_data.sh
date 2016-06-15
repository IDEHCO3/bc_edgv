#!/bin/bash

python manage.py loaddata hydra/fixtures/default.json
python manage.py loaddata context/fixtures/initial_data.json
python manage.py loaddata hydra/fixtures/initial_data.json

