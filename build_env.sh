#!/bin/bash
echo $0: Creating virtual environment
virtualenv --prompt="<library>" ./env

mkdir ./logs
mkdir ./db

echo $0: Installing dependencies
source ./env/bin/activate
export PIP_REQUIRE_VIRTUALENV=true
./env/bin/pip install --requirement=./requirements.conf --log=./logs/build_pip_packages.log

echo $0: Making virtual environment relocatable
virtualenv --relocatable ./env

echo $0: Creating virtual environment finished.

echo $0: Creating database './db/library.db'
sqlite3 ./db/library.db < schema.sql
echo $0: Creating database finished
