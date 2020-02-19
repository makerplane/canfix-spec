Suggested Device Types
----------------------

Each device should have a specific device type that can be queried by the Node
Identification command to determine what kind of device the node is.  The
purpose for this is mostly configuration.  This device type as well as the model
number and firmware version could be used by configuration software to look up
and indicate to the user the name of the device, what kind of firmware loading
algorithms to use, the configuration parameters that are available, etc.

Although not a requirement for the proper functioning of the network it seems
helpful enough to suggest a set of device types for CAN-FiX capable devices.

The following list gives some recommendations for device type codes.  This is by
no means exhaustive and is not required.

It is also recommended that each device, ship with it's default Node ID set to
the device type.  For simple installations this may keep the user from having to
set Node IDs at all.  The Node IDs can be changed with Node Specific Messages
easily enough in the cases where that is necessary.

The device types are separated into groups.  The first code in the group is
marked as General and can be used if the correct one cannot be found.  This list
will be updated from time to time.  See the section :ref:`Approval Process`
for more details on the revision process.


**Flight Control Inputs**

  0x00
    General
  0x01
    Pitch
  0x02
    Roll
  0x03
    Yaw
  0x04
    Collective
  0x05
    Cyclic
  0x06
    Flap
  0x07
    Speed Brake / Spoiler
  0x08
    Combination Pitch / Roll

**Engine Control Inputs**

  0x10
    General
  0x11
    Throttle Control
  0x12
    Propeller Pitch Control
  0x13
    Mixture Control


**System Control Inputs**

  0x20
    General
  0x21
    Keyboard
  0x22
    Numeric Keypad
  0x23
    Button / Switch Input


**Flight Data**

  0x30
    General
  0x31
    AHRS
  0x32
    Air Data
  0x33
    Pitot Pressure
  0x34
    Static Pressure
  0x35
    AOA
  0x36
    Magnetometer
  0x37
    Air Data
  0x38
    OAT Input
  0x39
    Radar Altimeter

**Engine Data**

  0x40
    General
  0x41
    Thermocouple Input
  0x42
    Fuel Flow
  0x43
    Fuel Level Input
  0x44
    Fuel Computer
  0x45
    EGT Input
  0x46
    CHT Input
  0x47
    Inlet Air Temperature Input
  0x48
    Oil Pressure Input
  0x49
    Oil Temperature Input
  0x4A
    Fuel Pressure Input
  0x4B
    Resistive Thermal Input
  0x4C
    Pressure Input

**Flight Controls**

  0x60
    General
  0x61
    Pitch Surface
  0x62
    Roll Surface
  0x63
    Yaw Surface
  0x64
    Collective
  0x65
    Cyclic
  0x66
    Pitch Autopilot Servo
  0x67
    Roll Autopilot Servo
  0x68
    Yaw Autopilot Servo
  0x69
    Cyclic Autopilot Servo
  0x6A
    Collective Autopilot Servo
  0x6B
    Combination Autopilot
  0x6C
    Pitch Trim Servo
  0x6D
    Roll Trim Servo
  0x6E
    Yaw Trim
  0x6F
    Flap Motor


**Engine Controls**

  0x80
    General
  0x81
    Fuel Servo
  0x82
    Propeller Pitch
  0x83
    Engine Control Unit
  0x84
    Ignition Control Unit


**Display Equipment**

  0x90
    General
  0x91
    Primary Electronic Flight Display
  0x92
    Secondary Electronic Flight Display
  0x93
    Annunciator
  0x94
    Generic Display


**Device Interface**

  0xA0
    General
  0xA1
    Navigation Radio Interface
  0xA2
    Comm Radio Interface
  0xA3
    Transponder Interface
  0xA4
    EMS Serial Interface Converter
  0xA5
    EFIS Serial Interface Converter


**Protocol Converter**

  0xB0
    General
  0xB1
    Serial NMEA Converter
  0xB2
    FIX Serial Port Converter
  0xB3
    Generic Serial Protocol Converter
  0xB4
    Generic Protocol Converter
  0xB5
    USB Interface
  0xB6
    CAN-FiX Router


**Navigation**

  0xC0
    General
  0xC1
    GPS
  0xC2
    NAV/ILS/GS Receiver
  0xC3
    Navigation Computer
  0xC4
    ADS-B Receiver


**Misc**

  0xD0
    General
  0xD1
    Position Light Controller
  0xD2
    Strobe Light Controller
  0xD3
    Panel Light Dimmer / Controller
  0xD4
    Cabin Light Controller
  0xD5
    Combination Light Controller
  0xD6
    Generic Discrete Input
  0xD7
    Generic Discrete Output
  0xD8
    Generic Analog Input
  0xFE
    Simulation
  0xFF
    Configuration Software
