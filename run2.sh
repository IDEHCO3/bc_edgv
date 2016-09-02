#!/bin/bash

cp module.conf /etc/nginx/sites-available/
ls -s /etc/nginx/sites-available/module.conf /etc/nginx/sites-enabled/module

service nginx restart

uwsgi --ini app-uwsgi.ini --uid root --gid www-data

