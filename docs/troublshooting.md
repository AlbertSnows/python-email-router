# Troubleshooting Guide

A place to store Problem->Solution combos as I do dev work.

## ModuleNotFoundError: No module named 'flaskr'

<https://flask.palletsprojects.com/en/2.3.x/tutorial/install/>

`pip install -e .`

Note: this seems to cause issue with the docker build so have to remove? Double check...

## Docker isn't picking up changes in filesystem

`docker-compose up --build`
