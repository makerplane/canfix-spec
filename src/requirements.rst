.. _Requirements:

General Requirements
====================

To be compliant with this specification, devices should meet some minimum level
of functionality.  The implementation of most of this specification is optional.
However, if any given part of the specification is implemented, the device is
expected to behave according to the descriptions in this document.

This section describes the minimum functionality that must be present for a
device to be considered compliant with this specification.  The requirements for
this specification have been deliberately kept to a minimum to make
implementation of this specification as easy as possible.


Communication Requirements
--------------------------

There are several *Node Specific Messages* that the device must respond to.
They are...

  * Node Identification
  * Bit Rate Set
  * Node ID Set
  * Disable Parameter
  * Enable Parameter
  * Node Report

All nodes should respond to the Node Identification command even if the only thing
they return is the specification number.

It is not required that a device send any parameters listed by the
specification.  The device must  however, respond to a Disable or an Enable
Parameter message.  If there are no parameters to disable or enable the device
can simply respond with an *Unknown Parameter* error.

If a device has no parameters to send it is not required to follow a Node Report
request with any data.

Data types cannot be substituted.  If parameters are sent by a device they must
match the data types given in this document.

Bit rate, node ID number and the parameters that have been enabled or disabled
should be stored in non-volatile memory so that these changes are permanent
unless changed by these commands again.

A device should send at least one self identifying frame on the CAN bus at least
once every 2 seconds to indicate it's health to the system.  Any frame that has
the devices node number implied will satisfy this requirement.  The only message
types that do not include the sender's node number are the two-way
channel communication frames, these would NOT satisfy this requirement.

The recommendation is to send a Node Status Information message with the status
word set to 0x0000 to indicate good health once per second.

125 kbps and 250 kbps are the only two bit rates that are mandatory.

Physical Requirements
---------------------

There are really no mandatory physical specifications that must be met.  There
are electrical connectors that are specified and if these types of connectors
are used the signals on the pins must match the descriptions in this
specification.

Good engineering practices should be used in the design of these devices.
A complete description is outside the scope of this document, however here is
a short list of issues to pay attention to.

  * Wires should be properly supported
  * Mounting should be secure and fasteners should be protected from loosening
    due to vibration
  * Connectors should be postively retained.  Friction is not a proper
    retention method.
  * Components should be properly cooled
  * Materials used for construction should not emit noxious fumes if burned.
    Aluminum is a great choice for enclosures, PVC is a terrible choice.

Electrical Requirements
-----------------------

The device should operate properly with supply voltages between 10 and 32 Volts
DC.

The device should be able to withstand reversed polarity connection to it's
power supply input.  The device does not have to protect against being connected
in reverse for prolonged periods of time.  It is assumed that the installer will
have some proper form of circuit protection installed on the power supply to the
device.  This allows a simple shunt diode to be used for this purpose.  More
sophisticated schemes of protection are recommended but not required.

The device is not required to operate while connected in reverse.  It must
simply survive.  In fact is recommended that the device NOT operate properly
while it's power supply is reversed.  This would cause attention to be given to
the device that it  would not recieve if it was opearating normally while
connected in reverse.

Good engineering practices should be used in the design of these devices.
A complete description is outside the scope of this document, however here is
a short list of issues to pay attention to.

  * Proper shielding should be employed to prevent radio frequency interfernce
    with other devices in the aircraft, if applicable.
  * Good power filtering should be used to prevent conducted noise from affecting
    other devices within the aircraft.  Also proper bypassing of high frequency
    components (i.e. microcontrollers) should also be employed for the same
    reason.
  * High quality components should be used when possible.
  * The system should be designed in such a way, that faults within the device
    will not cause a fire.
