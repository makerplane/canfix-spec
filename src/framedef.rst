.. _Frame Definitions:

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

If the identifier of a received frame is in the *High Priority Node Alarm Group*
(identifiers 1-255), then we have received a Node Alarm from the node whose ID
matches the frame identifier itself.

The first two bytes represent a 16 bit identifier for alarm code.  The meaning
of these alarm codes is not given by this specification.  The remaining six
bytes of data may be used to further describe the alarm.  These are also not
defined by this specification.

These are the highest priority messages on the network.  Care should be taken to
ensure that these messages are not allowed to saturate the network. Think of
these alarms as real time notifications that need to arrive at the destination
node within a few milliseconds.  Perhaps to coordinate the fail-over of a
redundant fly by wire servo or some other electronic failure.  If the goal is to
annunciate a low pressure or a high temperature to the pilot, these are NOT the
messages to use.

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

The first data byte is the *Node ID* of the node that is generating the data.
Node IDs should be unique on any given CANFIX network.

The second byte of the data field is the *Index*.  The index allows us to
communicate more than one instance of a particular parameter.  For example, the
Exhaust Gas Temperature is indexed for each cylinder.  The first cylinder is
given with 0x00 and the next with 0x01 etc.  If a parameter does not need to be
indexed (Airspeed, Altitude, etc), the index would simply be zero.

The third byte is the *Function / Status Code*.  The main use of this field
is to allow us to communicate meta data that is associated with the parameter
and to indicate the quality of that data.  Many parameters have normal operating
ranges that need to be defined and communicated.  This is done with meta data.
This meta data can be used by display equipment to scale the range on indicators
and to show the normal operating ranges

.. tabularcolumns:: |p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|

.. _functioncode:
.. csv-table:: Function / Status Code Bit Definitions
  :file: tables/functioncode.csv
  :header-rows: 1

The *Function / Status Code* is designed so that if the byte has a value of zero,
it indicates that the message being sent is nothing more than a parameter value
update of good quality.  This is the most common type of message in the system
so it makes sense to keep it simple for receivers to quickly determine that
there is nothing unusual going on.

The lowest order bit in the *Function Status Code* is the *Annunciate* bit.  If
this bit is set to 1, the data that is being transmitted is considered out of
range and should be annunciated.  What determines the parameter being out of
range depends upon the parameter.  More often than not it would be that an alarm
set point has been exceeded.  An oil pressure dropping below a certain threshold
would be an example.

The *Quality* bit indicates whether the sender believes the data is good or not.
If this bit is set then the value given should be flagged in some way.  The
value may still be displayed but some indication should be given to the pilot
that the value is untrusted.  Think of this like the flag on an attitude
indicator.  If the temperature of an electronic device is outside of it's
published specifications it would make sense for the Quality flag to be set.
That device may still be giving useful information but it's out of spec and
should be suspect.

The *Failure* bit is an indication that the sender knows that this data is bad.
The data should not be shown to the pilot and the failure should be indicated. A
pressure sensor that stops communicating to the microcontroller in the node
would be a way to know that the data has failed.  Other more sophisticated
methods could be used to determine failure of the data as well such as
measurement redundancy built into the device.  These details are left up to the
node designer.

If either the *Quality* bit or *Failure* bit is high, an alternate means of
retrieving this data should be used if available.

The four *Meta Data* bits give us the ability to assign 15 different values to a
particular parameter that could be some kind of configuration information, alarm
thresholds, or scaling.  Even a combination of any of these.  There are only 15
available because zero indicates the actual parameter itself.

Examples of meta data could include V-speeds for airspeed indications, it could
be the low and high oil pressure set points.  The definition of these depends on
the parameter itself.  Some parameters will have no meta data associated with
them.  Others may use all 15.

Meta data shares the same range, units and data type as the parameter itself.
Meta data is not meant to multiplex other related types of data into a single
parameter.  It's designed to allow configuration of points that are directly
related to the parameter, such as ranges and set points.  If you find yourself
wishing that the meta data had a different data type or range then you are
misusing the meta data.

The last five bytes of data in the Normal Data Message refer to the actual
value that is being transmitted.  One or all five of these data
bytes may be used depending on the parameter being transmitted.  Data is sent in
little endian order.  This means that the least significant byte is sent first.

See the :ref:`Data Types` chapter for information on how this data is to be
encoded.

Node Specific Message Data Field Format
---------------------------------------

.. tabularcolumns:: |p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|

.. _nodespecificframe:
.. csv-table:: Node Specific Message Data Field Format
  :file: tables/nodespecificframe.csv
  :header-rows: 1

*Node Specific Message* frames are sent with identifiers 1792 thru 2047.  These
are the last 256 CAN identifiers.

The *Node Specific Message* format is simple.  The source node ID is inferred by the identifier on which the message was
transmitted by the following formula.

  Frame ID - 1792 = Node ID

The first byte is the destination
node. Zero can be sent as the destination node to effect all nodes.
Whether the node is allowed to respond to this broadcast address depends on the
what type of message it is.

The *Control Code* indicates what type of message this is.  Table 3.5 shows the
different Control Codes that can be used.

.. tabularcolumns:: |c|l|c|c|

.. _nodecontrolcode:
.. csv-table:: Node Specific Message Data Field Format
  :file: tables/nodecontrolcode.csv
  :header-rows: 1

.. _Node Identification:

Node Identification Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *Node Identification* message is sent to a node to request information about
the node.

.. tabularcolumns:: |c|l|l|

.. _nodeidresponse:
.. csv-table:: Node Identification Command Response
  :file: tables/nodeidresponse.csv
  :header-rows: 1

Each node should respond to the *Node Identification* message with the
specification that it is using to send the data.  For this specification the
number is 0x01.  The rest of the data is optional but should be padded with
zeros for simplicity if not used.  Mostly this would be used by configuration
software to determine which types of devices were attached to the network and
what their node numbers were.  Obviously it would be advantageous if every node
created would send a unique response to this command.  It might be useful to
have a central database of device types and model numbers.  It has little use
during flight so if there are nodes on the network that have identical
identifications it won't cause any problems with the network.

Bit Rate Set Command
~~~~~~~~~~~~~~~~~~~~

The *Bit Rate* Set message requests that the node change it's CAN Bit Rate to
the given setting.  The change should take place immediately and therefore no
response is possible, unless there is an error.  The change should be permanent.

This message can be sent to Node Id 0 to affect all the nodes on the network at
the same time.

.. tabularcolumns:: |c|l|l|

.. _bitrate:
.. csv-table:: Bit Rate Set Command Response
  :file: tables/bitrate.csv
  :header-rows: 1

Bit rates given in byte two of the request frame should be one of the follwoing...

  | 1 = 125kbs
  | 2 = 250kbs
  | 3 = 500kbs
  | 4 = 1Mbs

Node ID Set Command
~~~~~~~~~~~~~~~~~~~

The *Node ID Set* message is used to command the node to change it's node ID.
This change should take place immediately and permanently at the time of
receiving this message.  The node should transmit it's success message on the
CAN ID that is based on it's new node ID.

.. tabularcolumns:: |c|l|l|

.. _nodeidset:
.. csv-table:: Node ID Set Command Response
  :file: tables/nodeidset.csv
  :header-rows: 1

Disable / Enable Parameter Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *Disable and Enable Parameter* messages are used to command a node to start
or stop broadcasting a particular parameter.  There may be multiple nodes that
report the same parameter and this allows a mechanism to force one node to stop
sending that parameter or to re-enable that node to resume sending that
parameter.  A fairly elaborate redundancy scheme could be generated using these
messages but that is outside the scope of this document.  This would more often
be used as an initial configuration and setup message.

The change should be immediate and permanent.

.. tabularcolumns:: |c|l|l|

.. _disableenable:
.. csv-table:: Disable / Enable Parameter Comamnd Response
  :file: tables/disableenable.csv
  :header-rows: 1

Node Report Command
~~~~~~~~~~~~~~~~~~~

The *Node Report* message is sent to force a node to report every parameter that
it is responsible for.  There is no data associated with this command.  Once the
node receives this message it should immediately begin sending each type of
parameter that it would send under normal circumstances.  This would normally be
used by flight display equipment to determine the information that is available
on the network and also what conflicts there may be.  If a parameter has been
disabled by the disable parameter command it should not be sent after a node
report to avoid possible conflicts on the network.

The node should also send the meta data associated with each parameter if
applicable. This gives display equipment all the information that it will need
to properly display the information.  Node Report commands should be avoided
during flight unless absolutely necessary.

There is no other response to this command.

Node Status Information
~~~~~~~~~~~~~~~~~~~~~~~

.. tabularcolumns:: |c|l|

.. _nodestatus:
.. csv-table:: Node Status Message
  :file: tables/nodestatus.csv
  :header-rows: 1

The *Node Status Information* message is a way for individual nodes to send
information about themselves directly to other nodes.  This information is
specific to the node and not necessarily specific to the aircraft.  Information
like internal temperature, communication status, error counters, etc. would fall
under this type of message.  There is no response necessary since this
information is more like normal parameter updates and is simply produced on the
network for any device to consume.  Care should be taken not to saturate the
network with this type of information.

The message contains 16 bits of parameter type ID in the first two bytes and
the following four bytes are for the data.

.. tabularcolumns:: |c|p{6cm}|c|c|

.. _statusparameters:
.. csv-table:: Node Status Parameter ID Definitions
  :file: tables/statusparameters.csv
  :header-rows: 1

:numref:`statusparameters` shows the parameters that are called out by
this specification.  This message is not mandatory.

Update Firmware Command
~~~~~~~~~~~~~~~~~~~~~~~

This command informs the node to open a connection on the given channel and
prepare to receive new firmware.  This command is optional and the method for
updating firmware is implementation specific and is not specified in this
document.

The *Verification Code* can be used by the node to make sure that the firmware
is going to be sent by a node that understands the proper way to update firmware
to this device.  This is simply a unique number that is agreed upon by the node
and the device used to download the firmware.

Before sending this command a node should listen on the prospective channel for
at least 500 ms to determine that the channel is not being used.  If it is being
used another channel should be selected.  Once the communication is established
on this channel data must be sent on this channel at least once every 250 ms so
that other nodes can determine whether or not the channel is being used.

.. tabularcolumns:: |c|l|l|

.. _firmware:
.. csv-table:: Update Firmware Command Response
  :file: tables/firmware.csv
  :header-rows: 1

Two-way Connection Request Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After this message is sent and the response is successful the two nodes will
begin communicating on the given channel.  Before sending this command a node
should listen on the prospective channel for at least 500 ms to determine that
the channel is not being used.  It is the senders responsibility to determine if
other nodes are using this channel.  If it is being used, another channel should
be selected. Once the communication is established on this channel data must be
sent at least once every 250 ms so that other nodes can determine whether or the
channel is being used.

Because these are such low priority CAN bus ID's it is possible on busy networks
that the 250ms requirement is impossible to meet.  For that reason, this should
not be considered a robust communication mechanism and should not be used for
flight critical data unless special precautions are taken to assure that there
is enough room on the network to accommodate the data and that the integrity of
the data is sound.

.. tabularcolumns:: |c|l|l|

.. _channel:
.. csv-table:: Two-Way Communication Request Command Resposne
  :file: tables/channel.csv
  :header-rows: 1

Node Configuration Command
~~~~~~~~~~~~~~~~~~~~~~~~~~

The *Node Configuration* command is used to set configuration parameters within
each node.  Typically this would be used as an initial setup and is done in a
key / value type of arrangement.  What these keys and values represent are
specific to each node and not specified in this document.

There may be a specification generated in the future that describes a mechanism
to identify configuration parameters that can be set for each type of node.
This would probably be some kind of XML document that would describe the
different types of information that could be set for each node.  This would
allow for a common piece of software to be used to set configuration parameters
for all devices.

.. tabularcolumns:: |c|l|l|

.. _configuration:
.. csv-table:: Node Configuration Command Response
  :file: tables/configuration.csv
  :header-rows: 1

Error Codes
  | 1 = Unknown Parameter
  | 2 = Parameter is Read Only
  | 3 = Data Out of Range
  | 4 = Wrong Data Type

Node Configuration Query Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a method that a sending node can use to query configuration parameters
that are stored in the destination node.  It's up to each node to understand
what format the data takes.

.. tabularcolumns:: |c|l|l|l|

.. _configquery:
.. csv-table:: Node Configuration Query Command Response
  :file: tables/configquery.csv
  :header-rows: 1

Parameter Set Command
~~~~~~~~~~~~~~~~~~~~~

The *Parameter Set Command* is used to give nodes a more point-to-point way of
setting parameters. The *Normal Data Field Format* is used to broadcast
(produce) data on the network for all nodes to consume. Sometimes it becomes
necessary for a specific node to send one of these parameters to another node to
**Set** that parameter. A common example would be the frequency in a
communication radio.  There is room in the specification for up to four radios.
Each would report the  current frequency at which they are set (also standby and
memory frequencies as well).  There could be several devices in the aircraft
that would be tasked with setting those frequencies.  Navigation equipement
could be configured to change the frequency based on the airport that is
selected, the EFIS could be programmed or a purpose built display "Head" might
all want to be able to set the frequency.  Without this mechanism an individual
CAN Frame Identifier would have to be allocated for each of these different
devices to send frequencies to each device [#f1]_.

Other uses for this mechanism are the Barometric Altimeter Setting and
navigational waypoints.

.. _parameterset:
.. csv-table:: Parameter Set Command
  :file: tables/parameterset.csv
  :header-rows: 1

.. _parameterbits:
.. table:: Parameter ID Bit Descripitons

  +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
  | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
  +====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+
  | Parameter Identifier                                 | Index                  |
  +------------------------------------------------------+------------------------+

The first two bytes of the message are a 16 bit number that describes the
parameter that is to be set.  The lower 11 bits match the actual parameter ID
given in the :ref:`Parameters` Chapter.  The remaining 5 bits are the index that
we are changing.

There are a couple of drawbacks to this mechansim.  The first is that we only
have four bytes left over for the payload to the parameter.  The paramters
themselves have 5.  Since very few parameters in this specification need more
than four bytes this seemed acceptable.  Those that do require all five
bytes don't seem like the type of information that would need to be set in
flight.

Another drawback is that with 5 bits for the index we are unable to set all of
the indexed information that could exist in a node.  This trade off seemed
reasonable as setting more than 32 frequencies or waypoints.

This is a mechanism for setting parameters in flight.  It's not meant to be a
way to set configuration information.  Meta data is not included in this
mechanism.  Changing the low oil pressure set point is better left to
configuration software while we are on the ground.

Node Description
~~~~~~~~~~~~~~~~

The *Node Description* message is here to allow a node to produce detailed information about
itself.  This information is in the form of a NULL terminated string that
is passed four ASCII characters at a time.

.. _nodedescription:
.. csv-table:: Node Description Message
  :file: tables/nodedescription.csv
  :header-rows: 1

The first two bytes of the payload are the *Packet Number*.  The string is
broken up into four byte "Packets."  This 16bit number identifies which of those
packets we are sending. A string of up to 256K characters can be sent using this
mechanism.  The packets should be sent in order starting with Packet Number = 0
and the end of the sring is designated by the NULL (0x00) character.  The
remaining bytes in the message should be padded with 0x00 to simplify decoding.

Typical use of this message is to send detailed information about the particular
node such as Manufacturer name, Model Description, Serial Number, License terms,
firmware revision date of manufacture etc.

Here is an example...

  ``MakerPlane EFIS v1.0.1 SN 180612345 Firmware v1.2.3.4-Jun 2018 GPL 2.0``

If implemented this string should be sent as a follow up reponse to the :ref:`Node
Identification` request.

.. rubric::Footnotes

.. [#f1] In fact this was the case in previous versions of this specification and it proved to be clumsy and unworkable.
