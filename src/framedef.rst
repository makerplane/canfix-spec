Frame Definitions
=================

The 11 bit identifier field within the CAN-Frame is used to identify what type
of frame we are sending.  The CAN frame gives us up to 8 bytes of data for each
frame type.  There are several frame formats given for different types of
messages.

Node Alarm Data Field Format
----------------------------
.. tabularcolumns:: |p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|

.. _alarmframe:
.. csv-table:: Node Alarm Byte Definitions
   :file: tables/alarmframe.csv
   :header-rows: 1
