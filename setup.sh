#!/bin/bash
# Quick script to rename the template to a new name

if [ "$#" -ne 1 ]; then
    echo "Usage: setup.sh <new_project_name>"
    exit 1
fi

PROJECT_NAME=$1

sed -i '' -e "s/djangoherokutemplate/${PROJECT_NAME}/g" djangoherokutemplate/settings.py djangoherokutemplate/urls.py djangoherokutemplate/wsgi.py manage.py
mv djangoherokutemplate ${PROJECT_NAME}
