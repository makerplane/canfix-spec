#!/bin/bash

./canfix_xml.py
./parameters.py

# TODO Run conversion script for SVG to PNG images

make latexpdf
make html
# This is a hack to get rid of :: in the HTML output for field lists
find _build/html/ -exec sed -i 's/::/:/g' {} \;
