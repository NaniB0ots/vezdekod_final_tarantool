#!/bin/bash

sleep 6
gunicorn --bind 0.0.0.0:8081 wsgi:app
