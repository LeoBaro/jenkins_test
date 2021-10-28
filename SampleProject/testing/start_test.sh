#!/bin/bash

environment=$1

source environment/bin/activate

pytest --cov-config=.coveragerc --junitxml=./junit_report.xml  --cov=../ test_utils.py

coverage xml -o ./coverage_report.xml