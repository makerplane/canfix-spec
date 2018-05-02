High Priority Pilot Control Inputs
----------------------------------

**256 - 257 (0x100 - 0x101) Flap Control Switches**

:Data Type: BYTE
:Range: Discrete Bits
:FIX Id: FLAPSW
:Remarks:
  | b0 = Up
  | b1 = Down
  | b2 - b7 Can be used for predefined notches


------------------

**258 - 259 (0x102 - 0x103) Trim Switches**

:Data Type: WORD
:Range: Discrete Bits
:FIX Id: TRIMSW
:Remarks:
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


------------------

**260 - 261 (0x104 - 0x105) Electrical Bus Control Switches**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**262 - 263 (0x106 - 0x107) Lighting Control Switches**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**264 - 265 (0x108 - 0x109) Fuel Pump System Switches**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**266 - 267 (0x10A - 0x10B) Fuel Valve System Switches**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**268 - 269 (0x10C - 0x10D) Auto Pilot Commands**

:Data Type: BYTE
:Range: Discrete Bits
:Remarks:
  | b0 = Engage
  | b1 = Disconnect
  | b2 = VS Mode
  | b3 = Alt Hold Mode
  | b4 = Alt Select Mode
  | b5 = Heading Increment
  | b6 = Heading Decrement


------------------

**270 - 271 (0x10E - 0x10F) VHF Control Commands**

:Data Type: BYTE
:Range: Discrete Bits
:Index: Radio
:Remarks:
  | b0 = PTT
  | b1 = Flip
  | b2 = Next Saved Freq
  | b3 = Last Saved Freq


------------------

**272 - 273 (0x110 - 0x111) VOR/LOC Control Commands**

:Data Type: BYTE
:Range: Discrete Bits
:Index: Radio
:Remarks:
  | b1 = Flip
  | b2 = Next Saved Freq
  | b3 = Last Saved Freq


------------------

**274 - 275 (0x112 - 0x113) Transponder Commands**

:Data Type: BYTE
:Range: Discrete Bits
:Remarks:
  | b0 = IDENT
  | b1 = ALT
  | b2 = STBY
  | b2 = ALT
  | b3 = VFR
  | b5 = OFF
  | b6 = Squat


------------------

**276 - 277 (0x114 - 0x115) Starter / Magneto Commands**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**278 - 279 (0x116 - 0x117) Landing Gear Control Position**

:Data Type: BYTE
:Range: Discrete Bits
:Remarks:
  | 0=Down
  | 1=Up
  | b0=Nose
  | b1=Left
  | b2=Right


------------------

**280 - 281 (0x118 - 0x119) Keypad Input**

:Data Type: CHAR[2]
:Range: Key, Function Key


------------------

**282 - 283 (0x11A - 0x11B) Encoder Input (High Priority)**

:Data Type: INT[2],BYTE
:Range: Steps Moved
:Index: Unit
:Remarks:
  | X,Y and Switch Positions
  | Less than 0 = CCW, Greater than 0 = CW


------------------

**284 - 291 (0x11C - 0x123) Generic Switches (High Priority)**

:Data Type: BYTE[5]
:Range: Discrete Bits
:Index: Unit
:Remarks:
  | User Defined For Multiplexing Switches


------------------

**292 - 292 (0x124 - 0x124) Pitch Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:FIX Id: CTLPTCH
:Remarks:
  | Greater Than 0 = Nose Up


------------------

**293 - 293 (0x125 - 0x125) Roll Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:FIX Id: CTLROLL
:Remarks:
  | Greater Than 0 = Right


------------------

**294 - 294 (0x126 - 0x126) Yaw Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:FIX Id: CTLYAW
:Remarks:
  | Greater Than 0 = Right


------------------

**295 - 295 (0x127 - 0x127) Collective Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:FIX Id: CTLCOLL
:Remarks:
  | Greater Than 0 = Up


------------------

**296 - 296 (0x128 - 0x128) Anti-Torque Pedals Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:FIX Id: CTLATP
:Remarks:
  | Greater Than 0 = Right


------------------

**297 - 297 (0x129 - 0x129) Flap Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:FIX Id: CTLFLAP
:Remarks:
  | Greater Than 0 = Down


------------------

**298 - 298 (0x12A - 0x12A) Left Brake Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:FIX Id: CTLLBRK


------------------

**299 - 299 (0x12B - 0x12B) Right Brake Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:FIX Id: CTLRBRK


------------------

**300 - 301 (0x12C - 0x12D) Engine Throttle Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:FIX Id: THR#


------------------

**302 - 303 (0x12E - 0x12F) Engine Prop Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:FIX Id: PROP#


------------------

**304 - 305 (0x130 - 0x131) Engine Mixture Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:FIX Id: MIX#


------------------

**306 - 307 (0x132 - 0x133) Generic Analog Control (High Priority)**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:Index: Unit
:FIX Id: GENAI#
:Remarks:
  | User Defined


------------------


High Priority Measured Positions
--------------------------------

**320 - 320 (0x140 - 0x140) Elevator Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:FIX Id: ELVPOS
:Meta:
  | 0000 = Min
  | 0001 = Max

:Remarks:
  | Greater Than 0 = Nose Up


------------------

**321 - 321 (0x141 - 0x141) Aileron Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:FIX Id: AILPOS
:Meta:
  | 0000 = Min
  | 0001 = Max

:Remarks:
  | Greater Than 0 = Right


------------------

**322 - 322 (0x142 - 0x142) Rudder Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:FIX Id: RUDPOS
:Meta:
  | 0000 = Min
  | 0001 = Max

:Remarks:
  | Greater Than 0 = Right


------------------

**323 - 323 (0x143 - 0x143) Collective Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:FIX Id: TRANGL
:Meta:
  | 0000 = Min
  | 0001 = Max

:Remarks:
  | Greater Than 0 = Up


------------------

**324 - 324 (0x144 - 0x144) Tail Rotor Angle**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:FIX Id: FLPPOS
:Meta:
  | 0000 = Min
  | 0001 = Max

:Remarks:
  | Greater Than 0 = Right


------------------

**325 - 325 (0x145 - 0x145) Flap Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:Meta:
  | 0000 = Min
  | 0001 = Max

:Remarks:
  | Greater Than 0 = Down


------------------

**326 - 326 (0x146 - 0x146) Landing Gear Position Switches**

:Data Type: BYTE
:Range: Discrete Bits
:FIX Id: GEARSW
:Remarks:
  | b0=Nose Up
  | b1=Nose Down
  | b2=Left Up
  | b3=Left Down
  | b4=Right Up
  | b5=Right Down


------------------


High Priority Flight Data
-------------------------

**384 - 384 (0x180 - 0x180) Pitch Angle**

:Data Type: INT
:Range: -180 to 180
:Units: 0.01°
:FIX Id: PITCH
:Remarks:
  | Greater Than 0 = Nose Up


------------------

**385 - 385 (0x181 - 0x181) Roll Angle**

:Data Type: INT
:Range: -180 to 180
:Units: 0.01°
:FIX Id: ROLL
:Remarks:
  | Greater Than 0 = Right


------------------

**386 - 386 (0x182 - 0x182) Angle of Attack**

:Data Type: INT
:Range: -180 to 180
:Units: 0.01°
:FIX Id: AOA
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0110 = 0g
  | 0111 = Warn
  | 1000 = Stall



------------------

**387 - 387 (0x183 - 0x183) Indicated Airspeed**

:Data Type: UINT
:Range: 0 to 999.9
:Units: 0.1 knots
:FIX Id: IAS
:Meta:
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



------------------

**388 - 388 (0x184 - 0x184) Indicated Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:FIX Id: ALT


------------------

**389 - 389 (0x185 - 0x185) Heading**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°
:FIX Id: HEAD
:Remarks:
  | Magnetic Heading


------------------

**390 - 390 (0x186 - 0x186) Vertical Speed**

:Data Type: INT
:Range: -30,000 to 30,000
:Units: ft/min
:FIX Id: VERTSP
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**391 - 391 (0x187 - 0x187) TE Variometer Vertical Speed**

:Data Type: INT
:Range: -300 to 300
:Units: 0.01 knots
:FIX Id: VARIO
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**392 - 392 (0x188 - 0x188) Radar Altitude**

:Data Type: UINT
:Range: 0 to 60,000
:Units: ft
:FIX Id: RALT
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**393 - 393 (0x189 - 0x189) Yaw Angle**

:Data Type: INT
:Range: -180 to 180
:Units: 0.01°
:FIX Id: YAW
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**394 - 394 (0x18A - 0x18A) Normal Acceleration**

:Data Type: INT
:Range: -30 to 30
:Units: 0.001 g
:FIX Id: ACNOR
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**395 - 395 (0x18B - 0x18B) Lateral Acceleration**

:Data Type: INT
:Range: -30 to 30
:Units: 0.001 g
:FIX Id: ACLAT
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**396 - 396 (0x18C - 0x18C) Longitudinal Acceleration**

:Data Type: INT
:Range: -30 to 30
:Units: 0.001 g
:FIX Id: ACLON
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**397 - 397 (0x18D - 0x18D) True Airspeed**

:Data Type: UINT
:Range: 0 to 2000
:Units: 0.1 knots
:FIX Id: TAS
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**398 - 398 (0x18E - 0x18E) Calibrated Airspeed**

:Data Type: UINT
:Range: 0 to 2000
:Units: 0.1 knots
:FIX Id: CAS
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**399 - 399 (0x18F - 0x18F) Mach Number**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01 Mach
:FIX Id: MACH
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**400 - 400 (0x190 - 0x190) Altimeter Setting Set**

:Data Type: UINT
:Range: 0 to 35
:Units: 0.001 inHg
:FIX Id: BARO


------------------

**401 - 401 (0x191 - 0x191) Altimeter Setting Report**

:Data Type: UINT
:Range: 0 to 35
:Units: 0.001 inHg


------------------

**402 - 402 (0x192 - 0x192) Pressure Altitude**

:Data Type: DINT
:Range: -1,000 to 60,000
:Units: ft
:FIX Id: PALT


------------------


High Priority Navigation Data
-----------------------------

**448 - 448 (0x1C0 - 0x1C0) VOR/LOC Deviation**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°
:FIX Id: VORDEV


------------------

**449 - 449 (0x1C1 - 0x1C1) Glideslope Deviation**

:Data Type: INT
:Range: -45 to 45
:Units: 0.01°
:FIX Id: GSDEV


------------------

**450 - 450 (0x1C2 - 0x1C2) OBI Flags**

:Data Type: WORD
:FIX Id: OBIFLG
:Remarks:
  | b0 = To/From (To = 1)
  | b1:b2 = Input (00=NAV1, 01=NAV2, 10=GPS1, 11=GPS2)
  | b3 = GS
  | b4 = LOC/NAV


------------------

**451 - 451 (0x1C3 - 0x1C3) Aircraft Position Latitude**

:Data Type: FLOAT
:Range: -90 to 90
:Units: °
:FIX Id: LAT


------------------

**452 - 452 (0x1C4 - 0x1C4) Aircraft Position Longitude**

:Data Type: FLOAT
:Range: -180 to 180
:Units: °
:FIX Id: LONG


------------------

**453 - 453 (0x1C5 - 0x1C5) Groundspeed**

:Data Type: UINT
:Range: 0 to 2000
:Units: 0.1 knots
:FIX Id: GSPEED


------------------

**454 - 454 (0x1C6 - 0x1C6) True Ground Track**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°
:FIX Id: TRACK


------------------

**455 - 455 (0x1C7 - 0x1C7) Magnetic Ground Track**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°
:FIX Id: TRACKM


------------------

**456 - 456 (0x1C8 - 0x1C8) Cross Track Error**

:Data Type: INT
:Units: 0.01 nm
:FIX Id: XTRACK


------------------

**457 - 457 (0x1C9 - 0x1C9) Selected Course**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°
:FIX Id: COURSE


------------------

**458 - 458 (0x1CA - 0x1CA) Selected Glidepath Angle**

:Data Type: UINT
:Range: 0 to 90
:Units: 0.1°


------------------

**459 - 459 (0x1CB - 0x1CB) Selected Vertical Speed**

:Data Type: INT
:Range: -30,000 to 30,000
:Units: ft/min


------------------

**460 - 460 (0x1CC - 0x1CC) Selected Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft


------------------

**461 - 461 (0x1CD - 0x1CD) RAIM Status**

:Data Type: USHORT
:Remarks:
  | 0 if Good
  | Otherwise the ID of the most likely failed satellite


------------------

**462 - 462 (0x1CE - 0x1CE) RAIM Horizontal Error**

:Data Type: UINT
:Units: ft


------------------

**463 - 463 (0x1CF - 0x1CF) RAIM Vertical Error**

:Data Type: UINT
:Units: ft


------------------

**464 - 464 (0x1D0 - 0x1D0) ADS-B ES Airborne Position Latitude**

:Data Type: FLOAT
:Range: -90 to 90
:Units: °
:Index: Aircraft


------------------

**465 - 465 (0x1D1 - 0x1D1) ADS-B ES Airborne Position Longitude**

:Data Type: FLOAT
:Range: -180 to 180
:Units: °
:Index: Aircraft


------------------

**466 - 466 (0x1D2 - 0x1D2) ADS-B ES Airborne Position Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:Index: Aircraft


------------------

**467 - 467 (0x1D3 - 0x1D3) ADS-B ES Surface Position Latitude**

:Data Type: FLOAT
:Range: -90 to 90
:Units: °
:Index: Aircraft


------------------

**468 - 468 (0x1D4 - 0x1D4) ADS-B ES Surface Position Longitude**

:Data Type: FLOAT
:Range: -180 to 180
:Units: °
:Index: Aircraft


------------------

**469 - 469 (0x1D5 - 0x1D5) ADS-B ES Surface Position Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:Index: Aircraft


------------------

**470 - 470 (0x1D6 - 0x1D6) ADS-B ES Status**

:Data Type: 
:Index: Aircraft


------------------

**471 - 471 (0x1D7 - 0x1D7) ADS-B ES Identification**

:Data Type: 
:Index: Aircraft


------------------

**472 - 472 (0x1D8 - 0x1D8) ADS-B ES Type**

:Data Type: 
:Index: Aircraft


------------------

**473 - 473 (0x1D9 - 0x1D9) ADS-B ES Airborne Velocity**

:Data Type: UINT
:Range: 0 to 2000
:Units: 0.1 knots
:Index: Aircraft


------------------

**474 - 474 (0x1DA - 0x1DA) ADS-B ES Airborne Bearing**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°
:Index: Aircraft


------------------

**475 - 475 (0x1DB - 0x1DB) ADS-B ES Airborne Rate of Climb**

:Data Type: INT
:Range: -30,000 to 30,000
:Units: ft/min
:Index: Aircraft


------------------

**476 - 476 (0x1DC - 0x1DC) ADS-B ES Emergency Priority Status**

:Data Type: 
:Index: Aircraft
:Remarks:
  | Event Driven Information


------------------

**477 - 477 (0x1DD - 0x1DD) ADS-B ES Current Trajectory Change Point**

:Data Type: 
:Index: Aircraft
:Remarks:
  | Event Driven Information


------------------

**478 - 478 (0x1DE - 0x1DE) ADS-B ES Next Trajectory Change Point**

:Data Type: 
:Index: Aircraft
:Remarks:
  | Event Driven Information


------------------

**479 - 479 (0x1DF - 0x1DF) ADS-B ES Operation Coord. Message**

:Data Type: 
:Index: Aircraft
:Remarks:
  | Event Driven Information


------------------

**480 - 480 (0x1E0 - 0x1E0) ADS-B ES Operational Status**

:Data Type: 
:Index: Aircraft
:Remarks:
  | Event Driven Information


------------------


High Priority Engine / Aircraft System Data
-------------------------------------------

**512 - 513 (0x200 - 0x201) N1 or Engine RPM**

:Data Type: UINT
:Units: RPM
:FIX Id: TACH
:Meta:
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

:Remarks:
  | N1 for Turbines


------------------

**514 - 515 (0x202 - 0x203) N2, Prop RPM or Rotor RPM**

:Data Type: UINT
:Units: RPM
:FIX Id: PROP
:Meta:
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

:Remarks:
  | N2 for Turbines


------------------

**516 - 517 (0x204 - 0x205) Torque**

:Data Type: INT
:FIX Id: TORQUE
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**518 - 519 (0x206 - 0x207) Turbine Inlet Temperature**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: TIT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**520 - 521 (0x208 - 0x209) Inter-turbine Temperature**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: ITT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**522 - 523 (0x20A - 0x20B) Turbine Outlet Temperature**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: TOT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**524 - 525 (0x20C - 0x20D) Fuel Pressure Switch**

:Data Type: SHORT
:FIX Id: FUELPS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**526 - 527 (0x20E - 0x20F) Oil Pressure Switch**

:Data Type: SHORT
:FIX Id: OILPS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**528 - 529 (0x210 - 0x211) Oil Temperature Switch**

:Data Type: SHORT
:FIX Id: OILTS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**530 - 531 (0x212 - 0x213) Coolant Temperature Switch**

:Data Type: SHORT
:FIX Id: H2OTS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**532 - 533 (0x214 - 0x215) Fuel Quantity Switch**

:Data Type: SHORT
:FIX Id: FUELS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**534 - 535 (0x216 - 0x217) Oil Quantity Switch**

:Data Type: SHORT
:FIX Id: OILLS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**536 - 537 (0x218 - 0x219) Coolant Quantity Switch**

:Data Type: SHORT
:FIX Id: H2OLS
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**538 - 539 (0x21A - 0x21B) Fuel Flow**

:Data Type: UINT
:Units: 0.01 gal/hr
:FIX Id: FUELF
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**540 - 541 (0x21C - 0x21D) Fuel Pressure**

:Data Type: UINT
:Units: 0.01 psi
:FIX Id: FUELP
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**542 - 543 (0x21E - 0x21F) Manifold Pressure**

:Data Type: UINT
:Units: 0.01 inHg
:FIX Id: MAP
:Meta:
  | 0000 = Min
  | 0001 = Max



------------------

**544 - 545 (0x220 - 0x221) Oil Pressure**

:Data Type: UINT
:Units: 0.01 psi
:FIX Id: OILP
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**546 - 547 (0x222 - 0x223) Oil Temperature**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: OILT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**548 - 549 (0x224 - 0x225) Coolant Temperature**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: H2OT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**550 - 553 (0x226 - 0x229) Fuel Quantity**

:Data Type: UINT
:Units: 0.01 gal
:Index: Aux Tank
:FIX Id: FUELQ
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**554 - 555 (0x22A - 0x22B) Fuel Pump Pressure**

:Data Type: UINT
:Units: 0.01 psi
:FIX Id: FUELPP
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**556 - 557 (0x22C - 0x22D) Oil Quantity**

:Data Type: UINT
:Units: 0.01 gal
:FIX Id: OILQTY
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**558 - 559 (0x22E - 0x22F) Coolant Quantity**

:Data Type: UINT
:Units: 0.01 gal
:FIX Id: H2OQTY
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**560 - 561 (0x230 - 0x231) Electric Propulsion Motor Current**

:Data Type: UINT
:Units: A
:FIX Id: EMI
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**562 - 563 (0x232 - 0x233) Main Propulsion Bus Voltage**

:Data Type: UINT
:Units: 0.1 V
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**564 - 565 (0x234 - 0x235) Main Battery Current**

:Data Type: INT
:Units: A
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**566 - 567 (0x236 - 0x237) Main Battery Temperature**

:Data Type: UINT
:Units: 0.1°C
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**568 - 569 (0x238 - 0x239) Main Battery Charge**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.1%
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm



------------------

**570 - 571 (0x23A - 0x23B) Hybrid System Status**

:Data Type: WORD


------------------


High Priority Auxiliary Data
----------------------------

**640 - 640 (0x280 - 0x280) Cabin Pressure**

:Data Type: UINT
:Range: 0 to 35
:Units: 0.001 inHg


------------------

**641 - 641 (0x281 - 0x281) Cabin Altitude**

:Data Type: INT
:Range: -1,000 to 30,000
:Units: ft


------------------


Normal Priority Pilot Control Inputs
------------------------------------

**768 - 775 (0x300 - 0x307) Encoder Input**

:Data Type: INT[2],BYTE
:Range: Steps Moved
:Index: Unit
:Remarks:
  | X,Y and Switch Positions
  | Less than 0 = CCW, Greater than 0 = CW


------------------

**776 - 783 (0x308 - 0x30F) Generic Switches**

:Data Type: BYTE[5]
:Range: Discrete Bits
:Index: Unit
:Remarks:
  | User Defined For Multiplexing Switches


------------------

**784 - 784 (0x310 - 0x310) Speedbrake Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%


------------------

**785 - 785 (0x311 - 0x311) Cowl Flaps Control Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%


------------------

**786 - 786 (0x312 - 0x312) Pitch Trim Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%


------------------

**787 - 787 (0x313 - 0x313) Roll Trim Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%


------------------

**788 - 788 (0x314 - 0x314) Yaw Trim Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%


------------------

**789 - 789 (0x315 - 0x315) Collective Trim Control Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%


------------------

**790 - 790 (0x316 - 0x316) Anti-Torque Pedals Trim Position**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%


------------------

**791 - 798 (0x317 - 0x31E) Generic Analog Control**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:Index: Unit
:Remarks:
  | User Defined


------------------


Normal Priority Measured Positions
----------------------------------

**896 - 896 (0x380 - 0x380) Speedbrake Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:Remarks:
  | Less than 0 = Down
  | Greater than 0 = Up


------------------

**897 - 897 (0x381 - 0x381) Cowl Flaps Position**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:Remarks:
  | 100% = Open


------------------

**898 - 898 (0x382 - 0x382) Pitch Trim Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:Remarks:
  | Less than 0 = Down
  | Greater than 0 = Up


------------------

**899 - 899 (0x383 - 0x383) Roll Trim Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**900 - 900 (0x384 - 0x384) Yaw Trim Position**

:Data Type: INT
:Range: -90 to 90
:Units: 0.01°
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**901 - 901 (0x385 - 0x385) Pitch Trim Motor Speed**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:Remarks:
  | Less than 0 = Down
  | Greater than 0 = Up


------------------

**902 - 902 (0x386 - 0x386) Roll Trim Motor Speed**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**903 - 903 (0x387 - 0x387) Yaw Trim Motor Speed**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**904 - 904 (0x388 - 0x388) Collective Trim Motor Speed**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:Remarks:
  | Less than 0 = Down
  | Greater than 0 = Up


------------------

**905 - 905 (0x389 - 0x389) Anti-Torque Pedals Trim Motor Speed**

:Data Type: INT
:Range: -100 to 100
:Units: 0.01%
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**906 - 906 (0x38A - 0x38A) Light Status**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**907 - 910 (0x38B - 0x38E) Fuel Pump Status**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**911 - 911 (0x38F - 0x38F) Fuel Valve Status**

:Data Type: BYTE
:Range: Discrete Bits


------------------

**912 - 919 (0x390 - 0x397) Generic Analog Measurement**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:Index: Unit
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm

:Remarks:
  | User Defined


------------------


Normal Priority Flight Data
---------------------------

**1024 - 1024 (0x400 - 0x400) Pitch Rate**

:Data Type: INT
:Range: -3000 to 3000
:Units: 0.1°/sec
:Remarks:
  | Less than 0 = Down
  | Greater than 0 = Up


------------------

**1025 - 1025 (0x401 - 0x401) Roll Rate**

:Data Type: INT
:Range: -3000 to 3000
:Units: 0.1°/sec
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**1026 - 1026 (0x402 - 0x402) Yaw Rate**

:Data Type: INT
:Range: -3000 to 3000
:Units: 0.1°/sec
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**1027 - 1027 (0x403 - 0x403) Turn Rate**

:Data Type: INT
:Range: -3000 to 3000
:Units: 0.1°/sec
:Remarks:
  | Less than 0 = Left
  | Greater than 0 = Right


------------------

**1028 - 1028 (0x404 - 0x404) Static Pressure**

:Data Type: UINT
:Units: 0.001 inHg


------------------

**1029 - 1029 (0x405 - 0x405) Pitot Pressure**

:Data Type: UINT
:Units: 0.001 inHg


------------------

**1030 - 1030 (0x406 - 0x406) Total Air Temperature**

:Data Type: INT
:Range: -300 to 300
:Units: 0.01°C


------------------

**1031 - 1031 (0x407 - 0x407) Static Air Temperature**

:Data Type: INT
:Range: -300 to 300
:Units: 0.01°C


------------------

**1032 - 1032 (0x408 - 0x408) Density Altitude**

:Data Type: DINT
:Range: -1,000 to 60,000
:Units: ft


------------------

**1033 - 1033 (0x409 - 0x409) True Altitude**

:Data Type: DINT
:Range: -1,000 to 60,000
:Units: ft


------------------

**1034 - 1034 (0x40A - 0x40A) Wind Speed**

:Data Type: UINT
:Range: 0 to 2000
:Units: 0.1 knots


------------------

**1035 - 1035 (0x40B - 0x40B) Wind Direction**

:Data Type: UINT
:Range: 0 to 360
:Units: 0.01°
:Remarks:
  | Magnetic


------------------


Normal Priority Navigation Data
-------------------------------

**1152 - 1152 (0x480 - 0x480) Next Waypoint Identifier**

:Data Type: CHAR[4]


------------------

**1153 - 1153 (0x481 - 0x481) Next Waypoint Latitude**

:Data Type: FLOAT
:Range: -90 to 90
:Units: °


------------------

**1154 - 1154 (0x482 - 0x482) Next Waypoint Longitude**

:Data Type: FLOAT
:Range: -180 to 180
:Units: °


------------------

**1155 - 1155 (0x483 - 0x483) Next Waypoint Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft


------------------

**1156 - 1156 (0x484 - 0x484) Next Waypoint ETA**

:Data Type: USHORT[3]
:Range: Hour, Min, Sec
:Units: UTC


------------------

**1157 - 1157 (0x485 - 0x485) Next Waypoint ETE**

:Data Type: USHORT[3]
:Range: Hour, Min, Sec


------------------

**1158 - 1158 (0x486 - 0x486) Waypoint Identifier**

:Data Type: CHAR[4]
:Index: Waypoint


------------------

**1159 - 1159 (0x487 - 0x487) Waypoint Latitude**

:Data Type: FLOAT
:Range: -90 to 90
:Units: °
:Index: Waypoint


------------------

**1160 - 1160 (0x488 - 0x488) Waypoint Longitude**

:Data Type: FLOAT
:Range: -180 to 180
:Units: °
:Index: Waypoint


------------------

**1161 - 1161 (0x489 - 0x489) Waypoint Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:Index: Waypoint


------------------

**1162 - 1162 (0x48A - 0x48A) Waypoint ETA**

:Data Type: USHORT[3]
:Range: Hour, Min, Sec
:Units: UTC
:Index: Waypoint


------------------

**1163 - 1163 (0x48B - 0x48B) Waypoint ETE**

:Data Type: USHORT[3]
:Range: Hour, Min, Sec
:Index: Waypoint


------------------

**1164 - 1164 (0x48C - 0x48C) Waypoint, Distance To**

:Data Type: UINT
:Units: nm
:Index: Waypoint


------------------

**1165 - 1165 (0x48D - 0x48D) Waypoint Minimum Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:Index: Waypoint


------------------

**1166 - 1166 (0x48E - 0x48E) Waypoint Minimum Flight Level**

:Data Type: UINT
:Index: Waypoint


------------------

**1167 - 1167 (0x48F - 0x48F) Waypoint Minimum Radar Level**

:Data Type: UINT
:Index: Waypoint


------------------

**1168 - 1168 (0x490 - 0x490) Waypoint Maximum Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:Index: Waypoint


------------------

**1169 - 1169 (0x491 - 0x491) Waypoint Maximum Flight Level**

:Data Type: UINT
:Index: Waypoint


------------------

**1170 - 1170 (0x492 - 0x492) Waypoint Maximum Radar Level**

:Data Type: UINT
:Index: Waypoint


------------------

**1171 - 1171 (0x493 - 0x493) Waypoint Planned Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft
:Index: Waypoint


------------------

**1172 - 1172 (0x494 - 0x494) Waypoint Reserved**

:Data Type: 
:Index: Waypoint


------------------

**1173 - 1173 (0x495 - 0x495) Destination Identifier**

:Data Type: CHAR[4]


------------------

**1174 - 1174 (0x496 - 0x496) Destination Latitude**

:Data Type: FLOAT
:Range: -90 to 90
:Units: °


------------------

**1175 - 1175 (0x497 - 0x497) Destination Longitude**

:Data Type: FLOAT
:Range: -180 to 180
:Units: °


------------------

**1176 - 1176 (0x498 - 0x498) Destination Altitude**

:Data Type: DINT
:Range: -1000 to 60,000
:Units: ft


------------------

**1177 - 1177 (0x499 - 0x499) Destination ETA**

:Data Type: USHORT[3]
:Range: Hour, Min, Sec
:Units: UTC


------------------

**1178 - 1178 (0x49A - 0x49A) Destination ETE**

:Data Type: USHORT[3]
:Range: Hour, Min, Sec


------------------

**1179 - 1179 (0x49B - 0x49B) Track Error Angle**

:Data Type: 
:Units: °


------------------

**1180 - 1215 (0x49C - 0x4BF) Reserved**

:Data Type: 


------------------

**1216 - 1219 (0x4C0 - 0x4C3) VHF Com Frequency Set**

:Data Type: UINT
:Units: 0.01 MHz
:Index: 0=Current, 1=Standby, >1 = Memory Locations


------------------

**1220 - 1223 (0x4C4 - 0x4C7) VHF Com Frequency Report**

:Data Type: UINT
:Units: 0.01 MHz
:Index: 0=Current, 1=Standby, >1 = Memory Locations


------------------

**1224 - 1227 (0x4C8 - 0x4CB) VOR/ILS Frequency Set**

:Data Type: UINT
:Units: 0.01 MHz
:Index: 0=Current, 1=Standby, >1 = Memory Locations


------------------

**1228 - 1231 (0x4CC - 0x4CF) VOR/ILS Frequency Report**

:Data Type: UINT
:Range: 0 to 359
:Units: °
:Index: 0=Current, 1=Standby, >1 = Memory Locations


------------------

**1232 - 1235 (0x4D0 - 0x4D3) VOR/ILS Identifier**

:Data Type: CHAR[4]


------------------

**1236 - 1239 (0x4D4 - 0x4D7) Actual VOR Radial**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°


------------------

**1240 - 1243 (0x4D8 - 0x4DB) Selected VOR Radial**

:Data Type: UINT
:Range: 0 to 359.9
:Units: 0.1°


------------------

**1244 - 1244 (0x4DC - 0x4DC) Transponder Code**

:Data Type: USHORT[4]


------------------


Normal Priority Engine / Aircraft System Data
---------------------------------------------

**1280 - 1281 (0x500 - 0x501) Cylinder Head Temperature**

:Data Type: UINT
:Units: 0.1°C
:Index: Cylinder
:FIX Id: CHT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1282 - 1283 (0x502 - 0x503) Exhaust Gas Temperature**

:Data Type: UINT
:Units: 0.1°C
:Index: Cylinder
:FIX Id: EGT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1284 - 1285 (0x504 - 0x505) Cylinder Head Temp. Rate of Change**

:Data Type: UINT
:Units: 0.1°C/Min
:Index: Cylinder
:FIX Id: CHTROC
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1286 - 1287 (0x506 - 0x507) Cylinder Head Temp. Deviation**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: CHTDT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1288 - 1289 (0x508 - 0x509) Exhaust Gas Temp.  Rate of Change**

:Data Type: UINT
:Units: 0.1°C/Min
:Index: Cylinder
:FIX Id: EGTROC
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1290 - 1291 (0x50A - 0x50B) Exhaust Gas Temp. Deviation**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: EGTDT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1292 - 1293 (0x50C - 0x50D) Carburetor Temperature**

:Data Type: UINT
:Units: 0.1°C
:FIX Id: CARBT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1294 - 1297 (0x50E - 0x511) Electrical Bus Voltage**

:Data Type: UINT
:Units: 0.1 V
:FIX Id: VOLT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1298 - 1301 (0x512 - 0x515) Electrical Bus Current**

:Data Type: UINT
:Units: 0.1 A
:FIX Id: CURRNT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1302 - 1305 (0x516 - 0x519) Generator / Alternator Voltage**

:Data Type: UINT
:Units: 0.1 V
:FIX Id: ALTVOLT
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1306 - 1309 (0x51A - 0x51D) Generator / Alternator Current**

:Data Type: UINT
:Units: 0.1 A
:FIX Id: ALTCUR
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1310 - 1311 (0x51E - 0x51F) Engine Power**

:Data Type: UINT
:Units: 0.1%
:FIX Id: POWER


------------------

**1312 - 1313 (0x520 - 0x521) Total Engine Time**

:Data Type: UINT
:Units: 0.1 Hours
:FIX Id: HOBBS


------------------

**1314 - 1315 (0x522 - 0x523) Gearbox Speed**

:Data Type: UINT
:Units: RPM
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1316 - 1317 (0x524 - 0x525) Gearbox Oil Pressure Switch**

:Data Type: BYTE
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**1318 - 1319 (0x526 - 0x527) Gearbox Oil Temperature Switch**

:Data Type: BYTE
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**1320 - 1321 (0x528 - 0x529) Gearbox Oil Quantity Switch**

:Data Type: BYTE
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**1322 - 1323 (0x52A - 0x52B) Hydraulic Pressure Switch**

:Data Type: BYTE
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**1324 - 1325 (0x52C - 0x52D) Hydraulic Temperature Switch**

:Data Type: BYTE
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**1326 - 1327 (0x52E - 0x52F) Hydraulic Fluid Quantity Switch**

:Data Type: BYTE
:Remarks:
  | 0 = Normal
  | -1 = Low
  | 1 = High


------------------

**1328 - 1329 (0x530 - 0x531) Gearbox Oil Pressure**

:Data Type: UINT
:Units: 0.01 psi
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1330 - 1331 (0x532 - 0x533) Gearbox Oil Temperature**

:Data Type: UINT
:Units: 0.1°C
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1332 - 1333 (0x534 - 0x535) Gearbox Oil Quantity**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1334 - 1335 (0x536 - 0x537) Hydraulic Pressure**

:Data Type: UINT
:Units: 0.01 psi
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1336 - 1337 (0x538 - 0x539) Hydraulic Temperature**

:Data Type: UINT
:Units: 0.1°C
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1338 - 1339 (0x53A - 0x53B) Hydraulic Fluid Quantity**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.01%
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1340 - 1343 (0x53C - 0x53F) Tire Pressure**

:Data Type: UINT
:Units: 0.01 psi
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1344 - 1347 (0x540 - 0x543) Strut Pressure**

:Data Type: UINT
:Units: 0.01 psi
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1348 - 1348 (0x544 - 0x544) Flight Time**

:Data Type: UINT
:Units: 0.1 Hours
:Index: Flight
:FIX Id: FTIME
:Remarks:
  | 0 Index = last flight, reverse chronological order from there


------------------


Normal Priority Auxiliary Data
------------------------------

**1408 - 1408 (0x580 - 0x580) Time**

:Data Type: USHORT[3],UINT
:Range: Hour, Min, Sec, mSec
:Units: UTC
:FIX Id: TIME


------------------

**1409 - 1409 (0x581 - 0x581) Date**

:Data Type: UINT, USHORT[2]
:Range: Year, Month, Day
:FIX Id: DATE


------------------

**1410 - 1410 (0x582 - 0x582) Time Zone**

:Data Type: SHORT
:Range: -12 to 12


------------------

**1411 - 1411 (0x583 - 0x583) Cabin Temperature**

:Data Type: UINT
:Units: 0.1°C


------------------

**1412 - 1412 (0x584 - 0x584) Panel Dimmer Level**

:Data Type: USHORT
:Range: 0 to 100
:Units: %


------------------

**1413 - 1413 (0x585 - 0x585) Longitudinal Center of Gravity**

:Data Type: UINT
:Range: 0 to 100
:Units: 0.1% MAC
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1414 - 1414 (0x586 - 0x586) Lateral Center of Gravity**

:Data Type: INT
:Range: -100 to 100
:Units: 0.1%
:Meta:
  | 0000 = Min
  | 0001 = Max
  | 0011 = Low Warn
  | 0100 = Low Alarm
  | 0101 = High Warn
  | 0110 = High Alarm



------------------

**1415 - 1415 (0x587 - 0x587) Aircraft Identifier**

:Data Type: CHAR[5]
:FIX Id: ID


------------------

