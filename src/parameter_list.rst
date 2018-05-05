High Priority Pilot Control Inputs
----------------------------------

Flap Control Switches
~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 256 - 257 (0x100 - 0x101)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:FIX Id\:: FLAPSW
:Remarks\::
  | b0 = Up
  | b1 = Down
  | b2 - b7 Can be used for predefined notches

Trim Switches
~~~~~~~~~~~~~

:Identifiers\:: 258 - 259 (0x102 - 0x103)
:Data Type\:: WORD
:Range\:: Discrete Bits
:FIX Id\:: TRIMSW
:Remarks\::
  | b0 = Pitch Up
  | b1 = Pitch Down
  | b2 = Pitch Center
  | b3 = Roll Left
  | b4 = Roll Right
  | b5 = Roll Center
  | b6 = Yaw Left
  | b7 = Yaw Right
  | b8 = Yaw Center
  | b9 = Collective Up
  | b10 = Collective Dn
  | b11 = AT Pedals Left
  | b12 = AT Pedals Right
  | b13 = AT Pedals Center

Electrical Bus Control Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 260 - 261 (0x104 - 0x105)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Lighting Control Switches
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 262 - 263 (0x106 - 0x107)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Fuel Pump System Switches
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 264 - 265 (0x108 - 0x109)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Fuel Valve System Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 266 - 267 (0x10A - 0x10B)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Auto Pilot Commands
~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 268 - 269 (0x10C - 0x10D)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:Remarks\::
  | b0 = Engage
  | b1 = Disconnect
  | b2 = VS Mode
  | b3 = Alt Hold Mode
  | b4 = Alt Select Mode
  | b5 = Heading Increment
  | b6 = Heading Decrement

VHF Control Commands
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 270 - 271 (0x10E - 0x10F)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:Index\:: Radio
:Remarks\::
  | b0 = PTT
  | b1 = Flip
  | b2 = Next Saved Freq
  | b3 = Last Saved Freq

VOR/LOC Control Commands
~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 272 - 273 (0x110 - 0x111)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:Index\:: Radio
:Remarks\::
  | b1 = Flip
  | b2 = Next Saved Freq
  | b3 = Last Saved Freq

Transponder Commands
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 274 - 275 (0x112 - 0x113)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:Remarks\::
  | b0 = IDENT
  | b1 = ALT
  | b2 = STBY
  | b2 = ALT
  | b3 = VFR
  | b5 = OFF
  | b6 = Squat

Starter / Magneto Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 276 - 277 (0x114 - 0x115)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Landing Gear Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 278 - 279 (0x116 - 0x117)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:Remarks\::
  | 0=Down
  | 1=Up
  | b0=Nose
  | b1=Left
  | b2=Right

Keypad Input
~~~~~~~~~~~~

:Identifiers\:: 280 - 281 (0x118 - 0x119)
:Data Type\:: CHAR[2]
:Range\:: Key, Function Key

Encoder Input (High Priority)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 282 - 283 (0x11A - 0x11B)
:Data Type\:: INT[2],BYTE
:Range\:: Steps Moved
:Index\:: Unit
:Remarks\::
  | X,Y and Switch Positions
  | Less than 0 = CCW, Greater than 0 = CW

Generic Switches (High Priority)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 284 - 291 (0x11C - 0x123)
:Data Type\:: BYTE[5]
:Range\:: Discrete Bits
:Index\:: Unit
:Remarks\::
  | User Defined For Multiplexing Switches

Pitch Control Position
~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 292 (0x124)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:FIX Id\:: CTLPTCH
:Remarks\::
  | Greater Than 0 = Nose Up

Roll Control Position
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 293 (0x125)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:FIX Id\:: CTLROLL
:Remarks\::
  | Greater Than 0 = Right

Yaw Control Position
~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 294 (0x126)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:FIX Id\:: CTLYAW
:Remarks\::
  | Greater Than 0 = Right

Collective Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 295 (0x127)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:FIX Id\:: CTLCOLL
:Remarks\::
  | Greater Than 0 = Up

Anti-Torque Pedals Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 296 (0x128)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:FIX Id\:: CTLATP
:Remarks\::
  | Greater Than 0 = Right

Flap Control Position
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 297 (0x129)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:FIX Id\:: CTLFLAP
:Remarks\::
  | Greater Than 0 = Down

Left Brake Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 298 (0x12A)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:FIX Id\:: CTLLBRK

Right Brake Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 299 (0x12B)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:FIX Id\:: CTLRBRK

Engine Throttle Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 300 - 301 (0x12C - 0x12D)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:FIX Id\:: THR#

Engine Prop Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 302 - 303 (0x12E - 0x12F)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:FIX Id\:: PROP#

Engine Mixture Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 304 - 305 (0x130 - 0x131)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:FIX Id\:: MIX#

Generic Analog Control (High Priority)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 306 - 307 (0x132 - 0x133)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:Index\:: Unit
:FIX Id\:: GENAI#
:Remarks\::
  | User Defined


High Priority Measured Positions
--------------------------------

Elevator Position
~~~~~~~~~~~~~~~~~

:Identifier\:: 320 (0x140)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:FIX Id\:: ELVPOS
:Meta\::
  | 0000 = Min
  | 0001 = Max

:Remarks\::
  | Greater Than 0 = Nose Up

Aileron Position
~~~~~~~~~~~~~~~~

:Identifier\:: 321 (0x141)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:FIX Id\:: AILPOS
:Meta\::
  | 0000 = Min
  | 0001 = Max

:Remarks\::
  | Greater Than 0 = Right

Rudder Position
~~~~~~~~~~~~~~~

:Identifier\:: 322 (0x142)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:FIX Id\:: RUDPOS
:Meta\::
  | 0000 = Min
  | 0001 = Max

:Remarks\::
  | Greater Than 0 = Right

Collective Position
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 323 (0x143)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:FIX Id\:: TRANGL
:Meta\::
  | 0000 = Min
  | 0001 = Max

:Remarks\::
  | Greater Than 0 = Up

Tail Rotor Angle
~~~~~~~~~~~~~~~~

:Identifier\:: 324 (0x144)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:FIX Id\:: FLPPOS
:Meta\::
  | 0000 = Min
  | 0001 = Max

:Remarks\::
  | Greater Than 0 = Right

Flap Position
~~~~~~~~~~~~~

:Identifier\:: 325 (0x145)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:Meta\::
  | 0000 = Min
  | 0001 = Max

:Remarks\::
  | Greater Than 0 = Down

Landing Gear Position Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 326 (0x146)
:Data Type\:: BYTE
:Range\:: Discrete Bits
:FIX Id\:: GEARSW
:Remarks\::
  | b0=Nose Up
  | b1=Nose Down
  | b2=Left Up
  | b3=Left Down
  | b4=Right Up
  | b5=Right Down


High Priority Flight Data
-------------------------

Pitch Angle
~~~~~~~~~~~

:Identifier\:: 384 (0x180)
:Data Type\:: INT
:Range\:: -180 to 180
:Units\:: 0.01°
:FIX Id\:: PITCH
:Remarks\::
  | Greater Than 0 = Nose Up

Roll Angle
~~~~~~~~~~

:Identifier\:: 385 (0x181)
:Data Type\:: INT
:Range\:: -180 to 180
:Units\:: 0.01°
:FIX Id\:: ROLL
:Remarks\::
  | Greater Than 0 = Right

Angle of Attack
~~~~~~~~~~~~~~~

:Identifier\:: 386 (0x182)
:Data Type\:: INT
:Range\:: -180 to 180
:Units\:: 0.01°
:FIX Id\:: AOA
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0110 = 0g
  | 0111 = Warn
  | 1000 = Stall


Indicated Airspeed
~~~~~~~~~~~~~~~~~~

:Identifier\:: 387 (0x183)
:Data Type\:: UINT
:Range\:: 0 to 999.9
:Units\:: 0.1 knots
:FIX Id\:: IAS
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0010 = V1
  | 0011 = V2
  | 0100 = Vne
  | 0101 = Vfe
  | 0110 = Vmc
  | 0111 = Va
  | 1000 = Vno
  | 1001 = Vs
  | 1010 = Vs0
  | 1101 = Vx
  | 1110 = Vy


Indicated Altitude
~~~~~~~~~~~~~~~~~~

:Identifier\:: 388 (0x184)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:FIX Id\:: ALT

Heading
~~~~~~~

:Identifier\:: 389 (0x185)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°
:FIX Id\:: HEAD
:Remarks\::
  | Magnetic Heading

Vertical Speed
~~~~~~~~~~~~~~

:Identifier\:: 390 (0x186)
:Data Type\:: INT
:Range\:: -30,000 to 30,000
:Units\:: ft/min
:FIX Id\:: VERTSP
:Meta\::
  | 0000 = Min
  | 0001 = Max


TE Variometer Vertical Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 391 (0x187)
:Data Type\:: INT
:Range\:: -300 to 300
:Units\:: 0.01 knots
:FIX Id\:: VARIO
:Meta\::
  | 0000 = Min
  | 0001 = Max


Radar Altitude
~~~~~~~~~~~~~~

:Identifier\:: 392 (0x188)
:Data Type\:: UINT
:Range\:: 0 to 60,000
:Units\:: ft
:FIX Id\:: RALT
:Meta\::
  | 0000 = Min
  | 0001 = Max


Yaw Angle
~~~~~~~~~

:Identifier\:: 393 (0x189)
:Data Type\:: INT
:Range\:: -180 to 180
:Units\:: 0.01°
:FIX Id\:: YAW
:Meta\::
  | 0000 = Min
  | 0001 = Max


Normal Acceleration
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 394 (0x18A)
:Data Type\:: INT
:Range\:: -30 to 30
:Units\:: 0.001 g
:FIX Id\:: ACNOR
:Meta\::
  | 0000 = Min
  | 0001 = Max


Lateral Acceleration
~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 395 (0x18B)
:Data Type\:: INT
:Range\:: -30 to 30
:Units\:: 0.001 g
:FIX Id\:: ACLAT
:Meta\::
  | 0000 = Min
  | 0001 = Max


Longitudinal Acceleration
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 396 (0x18C)
:Data Type\:: INT
:Range\:: -30 to 30
:Units\:: 0.001 g
:FIX Id\:: ACLON
:Meta\::
  | 0000 = Min
  | 0001 = Max


True Airspeed
~~~~~~~~~~~~~

:Identifier\:: 397 (0x18D)
:Data Type\:: UINT
:Range\:: 0 to 2000
:Units\:: 0.1 knots
:FIX Id\:: TAS
:Meta\::
  | 0000 = Min
  | 0001 = Max


Calibrated Airspeed
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 398 (0x18E)
:Data Type\:: UINT
:Range\:: 0 to 2000
:Units\:: 0.1 knots
:FIX Id\:: CAS
:Meta\::
  | 0000 = Min
  | 0001 = Max


Mach Number
~~~~~~~~~~~

:Identifier\:: 399 (0x18F)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01 Mach
:FIX Id\:: MACH
:Meta\::
  | 0000 = Min
  | 0001 = Max


Altimeter Setting
~~~~~~~~~~~~~~~~~

:Identifier\:: 400 (0x190)
:Data Type\:: UINT
:Range\:: 0 to 35
:Units\:: 0.001 inHg
:FIX Id\:: BARO

Pressure Altitude
~~~~~~~~~~~~~~~~~

:Identifier\:: 401 (0x191)
:Data Type\:: DINT
:Range\:: -1,000 to 60,000
:Units\:: ft
:FIX Id\:: PALT


High Priority Navigation Data
-----------------------------

VOR/LOC Deviation
~~~~~~~~~~~~~~~~~

:Identifier\:: 448 (0x1C0)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°
:FIX Id\:: VORDEV

Glideslope Deviation
~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 449 (0x1C1)
:Data Type\:: INT
:Range\:: -45 to 45
:Units\:: 0.01°
:FIX Id\:: GSDEV

OBI Flags
~~~~~~~~~

:Identifier\:: 450 (0x1C2)
:Data Type\:: WORD
:FIX Id\:: OBIFLG
:Remarks\::
  | b0 = To/From (To = 1)
  | b1:b2 = Input (00=NAV1, 01=NAV2, 10=GPS1, 11=GPS2)
  | b3 = GS
  | b4 = LOC/NAV

Aircraft Position Latitude
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 451 (0x1C3)
:Data Type\:: FLOAT
:Range\:: -90 to 90
:Units\:: °
:FIX Id\:: LAT

Aircraft Position Longitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 452 (0x1C4)
:Data Type\:: FLOAT
:Range\:: -180 to 180
:Units\:: °
:FIX Id\:: LONG

Groundspeed
~~~~~~~~~~~

:Identifier\:: 453 (0x1C5)
:Data Type\:: UINT
:Range\:: 0 to 2000
:Units\:: 0.1 knots
:FIX Id\:: GSPEED

True Ground Track
~~~~~~~~~~~~~~~~~

:Identifier\:: 454 (0x1C6)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°
:FIX Id\:: TRACK

Magnetic Ground Track
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 455 (0x1C7)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°
:FIX Id\:: TRACKM

Cross Track Error
~~~~~~~~~~~~~~~~~

:Identifier\:: 456 (0x1C8)
:Data Type\:: INT
:Units\:: 0.01 nm
:FIX Id\:: XTRACK

Selected Course
~~~~~~~~~~~~~~~

:Identifier\:: 457 (0x1C9)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°
:FIX Id\:: COURSE

Selected Glidepath Angle
~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 458 (0x1CA)
:Data Type\:: UINT
:Range\:: 0 to 90
:Units\:: 0.1°

Selected Vertical Speed
~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 459 (0x1CB)
:Data Type\:: INT
:Range\:: -30,000 to 30,000
:Units\:: ft/min

Selected Altitude
~~~~~~~~~~~~~~~~~

:Identifier\:: 460 (0x1CC)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft

RAIM Status
~~~~~~~~~~~

:Identifier\:: 461 (0x1CD)
:Data Type\:: USHORT
:Remarks\::
  | 0 if Good
  | Otherwise the ID of the most likely failed satellite

RAIM Horizontal Error
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 462 (0x1CE)
:Data Type\:: UINT
:Units\:: ft

RAIM Vertical Error
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 463 (0x1CF)
:Data Type\:: UINT
:Units\:: ft

ADS-B ES Airborne Position Latitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 464 (0x1D0)
:Data Type\:: FLOAT
:Range\:: -90 to 90
:Units\:: °
:Index\:: Aircraft

ADS-B ES Airborne Position Longitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 465 (0x1D1)
:Data Type\:: FLOAT
:Range\:: -180 to 180
:Units\:: °
:Index\:: Aircraft

ADS-B ES Airborne Position Altitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 466 (0x1D2)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:Index\:: Aircraft

ADS-B ES Surface Position Latitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 467 (0x1D3)
:Data Type\:: FLOAT
:Range\:: -90 to 90
:Units\:: °
:Index\:: Aircraft

ADS-B ES Surface Position Longitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 468 (0x1D4)
:Data Type\:: FLOAT
:Range\:: -180 to 180
:Units\:: °
:Index\:: Aircraft

ADS-B ES Surface Position Altitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 469 (0x1D5)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:Index\:: Aircraft

ADS-B ES Status
~~~~~~~~~~~~~~~

:Identifier\:: 470 (0x1D6)
:Data Type\:: 
:Index\:: Aircraft

ADS-B ES Identification
~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 471 (0x1D7)
:Data Type\:: 
:Index\:: Aircraft

ADS-B ES Type
~~~~~~~~~~~~~

:Identifier\:: 472 (0x1D8)
:Data Type\:: 
:Index\:: Aircraft

ADS-B ES Airborne Velocity
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 473 (0x1D9)
:Data Type\:: UINT
:Range\:: 0 to 2000
:Units\:: 0.1 knots
:Index\:: Aircraft

ADS-B ES Airborne Bearing
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 474 (0x1DA)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°
:Index\:: Aircraft

ADS-B ES Airborne Rate of Climb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 475 (0x1DB)
:Data Type\:: INT
:Range\:: -30,000 to 30,000
:Units\:: ft/min
:Index\:: Aircraft

ADS-B ES Emergency Priority Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 476 (0x1DC)
:Data Type\:: 
:Index\:: Aircraft
:Remarks\::
  | Event Driven Information

ADS-B ES Current Trajectory Change Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 477 (0x1DD)
:Data Type\:: 
:Index\:: Aircraft
:Remarks\::
  | Event Driven Information

ADS-B ES Next Trajectory Change Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 478 (0x1DE)
:Data Type\:: 
:Index\:: Aircraft
:Remarks\::
  | Event Driven Information

ADS-B ES Operation Coord. Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 479 (0x1DF)
:Data Type\:: 
:Index\:: Aircraft
:Remarks\::
  | Event Driven Information

ADS-B ES Operational Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 480 (0x1E0)
:Data Type\:: 
:Index\:: Aircraft
:Remarks\::
  | Event Driven Information


High Priority Engine / Aircraft System Data
-------------------------------------------

N1 or Engine RPM
~~~~~~~~~~~~~~~~

:Identifiers\:: 512 - 513 (0x200 - 0x201)
:Data Type\:: UINT
:Units\:: RPM
:FIX Id\:: TACH
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm
  | 0111 = Restriction 1 Low
  | 1000 = Restriction 1 High
  | 1001 = Restriction 2 Low
  | 1010 = Restriction 2 High

:Remarks\::
  | N1 for Turbines

N2, Prop RPM or Rotor RPM
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 514 - 515 (0x202 - 0x203)
:Data Type\:: UINT
:Units\:: RPM
:FIX Id\:: PROP
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm
  | 0111 = Restriction 1 Low
  | 1000 = Restriction 1 High
  | 1001 = Restriction 2 Low
  | 1010 = Restriction 2 High

:Remarks\::
  | N2 for Turbines

Torque
~~~~~~

:Identifiers\:: 516 - 517 (0x204 - 0x205)
:Data Type\:: INT
:FIX Id\:: TORQUE
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Turbine Inlet Temperature
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 518 - 519 (0x206 - 0x207)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: TIT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Inter-turbine Temperature
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 520 - 521 (0x208 - 0x209)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: ITT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Turbine Outlet Temperature
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 522 - 523 (0x20A - 0x20B)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: TOT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Fuel Pressure Switch
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 524 - 525 (0x20C - 0x20D)
:Data Type\:: SHORT
:FIX Id\:: FUELPS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Oil Pressure Switch
~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 526 - 527 (0x20E - 0x20F)
:Data Type\:: SHORT
:FIX Id\:: OILPS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Oil Temperature Switch
~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 528 - 529 (0x210 - 0x211)
:Data Type\:: SHORT
:FIX Id\:: OILTS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Coolant Temperature Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 530 - 531 (0x212 - 0x213)
:Data Type\:: SHORT
:FIX Id\:: H2OTS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Fuel Quantity Switch
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 532 - 533 (0x214 - 0x215)
:Data Type\:: SHORT
:FIX Id\:: FUELS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Oil Quantity Switch
~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 534 - 535 (0x216 - 0x217)
:Data Type\:: SHORT
:FIX Id\:: OILLS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Coolant Quantity Switch
~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 536 - 537 (0x218 - 0x219)
:Data Type\:: SHORT
:FIX Id\:: H2OLS
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Fuel Flow
~~~~~~~~~

:Identifiers\:: 538 - 539 (0x21A - 0x21B)
:Data Type\:: UINT
:Units\:: 0.01 gal/hr
:FIX Id\:: FUELF
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Fuel Pressure
~~~~~~~~~~~~~

:Identifiers\:: 540 - 541 (0x21C - 0x21D)
:Data Type\:: UINT
:Units\:: 0.01 psi
:FIX Id\:: FUELP
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Manifold Pressure
~~~~~~~~~~~~~~~~~

:Identifiers\:: 542 - 543 (0x21E - 0x21F)
:Data Type\:: UINT
:Units\:: 0.01 inHg
:FIX Id\:: MAP
:Meta\::
  | 0000 = Min
  | 0001 = Max


Oil Pressure
~~~~~~~~~~~~

:Identifiers\:: 544 - 545 (0x220 - 0x221)
:Data Type\:: UINT
:Units\:: 0.01 psi
:FIX Id\:: OILP
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Oil Temperature
~~~~~~~~~~~~~~~

:Identifiers\:: 546 - 547 (0x222 - 0x223)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: OILT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Coolant Temperature
~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 548 - 549 (0x224 - 0x225)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: H2OT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Fuel Quantity
~~~~~~~~~~~~~

:Identifiers\:: 550 - 553 (0x226 - 0x229)
:Data Type\:: UINT
:Units\:: 0.01 gal
:Index\:: Aux Tank
:FIX Id\:: FUELQ
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Fuel Pump Pressure
~~~~~~~~~~~~~~~~~~

:Identifiers\:: 554 - 555 (0x22A - 0x22B)
:Data Type\:: UINT
:Units\:: 0.01 psi
:FIX Id\:: FUELPP
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Oil Quantity
~~~~~~~~~~~~

:Identifiers\:: 556 - 557 (0x22C - 0x22D)
:Data Type\:: UINT
:Units\:: 0.01 gal
:FIX Id\:: OILQTY
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Coolant Quantity
~~~~~~~~~~~~~~~~

:Identifiers\:: 558 - 559 (0x22E - 0x22F)
:Data Type\:: UINT
:Units\:: 0.01 gal
:FIX Id\:: H2OQTY
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Electric Propulsion Motor Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 560 - 561 (0x230 - 0x231)
:Data Type\:: UINT
:Units\:: A
:FIX Id\:: EMI
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Main Propulsion Bus Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 562 - 563 (0x232 - 0x233)
:Data Type\:: UINT
:Units\:: 0.1 V
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Main Battery Current
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 564 - 565 (0x234 - 0x235)
:Data Type\:: INT
:Units\:: A
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Main Battery Temperature
~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 566 - 567 (0x236 - 0x237)
:Data Type\:: UINT
:Units\:: 0.1°C
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm


Main Battery Charge
~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 568 - 569 (0x238 - 0x239)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.1%
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm


Hybrid System Status
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 570 - 571 (0x23A - 0x23B)
:Data Type\:: WORD


High Priority Auxiliary Data
----------------------------

Cabin Pressure
~~~~~~~~~~~~~~

:Identifier\:: 640 (0x280)
:Data Type\:: UINT
:Range\:: 0 to 35
:Units\:: 0.001 inHg

Cabin Altitude
~~~~~~~~~~~~~~

:Identifier\:: 641 (0x281)
:Data Type\:: INT
:Range\:: -1,000 to 30,000
:Units\:: ft


Normal Priority Pilot Control Inputs
------------------------------------

Encoder Input
~~~~~~~~~~~~~

:Identifiers\:: 768 - 775 (0x300 - 0x307)
:Data Type\:: INT[2],BYTE
:Range\:: Steps Moved
:Index\:: Unit
:Remarks\::
  | X,Y and Switch Positions
  | Less than 0 = CCW, Greater than 0 = CW

Generic Switches
~~~~~~~~~~~~~~~~

:Identifiers\:: 776 - 783 (0x308 - 0x30F)
:Data Type\:: BYTE[5]
:Range\:: Discrete Bits
:Index\:: Unit
:Remarks\::
  | User Defined For Multiplexing Switches

Speedbrake Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 784 (0x310)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%

Cowl Flaps Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 785 (0x311)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%

Pitch Trim Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 786 (0x312)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%

Roll Trim Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 787 (0x313)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%

Yaw Trim Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 788 (0x314)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%

Collective Trim Control Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 789 (0x315)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%

Anti-Torque Pedals Trim Position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 790 (0x316)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%

Generic Analog Control
~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 791 - 798 (0x317 - 0x31E)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:Index\:: Unit
:Remarks\::
  | User Defined


Normal Priority Measured Positions
----------------------------------

Speedbrake Position
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 896 (0x380)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:Remarks\::
  | Less than 0 = Down
  | Greater than 0 = Up

Cowl Flaps Position
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 897 (0x381)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:Remarks\::
  | 100% = Open

Pitch Trim Position
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 898 (0x382)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:Remarks\::
  | Less than 0 = Down
  | Greater than 0 = Up

Roll Trim Position
~~~~~~~~~~~~~~~~~~

:Identifier\:: 899 (0x383)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Yaw Trim Position
~~~~~~~~~~~~~~~~~

:Identifier\:: 900 (0x384)
:Data Type\:: INT
:Range\:: -90 to 90
:Units\:: 0.01°
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Pitch Trim Motor Speed
~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 901 (0x385)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:Remarks\::
  | Less than 0 = Down
  | Greater than 0 = Up

Roll Trim Motor Speed
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 902 (0x386)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Yaw Trim Motor Speed
~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 903 (0x387)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Collective Trim Motor Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 904 (0x388)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:Remarks\::
  | Less than 0 = Down
  | Greater than 0 = Up

Anti-Torque Pedals Trim Motor Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 905 (0x389)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.01%
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Light Status
~~~~~~~~~~~~

:Identifier\:: 906 (0x38A)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Fuel Pump Status
~~~~~~~~~~~~~~~~

:Identifiers\:: 907 - 910 (0x38B - 0x38E)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Fuel Valve Status
~~~~~~~~~~~~~~~~~

:Identifier\:: 911 (0x38F)
:Data Type\:: BYTE
:Range\:: Discrete Bits

Generic Analog Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 912 - 919 (0x390 - 0x397)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:Index\:: Unit
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm

:Remarks\::
  | User Defined


Normal Priority Flight Data
---------------------------

Pitch Rate
~~~~~~~~~~

:Identifier\:: 1024 (0x400)
:Data Type\:: INT
:Range\:: -3000 to 3000
:Units\:: 0.1°/sec
:Remarks\::
  | Less than 0 = Down
  | Greater than 0 = Up

Roll Rate
~~~~~~~~~

:Identifier\:: 1025 (0x401)
:Data Type\:: INT
:Range\:: -3000 to 3000
:Units\:: 0.1°/sec
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Yaw Rate
~~~~~~~~

:Identifier\:: 1026 (0x402)
:Data Type\:: INT
:Range\:: -3000 to 3000
:Units\:: 0.1°/sec
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Turn Rate
~~~~~~~~~

:Identifier\:: 1027 (0x403)
:Data Type\:: INT
:Range\:: -3000 to 3000
:Units\:: 0.1°/sec
:Remarks\::
  | Less than 0 = Left
  | Greater than 0 = Right

Static Pressure
~~~~~~~~~~~~~~~

:Identifier\:: 1028 (0x404)
:Data Type\:: UINT
:Units\:: 0.001 inHg

Pitot Pressure
~~~~~~~~~~~~~~

:Identifier\:: 1029 (0x405)
:Data Type\:: UINT
:Units\:: 0.001 inHg

Total Air Temperature
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1030 (0x406)
:Data Type\:: INT
:Range\:: -300 to 300
:Units\:: 0.01°C

Static Air Temperature
~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1031 (0x407)
:Data Type\:: INT
:Range\:: -300 to 300
:Units\:: 0.01°C

Density Altitude
~~~~~~~~~~~~~~~~

:Identifier\:: 1032 (0x408)
:Data Type\:: DINT
:Range\:: -1,000 to 60,000
:Units\:: ft

True Altitude
~~~~~~~~~~~~~

:Identifier\:: 1033 (0x409)
:Data Type\:: DINT
:Range\:: -1,000 to 60,000
:Units\:: ft

Wind Speed
~~~~~~~~~~

:Identifier\:: 1034 (0x40A)
:Data Type\:: UINT
:Range\:: 0 to 2000
:Units\:: 0.1 knots

Wind Direction
~~~~~~~~~~~~~~

:Identifier\:: 1035 (0x40B)
:Data Type\:: UINT
:Range\:: 0 to 360
:Units\:: 0.01°
:Remarks\::
  | Magnetic


Normal Priority Navigation Data
-------------------------------

Next Waypoint Identifier
~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1152 (0x480)
:Data Type\:: CHAR[4]

Next Waypoint Latitude
~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1153 (0x481)
:Data Type\:: FLOAT
:Range\:: -90 to 90
:Units\:: °

Next Waypoint Longitude
~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1154 (0x482)
:Data Type\:: FLOAT
:Range\:: -180 to 180
:Units\:: °

Next Waypoint Altitude
~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1155 (0x483)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft

Next Waypoint ETA
~~~~~~~~~~~~~~~~~

:Identifier\:: 1156 (0x484)
:Data Type\:: USHORT[3]
:Range\:: Hour, Min, Sec
:Units\:: UTC

Next Waypoint ETE
~~~~~~~~~~~~~~~~~

:Identifier\:: 1157 (0x485)
:Data Type\:: USHORT[3]
:Range\:: Hour, Min, Sec

Waypoint Identifier
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1158 (0x486)
:Data Type\:: CHAR[4]
:Index\:: Waypoint

Waypoint Latitude
~~~~~~~~~~~~~~~~~

:Identifier\:: 1159 (0x487)
:Data Type\:: FLOAT
:Range\:: -90 to 90
:Units\:: °
:Index\:: Waypoint

Waypoint Longitude
~~~~~~~~~~~~~~~~~~

:Identifier\:: 1160 (0x488)
:Data Type\:: FLOAT
:Range\:: -180 to 180
:Units\:: °
:Index\:: Waypoint

Waypoint Altitude
~~~~~~~~~~~~~~~~~

:Identifier\:: 1161 (0x489)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:Index\:: Waypoint

Waypoint ETA
~~~~~~~~~~~~

:Identifier\:: 1162 (0x48A)
:Data Type\:: USHORT[3]
:Range\:: Hour, Min, Sec
:Units\:: UTC
:Index\:: Waypoint

Waypoint ETE
~~~~~~~~~~~~

:Identifier\:: 1163 (0x48B)
:Data Type\:: USHORT[3]
:Range\:: Hour, Min, Sec
:Index\:: Waypoint

Waypoint, Distance To
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1164 (0x48C)
:Data Type\:: UINT
:Units\:: nm
:Index\:: Waypoint

Waypoint Minimum Altitude
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1165 (0x48D)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:Index\:: Waypoint

Waypoint Minimum Flight Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1166 (0x48E)
:Data Type\:: UINT
:Index\:: Waypoint

Waypoint Minimum Radar Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1167 (0x48F)
:Data Type\:: UINT
:Index\:: Waypoint

Waypoint Maximum Altitude
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1168 (0x490)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:Index\:: Waypoint

Waypoint Maximum Flight Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1169 (0x491)
:Data Type\:: UINT
:Index\:: Waypoint

Waypoint Maximum Radar Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1170 (0x492)
:Data Type\:: UINT
:Index\:: Waypoint

Waypoint Planned Altitude
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1171 (0x493)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft
:Index\:: Waypoint

Waypoint Reserved
~~~~~~~~~~~~~~~~~

:Identifier\:: 1172 (0x494)
:Data Type\:: 
:Index\:: Waypoint

Destination Identifier
~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1173 (0x495)
:Data Type\:: CHAR[4]

Destination Latitude
~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1174 (0x496)
:Data Type\:: FLOAT
:Range\:: -90 to 90
:Units\:: °

Destination Longitude
~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1175 (0x497)
:Data Type\:: FLOAT
:Range\:: -180 to 180
:Units\:: °

Destination Altitude
~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1176 (0x498)
:Data Type\:: DINT
:Range\:: -1000 to 60,000
:Units\:: ft

Destination ETA
~~~~~~~~~~~~~~~

:Identifier\:: 1177 (0x499)
:Data Type\:: USHORT[3]
:Range\:: Hour, Min, Sec
:Units\:: UTC

Destination ETE
~~~~~~~~~~~~~~~

:Identifier\:: 1178 (0x49A)
:Data Type\:: USHORT[3]
:Range\:: Hour, Min, Sec

Track Error Angle
~~~~~~~~~~~~~~~~~

:Identifier\:: 1179 (0x49B)
:Data Type\:: 
:Units\:: °

Reserved
~~~~~~~~

:Identifiers\:: 1180 - 1215 (0x49C - 0x4BF)
:Data Type\:: 

VHF Com Frequency
~~~~~~~~~~~~~~~~~

:Identifiers\:: 1216 - 1219 (0x4C0 - 0x4C3)
:Data Type\:: UINT
:Units\:: 0.01 MHz
:Index\:: 0=Current, 1=Standby, >1 = Memory Locations

VOR/ILS Frequency
~~~~~~~~~~~~~~~~~

:Identifiers\:: 1220 - 1223 (0x4C4 - 0x4C7)
:Data Type\:: UINT
:Range\:: 0 to 359
:Units\:: °
:Index\:: 0=Current, 1=Standby, >1 = Memory Locations

VOR/ILS Identifier
~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1224 - 1227 (0x4C8 - 0x4CB)
:Data Type\:: CHAR[4]

Actual VOR Radial
~~~~~~~~~~~~~~~~~

:Identifiers\:: 1228 - 1231 (0x4CC - 0x4CF)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°

Selected VOR Radial
~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1232 - 1235 (0x4D0 - 0x4D3)
:Data Type\:: UINT
:Range\:: 0 to 359.9
:Units\:: 0.1°

Transponder Code
~~~~~~~~~~~~~~~~

:Identifier\:: 1236 (0x4D4)
:Data Type\:: USHORT[4]


Normal Priority Engine / Aircraft System Data
---------------------------------------------

Cylinder Head Temperature
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1280 - 1281 (0x500 - 0x501)
:Data Type\:: UINT
:Units\:: 0.1°C
:Index\:: Cylinder
:FIX Id\:: CHT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Exhaust Gas Temperature
~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1282 - 1283 (0x502 - 0x503)
:Data Type\:: UINT
:Units\:: 0.1°C
:Index\:: Cylinder
:FIX Id\:: EGT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Cylinder Head Temp. Rate of Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1284 - 1285 (0x504 - 0x505)
:Data Type\:: UINT
:Units\:: 0.1°C/Min
:Index\:: Cylinder
:FIX Id\:: CHTROC
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm


Cylinder Head Temp. Deviation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1286 - 1287 (0x506 - 0x507)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: CHTDT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm


Exhaust Gas Temp.  Rate of Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1288 - 1289 (0x508 - 0x509)
:Data Type\:: UINT
:Units\:: 0.1°C/Min
:Index\:: Cylinder
:FIX Id\:: EGTROC
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm


Exhaust Gas Temp. Deviation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1290 - 1291 (0x50A - 0x50B)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: EGTDT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm


Carburetor Temperature
~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1292 - 1293 (0x50C - 0x50D)
:Data Type\:: UINT
:Units\:: 0.1°C
:FIX Id\:: CARBT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Electrical Bus Voltage
~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1294 - 1297 (0x50E - 0x511)
:Data Type\:: UINT
:Units\:: 0.1 V
:FIX Id\:: VOLT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Electrical Bus Current
~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1298 - 1301 (0x512 - 0x515)
:Data Type\:: UINT
:Units\:: 0.1 A
:FIX Id\:: CURRNT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Generator / Alternator Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1302 - 1305 (0x516 - 0x519)
:Data Type\:: UINT
:Units\:: 0.1 V
:FIX Id\:: ALTVOLT
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Generator / Alternator Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1306 - 1309 (0x51A - 0x51D)
:Data Type\:: UINT
:Units\:: 0.1 A
:FIX Id\:: ALTCUR
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Engine Power
~~~~~~~~~~~~

:Identifiers\:: 1310 - 1311 (0x51E - 0x51F)
:Data Type\:: UINT
:Units\:: 0.1%
:FIX Id\:: POWER

Total Engine Time
~~~~~~~~~~~~~~~~~

:Identifiers\:: 1312 - 1313 (0x520 - 0x521)
:Data Type\:: UINT
:Units\:: 0.1 Hours
:Index\:: Flight
:FIX Id\:: HOBBS
:Remarks\::
  | Index 0 = Total, 1 = last flight, reverse chronological order from there

Total Engine Time (Tach)
~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1314 - 1315 (0x522 - 0x523)
:Data Type\:: UINT
:Units\:: 0.1 Hours
:Index\:: Flight
:FIX Id\:: TACHTM
:Remarks\::
  | Index 0 = Total, 1 = last flight, reverse chronological order from there

Gearbox Speed
~~~~~~~~~~~~~

:Identifiers\:: 1316 - 1317 (0x524 - 0x525)
:Data Type\:: UINT
:Units\:: RPM
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Gearbox Oil Pressure Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1318 - 1319 (0x526 - 0x527)
:Data Type\:: BYTE
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Gearbox Oil Temperature Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1320 - 1321 (0x528 - 0x529)
:Data Type\:: BYTE
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Gearbox Oil Quantity Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1322 - 1323 (0x52A - 0x52B)
:Data Type\:: BYTE
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Hydraulic Pressure Switch
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1324 - 1325 (0x52C - 0x52D)
:Data Type\:: BYTE
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Hydraulic Temperature Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1326 - 1327 (0x52E - 0x52F)
:Data Type\:: BYTE
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Hydraulic Fluid Quantity Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1328 - 1329 (0x530 - 0x531)
:Data Type\:: BYTE
:Remarks\::
  | 0 = Normal
  | -1 = Low
  | 1 = High

Gearbox Oil Pressure
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1330 - 1331 (0x532 - 0x533)
:Data Type\:: UINT
:Units\:: 0.01 psi
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Gearbox Oil Temperature
~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1332 - 1333 (0x534 - 0x535)
:Data Type\:: UINT
:Units\:: 0.1°C
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Gearbox Oil Quantity
~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1334 - 1335 (0x536 - 0x537)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Hydraulic Pressure
~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1336 - 1337 (0x538 - 0x539)
:Data Type\:: UINT
:Units\:: 0.01 psi
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Hydraulic Temperature
~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1338 - 1339 (0x53A - 0x53B)
:Data Type\:: UINT
:Units\:: 0.1°C
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Hydraulic Fluid Quantity
~~~~~~~~~~~~~~~~~~~~~~~~

:Identifiers\:: 1340 - 1341 (0x53C - 0x53D)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.01%
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Tire Pressure
~~~~~~~~~~~~~

:Identifiers\:: 1344 - 1347 (0x540 - 0x543)
:Data Type\:: UINT
:Units\:: 0.01 psi
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Strut Pressure
~~~~~~~~~~~~~~

:Identifiers\:: 1348 - 1351 (0x544 - 0x547)
:Data Type\:: UINT
:Units\:: 0.01 psi
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Flight Time
~~~~~~~~~~~

:Identifier\:: 1349 (0x545)
:Data Type\:: UINT
:Units\:: 0.1 Hours
:Index\:: Flight
:FIX Id\:: FTIME
:Remarks\::
  | Index 0 = last flight, reverse chronological order from there


Normal Priority Auxiliary Data
------------------------------

Time
~~~~

:Identifier\:: 1408 (0x580)
:Data Type\:: USHORT[3],UINT
:Range\:: Hour, Min, Sec, mSec
:Units\:: UTC
:FIX Id\:: TIME

Date
~~~~

:Identifier\:: 1409 (0x581)
:Data Type\:: UINT, USHORT[2]
:Range\:: Year, Month, Day
:FIX Id\:: DATE

Time Zone
~~~~~~~~~

:Identifier\:: 1410 (0x582)
:Data Type\:: SHORT
:Range\:: -12 to 12
:Units\:: 0.1 Hours

Cabin Temperature
~~~~~~~~~~~~~~~~~

:Identifier\:: 1411 (0x583)
:Data Type\:: UINT
:Units\:: 0.1°C

Panel Dimmer Level
~~~~~~~~~~~~~~~~~~

:Identifier\:: 1412 (0x584)
:Data Type\:: USHORT
:Range\:: 0 to 100
:Units\:: %

Longitudinal Center of Gravity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1413 (0x585)
:Data Type\:: UINT
:Range\:: 0 to 100
:Units\:: 0.1% MAC
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Lateral Center of Gravity
~~~~~~~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1414 (0x586)
:Data Type\:: INT
:Range\:: -100 to 100
:Units\:: 0.1%
:Meta\::
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm


Aircraft Identifier
~~~~~~~~~~~~~~~~~~~

:Identifier\:: 1415 (0x587)
:Data Type\:: CHAR[5]
:FIX Id\:: ID

Aircraft Type
~~~~~~~~~~~~~

:Identifier\:: 1416 (0x588)
:Data Type\:: CHAR[5]

