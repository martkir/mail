#!/bin/bash

CURR_WD=$(pwd)
PY_VENV_DIR="$CURR_WD/venv"

cd $CURR_WD || exit

echo "Activating Python environment..."
source "$PY_VENV_DIR/bin/activate"
echo "Environment $(which python) has been activated."

# $CURR_WD/config.json $CURR_WD/content.txt"
python "$CURR_WD/main.py"
