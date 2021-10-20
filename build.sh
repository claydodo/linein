#!/bin/sh

rm dist/* -f

python3 -m build

VERSION=`cat setup.cfg | grep 'version = ' | grep -o '[0-9]*\.[0-9]*\.[0-9]*'`

twine upload dist/*${version}*
