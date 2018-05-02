Identifier Distribution
=======================

There are 2048 different CAN Identifiers that can be used in a Standard CAN
Frame.  This specification describes uses for each of these ID's.  This section
describes what those uses are.

The distribution of CAN Identifiers is given in :numref:`distribution`.

.. tabularcolumns:: |L|L|C|

.. _distribution:
.. csv-table:: CAN-FIX Identifier Distribution
   :file: tables/distribution.csv
   :header-rows: 1

The *High Priority Node Alarms* group is a set of node specific identifiers that
should be used by individual nodes to send emergency data that is of the highest
priority.  The identifier that each node is to use is the same as it's own node
ID.  There are 255 IDs set aside for each of the possible 255 nodes that may be
on the network.  Since CAN does not allow two different devices to send data
with the same identifier we needed a way for individual nodes to send alarm data
about themselves.  The answer was to allocate the first 256 identifiers for this
purpose.  When a node alarm is received, the sending node would therefore be the
same as the identifier of the received frame.

This data will override all other data in the system so it should only be used
for data that is time critical.  Typically this data would be one-shot type of
information about a node that would not be continuously communicated and
therefore would need to override data that is continuously communicated.

The *Node Specific Messages* group occupies the last 256 identifiers.  These are
somewhat similar to the High Priority Node Alarms in that, the sending node
number can be inferred from the frame identifier.  All nodes on the network
should monitor all 256 of these ID's.  The first of these 1792 (0x700), is
reserved and the rest should be used by each individual node according to it's
own node ID.  Each node should add it's node ID to the beginning identifier to
determine which one it should use to send these messages.  Node 2 would use 1794
(0x702) to send these control messages or to respond to other nodes.

Node Specific Messages are typically used as commands to specific nodes.  They
are used to initiate communication on the Two-Way Communication Channels, send
configuration data, request specific information from a node, etc.  See the
frame definition section for more information.

The *Two-Way Communication Channels* Group contains 32 identifiers that
represent 16 channels.  These channels are set aside for nodes to set up two
way, stream type communications if needed.  Each node would send it's data on
the two different IDs.  The even numbered identifier is the requester's id and
the responder would use the following odd numbered identifier.  Once established
the type of data sent on the channel is arbitrary and would be defined by the
two nodes.  The channel identifiers are detailed in :numref:`channels`. If two nodes
decide to use channel 0 for some form of communication the requesting node would
use ID 1760 and the responding node would use ID 1761.  This continues for all
16 channels.

Some generic protocols for using these two-way communication mechanisms may be
described for general use but are not required by the specification.  One
obvious use is firmware upload/download.  Another is retrieval of historical log
data.

Care should be taken to assure that there are only two nodes using any given
channel at any given time.  Node Specific Messages are used for this purpose.

.. table_style: borderless

.. _channels:
.. csv-table:: Two-Way Communication Channel IDs
   :file: tables/channels.csv
   :header-rows: 1

The rest of the groups are normal data update identifiers.  Care should be taken
to assure that only one node on the network is producing any particular
parameter to avoid potential errors that would be generated if two different
nodes attempted to communicate the same data simultaneously.
