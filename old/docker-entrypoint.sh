#!/bin/sh -ex

./projectname/manage.py migrate
./projectname/manage.py runserver 0.0.0.0:8080
