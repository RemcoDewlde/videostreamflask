#!/bin/bash

python3.7 -m unittest tests/test_main.py
coverage report main.py camera.py
coverage html main.py camera.py
cd htmlcov
open ./index.html
