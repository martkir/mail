#!/bin/bash

CURR_WD=$(pwd)
PY_VENV_DIR="$CURR_WD/venv"

cd $CURR_WD || exit

python3 -m venv venv

echo "Activating Python environment..."
source "$PY_VENV_DIR/bin/activate"
echo "Environment $(which python) has been activated."

pip install -r requirements.txt




