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

If the identifier is in the High Priority Node Alarm Group (identifiers 1-255),
The Node Alarm Frame is sent 03

The first two bytes represent a 16 bit identifier for alarm codes.  The rest are
six bytes of data that can be communicated with each of these alarm codes if
needed.  The meaning of these alarm codes is not given by this specification.
The sending node is inferred by the actual CAN identifier on which, the message
was sent.

Normal Data Field Format
------------------------
.. tabularcolumns:: |p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|

.. _dataframe:
.. csv-table:: Normal Data Field Format
  :file: tables/dataframe.csv
  :header-rows: 1

Node identifiers from 256 to 1759 indicate a normal parameter data update.
These are the heart and soul of the protocol.  The vast majority of the
information transmitted on the bus should be normal parameter updates.

The first data byte is the node number of the node that is generating the data.
Node numbers should be unique on any given CANFIX network.

The second byte of the data field is the index.  The index allows us to
communicate more than one instance of a particular parameter.  For example, the
Exhaust Gas Temperature is indexed for each cylinder.  The first cylinder is
given with 0x00 and the next with 0x01 etc.  If a parameter does not need to be
indexed (Airspeed, Altitude, etc), the index would simply be zero.

The third byte is the Function / Status (FS) code.  The main use of this field
is to allow us to communicate meta data that is associated with the parameter
and to indicate the quality of that data.  Many parameters have normal operating
ranges that need to be defined and communicated.  This is done with meta data.
This meta data can be used by display equipment to scale the range on indicators
and to show the normal operating ranges

.. tabularcolumns:: |p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|

.. _functioncode:
.. csv-table:: Function / Status Code Bit Definitions
  :file: tables/functioncod.csv
  :header-rows: 1

The Function / Status Code is designed so that if the byte has a value of zero,
it indicates that the message being sent is nothing more than a parameter value
update of good quality.  This is the most common type of message in the system
so it makes sense to keep it simple for receivers to quickly determine that
there is nothing unusual going on.

The lowest order bit in the FS Code is the Annunciate bit.  If this bit is set
to 1, the data that is being transmitted is considered out of range and should
be annunciated.  What determines the parameter being out of range depends upon
the parameter.  More often than not it would be that an alarm set point has been
exceeded.  An oil pressure dropping below a certain threshold would be an
example.

The Quality bit indicates whether the sender believes the data is good or not.
If this bit is set then the value given should be flagged in some way.  The
value may still be displayed but some indication should be given to the pilot
that the value is untrusted.  Think of this like the flag on an attitude
indicator.

The Failure bit is an indication that the sender knows that this data is bad.
The data should not be shown to the pilot and the failure should be indicated.

If either the Quality bit or Failure bit is high, an alternate means of
retrieving this data should be used if available.

The four Meta Data bits give us the ability to assign 15 different values to a
particular parameter that could be some kind of configuration information, alarm
thresholds, or scaling.  Even a combination of any of these.  There are only 15
available because zero indicates the actual parameter itself.

Examples of meta data could include V-speeds for airspeed indications, it could
be the low and high oil pressure set points.  The definition of these depends on
the parameter itself.  Some parameters will have no meta data associated with
them.  Others may need more than 15 and will have to use some of the user
defined node configuration messages to take care of them.

Meta data shares the same range, units and data type as the parameter itself.
Meta data is not meant to multiplex other related types of data into a single
parameter.  It's designed to allow configuration of points that are directly
related to the parameter, such as ranges and set points.  If you find yourself
wishing that the meta data point used a different data type then you are
misusing the meta data.

The last five bytes of data in the Normal Data Message refer to the actual
informational data that is being transmitted.  One or all five of these data
bytes may be used depending on the parameter being transmitted.  Data is sent in
little endian order.  This means that the least significant byte is sent first.

Node Specific Message Data Field Format
---------------------------------------

.. tabularcolumns:: |p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|

.. _fnodespecificframe:
.. csv-table:: Node Specific Message Data Field Format
  :file: tables/nodespecificframe.csv
  :header-rows: 1

Node Specific message frames are sent with identifiers 1792 thru 2047.  These
are the last 256 CAN identifiers.

The Node Specific Message format is simple.  The first byte is the destination
node.  The source node ID is inferred by the identifier on which the message was
transmitted.  Zero can be sent as the destination node to effect all nodes.
Whether the node is allowed to respond to this broadcast address depends on the
what type of message it is.

The Control Code indicates what type of message this is.  Table 3.5 shows the
different Control Codes that can be used.

.. tabularcolumns:: |c|l|c|c|

.. _nodecontrolcode:
.. csv-table:: Node Specific Message Data Field Format
  :file: tables/nodecontrolcode.csv
  :header-rows: 1

Node Identification Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Node Identification message is sent to a node to request information about
the node.
