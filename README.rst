 This is the Specification Document for the CAN-FIX communication protocol.

FIX is an acronym for Flight Information eXchange.  It is a set of protocol
specifications for exchanging information between aircraft avionics and flight
systems.  This specification and the protocols themselves are licensed under a
Creative Commons license that allows anyone to modify and redistribute these
documents without charge.

This is a community supported endeavor, with the primary goal of providing a
standard method for avionics and flight control systems to communicate with one
other in a vendor neutral way.

The specifications and protocols are primarily geared toward the Experimental
Amateur Built (E-AB) aircraft community.  Keeping the specification open and
free allows airplane builders to create their own devices and write their own
software that will be able to communicate with other devices without need to
pay for specifications or licenses.  It also encourages collaboration in the
development and improvement of the protocols themselves.

FIX is a protocol family.  This document will describe the CAN-FIX
implementation of the FIX protocol.  CAN-FIX is a CAN specific implementation
of the FIX protocol.

The specification documents are built with Sphinx.  The following shows how to
install the requirements on Ubuntu

sudo pip install pyexcel pyexcel-ods
sudo pip install sphinx
sudo apt install texlive-latex-base texlive-fonts-recommended
sudo apt install texlive-fonts-extra texlive-latex-extra
sudo apt install latexmk
