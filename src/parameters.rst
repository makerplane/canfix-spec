.. _Parameters:

Parameters
==========

This section describes the individual parameter definitions.  Some parameters
are spread over multiple identifiers, to allow for multiple sources of the
information.  The best example of this is the engine data.  There is room for
two engines in this specification.  Every engine parameter is spread out over
two identifiers.  There are other times when multiple identifiers are used as
well.  There is room for multiple radios as well as multiple systems such as
fuel or electrical.

Basically anytime that it might make sense for more than one node to communicate
the same data (multiple radios or multiple engine monitors) then that data has
more than one identifier that can be used.  If there are multiple versions of
the data within a single node then that information will use the Index byte
within the data frame.  Waypoints and cylinder temperatures are common examples
of this.

This idea of using multiple identifiers and index bytes may be a bit confusing.
The reasoning lies in the CAN protocol itself.  It is an error if two different
nodes try to send a frame with the same identifier at the same time.  Because of
this if we are going to have multiple nodes trying to send the same type of
information we'd need multiple identifiers for each node.  This limits that
amount of information that we can transmit because there is a very finite number
of identifiers, so we added the idea of the indexing.

We have left room for two different engine monitoring nodes to exist on the
network and each one has a different set of identifiers for each of the engine
parameters.  There is nothing stopping the designer from having a single piece
of electronics measuring data for multiple engines.  In that case the different
identifiers can be used or the indexing.  As long as the receiving equipment
understands the distinction it doesn't matter.  Once there are multiple nodes,
then using the different identifiers becomes mandatory.  It is somewhat
confusing but it is also highly flexible.  We actually have room in this
protocol to measure 512 different exhaust gas temperatures on a single bus.  If
you need more than that you, can probably afford to run another network.

.. include:: parameter_list.rst
