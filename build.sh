#!/bin/bash
cd /home/gxhut/ferriswheel/
git fetch
git reset --hard origin/main
chmod +x ./build.sh
python3 -m build
twine upload dist/*
chown -R gxhut /home/gxhut/ferriswheel
