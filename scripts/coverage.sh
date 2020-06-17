#!/bin/bash
pipenv run coverage run -m unittest
pipenv run coverage report -m