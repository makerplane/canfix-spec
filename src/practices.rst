Recommended Practices
=====================

The information in this chapter is not a requirement to be compliant with this
specification.  Rather, simply a list of recommendations that help to simplify
and standardize the implementation of the specification.  This makes it easier
on the developer, because typical mistakes can be avoided and it makes it easier
on the end user, because things will work together more easily and consistently.

Changing Bit Rates
------------------

Typically when a device requests that nodes change their bit rate it will send
that message to the broadcast address so that all nodes on the network will be
affected simultaneously.  It will take some nodes longer to change bit rates
than others. A good practice when being commanded to change bit rate is to
follow this sequence...

  #. Stop normal communication and close the connection
  #. Change the bit rate timing of the CAN network controller
  #. Wait at least one second
  #. Reopen the CAN connection
  #. Send the response to the *Change Bit Rate* command at the new bit rate.
  #. Resume normal communication

The reason for the delay is to reduce errors on the network during the
transition.  It gives time for all the nodes on the network time to change to
the new bit rate set before communication resumes.

***Change Bit Rate commands should NEVER be sent in flight!***

This is a function that is best left for configuration on the ground.

Parameter Update Rates
----------------------

At this time the update rates of the individual parameters is not specified.
Good judgement should be used here.  An update rate of once every minute would
not be acceptable for Indicated Airspeed but it would be perfectly accpetable for
the Aircraft Indentification.

It has been found that an update rate of at least 10 Hz should be used for
Attitude and Heading data.  Airspeed, altitude, turn rate and similar
information should be written on the buss no slower than twice per second.
Primary instrumentation update rates should probably be a configuration
parameter that the end user can set but the device must be capable of measuring,
calculating and sending that data at an acceptable rate for the safe operation
of the aircraft.

Much data can be sent *On Change*.  User interface elements like switches,
encoders, dials and  joysticks can send data on change.  Devices that send
analog data should take care to filter out noise that might cause on change
behavior to saturate the network with data.  A maximum update rate could be
imployed for this purpose as well.  The data could be sent on change but not
faster than maximum rate.

Discrete User Input Signals
---------------------------

No maximum rate should be employed for discrete digital type inputs or state
could be lost.  If the signal that a button was pressed was never followed by
the signal that the button was released, the actual state of the button would be
lost.

We have found it unnecessary to repeatedly send the position of discrete
switches.  It was a deliberate design decision to place these particular
parameters very low in the CAN identifier ranges so that they would have high
enough priority to work properly when simply sending the change of state
messages.  For very important message it may make the designer more comfortable
to send the data on change and then send it again every few hundred milliseconds
to "make sure" that the state is not lost, but care should be taken not to
saturate the network with this type of information.  These are high priority
messages and can be used to overwhelm the network.

Synchronization
---------------

The time of day should be sent on the bus at least once per second and the
milliseconds should not be ignored.  Lamp flashers and other devices on the
network that require synchroniztion should be able to rely on this time being
accurate.  The GPS receiver is probably the  best source of this information.
Using the GPS receiver also has the added benefit of synchronizing these signals
between aircraft.  This could be particulary useful for  formation teams.

Parameter Replacement
---------------------

If a device uses an internally measured parameter in a calculation and that
particular parameter is disabled by the Node Specific message for that purpose,
the calculation should be stopped unless that same parameter is received on the
bus from another device.

The reason for this recommendation is that the user may have determined that the
internal measurement of your device is flawed or that there is simply a better
source of that information on another device.

For exmple, let's assume you are designing an air data computer.  Your device
will measure pitot and static pressure as expected and report airspeed, altitude
and vertical speed, but you will also be measuring the total air temperature and
using that to calculate true airspeed and density altitude.  The aircraft owner
may realize that the air temperature measurement that you are using is not very
good because of installation issues and disable that parameter. You should use
that as a hint that you should stop calculating and producing values that depend
on that data.  But if you start receiving the total air temperature on the bus
then you can use that value in your calculations.  Perhaps the engine monitor
that the user installed does a better job of measuring air temperature than your
device becuase the probe is mounted in a better location.

.. include:: devicetypes.rst

Electronic Data Sheets
----------------------

Each device should ship with an Electronic Data Sheet that describes it's
function and operation. The utility software that is being devloped for
configuring, monitoring and troubleshooting the network would rely on these data
sheets for critical information about your device.

The elctronic data sheet is nothing more than a JSON file.

At a minimum the EDS should include a description of your device as well as a
Device ID, Firmware Revision and Model Number.  These should match the
information that your device would send in response to a Node Identification
request.  The utility software is programmed to send a Node Identification
Request to every node that it sees on the network.  It uses the information in
the response to match the node on the network with the EDS file.

The EDS file should also list all the parameters that your device is capable of
sending.  This gives the utility software the ability to list the parameters for
the user that he/she can then enable or disable depending on the specific need
of the aircraft.

Configuration parameters are also an important part of the EDS file.  The
utility software would use this list to give the user input into what the
configuration options are in your device.

Lacking a proper EDS file, the utility software will still allow the user to
send configuration commands to your node but this will be much more difficult
for your user than it could be.

The format of the EDS file can be very simple.

Here is an example EDS file::

    {
      "name":"Airdata Computer",
      "id":"0x32",
      "model":"0x0A0B0C",
      "firmware_code":"0xF22",
      "firmware_driver":"AT328",
      "parameters":
        [
          "0x182",
          "0x183",
          "0x184",
          "0x186",
          "0x18D",
          "0x190",
          "0x191",
          "0x405",
          "0x406",
          "0x408",
          "0x409",
          "0x40A",
          "0x40B"
        ],
      "configuration":
      [
        {
          "key":"0x0001",
          "name":"Airspeed Min",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0002",
          "name":"Airspeed Max",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0003",
          "name":"V1",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0004",
          "name":"V2",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0005",
          "name":"Vne",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0006",
          "name":"Vfe",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0007",
          "name":"Vmc",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0008",
          "name":"Va",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x0009",
          "name":"Vno",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x000A",
          "name":"Vs",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x000B",
          "name":"Vs0",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x000C",
          "name":"Vx",
          "type":"UINT",
          "multipier":"0.1"
        },
        {
          "key":"0x000D",
          "name":"Vy",
          "type":"UINT",
          "multipier":"0.1"
        }
      ]
    }

This is a simple example.  More complete documentation is availabe with the
CAN-FIX Configuration Utility.
