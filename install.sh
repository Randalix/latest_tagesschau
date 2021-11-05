#!/usr/bin/env sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" >/dev/null 2>&1 && pwd  )"
sudo cp $DIR/tagesschau.py /usr/bin/tagesschau
pip install -r $DIR/requirements.txt

