#!/bin/bash
cd /home/gxhut/ferriswheel/
git fetch
git reset --hard origin/main
python3 -m build
twine upload dist/*
