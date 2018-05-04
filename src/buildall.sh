#!/bin/bash

./canfix_xml.py
./parameters.py

# TODO Run conversion script for SVG to PNG images

make latexpdf
make html
