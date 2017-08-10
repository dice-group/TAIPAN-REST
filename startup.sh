#!/bin/bash

pip install -e /foxpy
pip install -e /agdistispy
pip install -e /taipan-lib

python /taipanserver/run.py
