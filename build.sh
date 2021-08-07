#!/bin/bash
cd /home/gxhut/ferriswheel/
git fetch
git reset --hard origin/main
python3 -m build
twine upload --config-file pypi-credentials.txt dist/*
chown -R gxhut /home/gxhut/ferriswheel
chmod +x build.sh
