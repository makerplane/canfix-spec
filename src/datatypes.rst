.. _Data Types:

Data Types
==========

The data type for each parameter depends on the definition of the parameter.
The data type is constant for each parameter.  There is no method to indicate
the data type within the message itself and this is by design.  It makes
implementation easier.  Floating point numbers are avoided if possible and fixed
point integers are preferred.  This is to make the protocol simple for small 8
bit micro-controllers.  This is CAN after all and it was designed to be simple
for use in small embedded applications and we will avoid complexity where
possible to make it easy to build small, inexpensive devices that are compatible
with this protocol.  The data types are listed in :numref:`datatypes`.

.. tabularcolumns:: |c|l|c|c|

.. _datatypes:
.. csv-table:: Data Types
  :file: tables/datatypes.csv
  :header-rows: 1

The ``BYTE`` data type typically means 8 bits.  These are usually used to indicate
discrete states such as, switch positions, status or commands.  The WORD data
type is similar but it's 16 bits.

The ``FLOAT`` data type is an *IEEE 754* Floating point number.

If 64 bit floating point precision is needed then the number will have to be
sent in two messages.  How this is done, will be detailed for each parameter in
which it is needed.  Thus far this has not been found necessary.

A parameter may also be sent as an array of data.  For example time is sent as
three ``USHORTs``, one for hours, minutes and seconds.  Any combination of these
five bytes may be used for the data and the data type may be mixed.  A date
could be given as ``UINT``, ``USHORT[2]``.  The ``UINT`` is for the year (we
don't want any Y2K stuff here) and the USHORTS are for month and day.

It is very common in this specification to use integers with assumed decimal
places in lieu of using floating point numbers.  Be sure to check the individual
parameter definitions for details.
