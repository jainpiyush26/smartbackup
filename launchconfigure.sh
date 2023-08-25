#!/usr/bin/env sh

PACKAGE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [[ -z "${PYTHONPATH}" ]]; then
    export PYTHONPATH="$PACKAGE_DIR/python"
else
    export PYTHONPATH="${PYTHONPATH};$PACKAGE_DIR/python"
fi


python $PACKAGE_DIR/bin/configuresmartbackup