#!/bin/bash

pytest --cov-config=.coveragerc --junitxml=./junit_report.xml  --cov=../ test_utils.py

coverage xml -o ./coverage_report.xml