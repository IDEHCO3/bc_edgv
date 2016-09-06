#!/bin/bash

cp nginx.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/module

service nginx restart

uwsgi --ini app-uwsgi.ini --uid root --gid www-data

