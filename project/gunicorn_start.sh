#!/bin/bash
#renunning
/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 run:app
