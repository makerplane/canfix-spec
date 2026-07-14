# Parameter Quick-Reference

Every CAN-FiX parameter (protocol version **0.7**), grouped by CAN identifier range.  This page is generated from [`src/canfix.json`](https://github.com/billmallard/canfix-spec/blob/master/src/canfix.json), which is built from the master spreadsheet `src/CAN-FIX.ods` -- so it always matches the specification.

For the full normative definitions (data encodings, frame formats, meta data and bit fields) see the [complete specification](https://billmallard.github.io/canfix-spec/), in particular the [Parameters chapter](https://billmallard.github.io/canfix-spec/parameters.html).

**Reading this table**

- **ID** -- the 11-bit CAN frame identifier. A range (e.g. `256-257`) means the parameter occupies several consecutive IDs for multiple instances.
- **Type** -- the [data type](https://billmallard.github.io/canfix-spec/datatypes.html) of the value (see also [Data Types](Data-Types)).
- **Units / Range / Mult** -- engineering units, min/max, and the multiplier (the value each least-significant bit represents).
- **Notes** -- the index dimension (for indexed parameters), the data format, and any per-parameter remarks.

## High Priority Pilot Control Inputs (256-319)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 256-257 | Flap Control Switches | BYTE |  |  |  | Discrete Bits; b0 = Up; b1 = Down; b2 - b7 Can be used for predefined notches |
| 258-259 | Trim Switches | WORD |  |  |  | Discrete Bits; b0 = Pitch Up; b1 = Pitch Down; b2 = Pitch Center; b3 = Roll Left; b4 = Roll Right; b5 = Roll Center; b6 = Yaw Left; b7 = Yaw Right; b8 = Yaw Center; b9 = Collective Up; b10 = Collective Dn; b11 = AT Pedals Left; b12 = AT Pedals Right; b13 = AT Pedals Center |
| 260-261 | Electrical Bus Control Switches | BYTE |  |  |  | Discrete Bits |
| 262-263 | Lighting Control Switches | BYTE |  |  |  | Discrete Bits |
| 264-265 | Fuel Pump System Switches | BYTE |  |  |  | Discrete Bits |
| 266-267 | Fuel Valve System Switches | BYTE |  |  |  | Discrete Bits |
| 268-269 | Auto Pilot Commands | WORD |  |  |  | Discrete Bits; b0 = Engage; b1 = Disconnect; b2 = VS Mode; b3 = Alt Hold Mode; b4 = Alt Select Mode; b5 = Heading Increment; b6 = Heading Decrement |
| 270-271 | VHF Control Commands | BYTE |  |  |  | Indexed by Radio; Discrete Bits; b0 = PTT; b1 = Flip; b2 = Next Saved Freq; b3 = Prev Saved Freq |
| 272-273 | VOR/LOC Control Commands | BYTE |  |  |  | Indexed by Radio; Discrete Bits; b1 = Flip; b2 = Next Saved Freq; b3 = Prev Saved Freq |
| 274-275 | Transponder Commands | BYTE |  |  |  | Discrete Bits; b0 = IDENT; b1 = ALT; b2 = STBY; b3 = VFR; b4 = OFF; b5 = Squat |
| 276-277 | Starter / Magneto Commands | BYTE |  |  |  | Discrete Bits |
| 278-279 | Landing Gear Control Position | BYTE |  |  |  | Discrete Bits; 0=Down; 1=Up; b0=Nose; b1=Left; b2=Right |
| 280-281 | Keypad Input | CHAR[2] |  |  |  | Key, Function Key |
| 282-283 | Encoder Input (High Priority) | INT[2],BYTE |  |  |  | Indexed by Unit; Steps Moved; X,Y and Switch Positions; Less than 0 = CCW, Greater than 0 = CW |
| 284-291 | Generic Switches (High Priority) | BYTE[5] |  |  |  | Indexed by Unit; Discrete Bits; User Defined For Multiplexing Switches |
| 292 | Pitch Control Position | INT | % | -100 to 100 | 0.01 | Greater Than 0 = Nose Up |
| 293 | Roll Control Position | INT | % | -100 to 100 | 0.01 | Greater Than 0 = Right |
| 294 | Yaw Control Position | INT | % | -100 to 100 | 0.01 | Greater Than 0 = Right |
| 295 | Collective Control Position | INT | % | -100 to 100 | 0.01 | Greater Than 0 = Up |
| 296 | Anti-Torque Pedals Position | INT | % | -100 to 100 | 0.01 | Greater Than 0 = Right |
| 297 | Flap Control Position | INT | % | -100 to 100 | 0.01 | Greater Than 0 = Down |
| 298 | Left Brake Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 299 | Right Brake Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 300-301 | Engine Throttle Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 302-303 | Engine Prop Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 304-305 | Engine Mixture Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 306-307 | Generic Analog Control (High Priority) | UINT | % | 0 to 100 | 0.01 | Indexed by Unit; User Defined |

## High Priority Measured Positions (320-383)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 320 | Elevator Position | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Nose Up |
| 321 | Aileron Position | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Right |
| 322 | Rudder Position | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Right |
| 323 | Collective Position | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Up |
| 324 | Tail Rotor Angle | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Right |
| 325 | Flap Position | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Down |
| 326-328 | Landing Gear Position Switches | BYTE |  |  |  | Discrete Bits; b0=Nose Up; b1=Nose Down; b2=Left Up; b3=Left Down; b4=Right Up; b5=Right Down |

## High Priority Flight Data (384-447)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 384 | Pitch Angle | INT | ° | -90 to 90 | 0.01 | Greater Than 0 = Nose Up |
| 385 | Roll Angle | INT | ° | -180 to 180 | 0.01 | Greater Than 0 = Right |
| 386 | Angle of Attack | INT | ° | -90 to 90 | 0.01 |  |
| 387 | Indicated Airspeed | UINT | knots | 0 to 999.9 | 0.1 |  |
| 388 | Indicated Altitude | DINT | ft | -1000 to 60,000 |  |  |
| 389 | Heading | UINT | ° | 0 to 359.9 | 0.1 | Magnetic Heading |
| 390 | Vertical Speed | INT | ft/min | -30,000 to 30,000 |  |  |
| 391 | TE Variometer Vertical Speed | INT | knots | -300 to 300 | 0.01 |  |
| 392 | Radar Altitude | UINT | ft | 0 to 60,000 |  |  |
| 393 | Yaw Angle | INT | ° | -180 to 180 | 0.01 |  |
| 394 | Normal Acceleration | INT | g | -30 to 30 | 0.001 |  |
| 395 | Lateral Acceleration | INT | g | -30 to 30 | 0.001 |  |
| 396 | Longitudinal Acceleration | INT | g | -30 to 30 | 0.001 |  |
| 397 | True Airspeed | UINT | knots | 0 to 999.9 | 0.1 |  |
| 398 | Calibrated Airspeed | UINT | knots | 0 to 999.9 | 0.1 |  |
| 399 | Mach Number | UINT | Mach | 0 to 100 | 0.01 |  |
| 400 | Altimeter Setting | UINT | inHg | 0 to 35 | 0.001 |  |
| 401 | Pressure Altitude | DINT | ft | -1,000 to 60,000 |  |  |

## High Priority Navigation Data (448-511)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 448 | VOR/LOC Deviation | UINT | ° | 0 to 359.9 | 0.1 |  |
| 449 | Glideslope Deviation | INT | ° | -45 to 45 | 0.01 |  |
| 450 | OBI Flags | WORD |  |  |  | b0 = To/From (To = 1); b1:b2 = Input (00=NAV1, 01=NAV2, 10=GPS1, 11=GPS2); b3 = GS; b4 = LOC/NAV |
| 451 | Aircraft Position Latitude | FLOAT | ° | -90 to 90 |  |  |
| 452 | Aircraft Position Longitude | FLOAT | ° | -180 to 180 |  |  |
| 453 | Groundspeed | UINT | knots | 0 to 2000 | 0.1 |  |
| 454 | True Ground Track | UINT | ° | 0 to 359.9 | 0.1 |  |
| 455 | Magnetic Ground Track | UINT | ° | 0 to 359.9 | 0.1 |  |
| 456 | Cross Track Error | INT | nm |  | 0.01 |  |
| 457 | Selected Course | UINT | ° | 0 to 359.9 | 0.1 |  |
| 458 | Selected Glidepath Angle | UINT | ° | 0 to 90 | 0.1 |  |
| 459 | Selected Vertical Speed | INT | ft/min | -30,000 to 30,000 |  |  |
| 460 | Selected Airspeed | UINT | knots | 0 to 999.9 | 0.1 |  |
| 461 | Selected Altitude | DINT | ft | -1000 to 60,000 |  |  |
| 462 | RAIM Status | USHORT |  |  |  | 0 if Good; Otherwise the ID of the most likely failed satellite |
| 463 | RAIM Horizontal Error | UINT | ft |  |  |  |
| 464 | RAIM Vertical Error | UINT | ft |  |  |  |
| 465 | ADS-B ES Airborne Position Latitude | FLOAT | ° | -90 to 90 |  | Indexed by Aircraft |
| 466 | ADS-B ES Airborne Position Longitude | FLOAT | ° | -180 to 180 |  | Indexed by Aircraft |
| 467 | ADS-B ES Airborne Position Altitude | DINT | ft | -1000 to 60,000 |  | Indexed by Aircraft |
| 468 | ADS-B ES Surface Position Latitude | FLOAT | ° | -90 to 90 |  | Indexed by Aircraft |
| 469 | ADS-B ES Surface Position Longitude | FLOAT | ° | -180 to 180 |  | Indexed by Aircraft |
| 470 | ADS-B ES Surface Position Altitude | DINT | ft | -1000 to 60,000 |  | Indexed by Aircraft |
| 471 | ADS-B ES Status |  |  |  |  | Indexed by Aircraft |
| 472 | ADS-B ES Identification |  |  |  |  | Indexed by Aircraft |
| 473 | ADS-B ES Type |  |  |  |  | Indexed by Aircraft |
| 474 | ADS-B ES Airborne Velocity | UINT | knots | 0 to 2000 | 0.1 | Indexed by Aircraft |
| 475 | ADS-B ES Airborne Bearing | UINT | ° | 0 to 359.9 | 0.1 | Indexed by Aircraft |
| 476 | ADS-B ES Airborne Rate of Climb | INT | ft/min | -30,000 to 30,000 |  | Indexed by Aircraft |
| 477 | ADS-B ES Emergency Priority Status |  |  |  |  | Indexed by Aircraft; Event Driven Information |
| 478 | ADS-B ES Current Trajectory Change Point |  |  |  |  | Indexed by Aircraft; Event Driven Information |
| 479 | ADS-B ES Next Trajectory Change Point |  |  |  |  | Indexed by Aircraft; Event Driven Information |
| 480 | ADS-B ES Operation Coord. Message |  |  |  |  | Indexed by Aircraft; Event Driven Information |
| 481 | ADS-B ES Operational Status |  |  |  |  | Indexed by Aircraft; Event Driven Information |

## High Priority Engine / Aircraft System Data (512-639)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 512-513 | N1 or Engine RPM | UINT | RPM |  |  | N1 for Turbines |
| 514-515 | N2, Prop RPM or Rotor RPM | UINT | RPM |  |  | N2 for Turbines |
| 516-517 | Torque | INT |  |  |  |  |
| 518-519 | Turbine Inlet Temperature | UINT | °C |  | 0.1 |  |
| 520-521 | Inter-turbine Temperature | UINT | °C |  | 0.1 |  |
| 522-523 | Turbine Outlet Temperature | UINT | °C |  | 0.1 |  |
| 524-525 | Fuel Pressure Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 526-527 | Oil Pressure Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 528-529 | Oil Temperature Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 530-531 | Coolant Temperature Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 532-533 | Fuel Quantity Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 534-535 | Oil Quantity Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 536-537 | Coolant Quantity Switch | SHORT |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 538-539 | Fuel Flow | UINT | gal/hr |  | 0.01 |  |
| 540-541 | Fuel Pressure | UINT | psi |  | 0.01 |  |
| 542-543 | Manifold Pressure | UINT | inHg |  | 0.01 |  |
| 544-545 | Oil Pressure | UINT | psi |  | 0.01 |  |
| 546-547 | Oil Temperature | UINT | °C |  | 0.1 |  |
| 548-549 | Coolant Temperature | UINT | °C |  | 0.1 |  |
| 550-553 | Fuel Quantity | UINT | gal |  | 0.01 | Indexed by Aux Tank |
| 554-555 | Fuel Pump Pressure | UINT | psi |  | 0.01 |  |
| 556-557 | Oil Quantity | UINT | gal |  | 0.01 |  |
| 558-559 | Coolant Quantity | UINT | gal |  | 0.01 |  |
| 560-561 | Electric Propulsion Motor Current | UINT | A |  |  |  |
| 562-563 | Main Propulsion Bus Voltage | UINT | V |  | 0.1 |  |
| 564-565 | Main Battery Current | INT | A |  |  |  |
| 566-567 | Main Battery Temperature | UINT | °C |  | 0.1 |  |
| 568-569 | Main Battery Charge | UINT | % | 0 to 100 | 0.1 |  |
| 570-571 | Hybrid System Status | WORD |  |  |  |  |
| 572-573 | Upper Deck Pressure | UINT | inHg |  | 0.01 |  |

## High Priority Auxiliary Data (640-767)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 640 | Cabin Pressure | UINT | inHg | 0 to 35 | 0.001 |  |
| 641 | Cabin Altitude | INT | ft | -1,000 to 30,000 |  |  |

## Normal Priority Pilot Control Inputs (768-895)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 768-775 | Encoder Input | INT[2],BYTE |  |  |  | Indexed by Unit; Steps Moved; X,Y and Switch Positions; Less than 0 = CCW, Greater than 0 = CW |
| 776-783 | Generic Switches | BYTE[5] |  |  |  | Indexed by Unit; Discrete Bits; User Defined For Multiplexing Switches |
| 784 | Speedbrake Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 785 | Cowl Flaps Control Position | UINT | % | 0 to 100 | 0.01 |  |
| 786 | Pitch Trim Control Position | INT | % | -100 to 100 | 0.01 |  |
| 787 | Roll Trim Control Position | INT | % | -100 to 100 | 0.01 |  |
| 788 | Yaw Trim Control Position | INT | % | -100 to 100 | 0.01 |  |
| 789 | Collective Trim Control Position | INT | % | -100 to 100 | 0.01 |  |
| 790 | Anti-Torque Pedals Trim Position | INT | % | -100 to 100 | 0.01 |  |
| 791-798 | Generic Analog Control | UINT | % | 0 to 100 | 0.01 | Indexed by Unit; User Defined |

## Normal Priority Measured Positions (896-1023)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 896 | Speedbrake Position | INT | ° | -90 to 90 | 0.01 | Less than 0 = Down; Greater than 0 = Up |
| 897 | Cowl Flaps Position | UINT | % | 0 to 100 | 0.01 | 100% = Open |
| 898 | Pitch Trim Position | INT | ° | -90 to 90 | 0.01 | Less than 0 = Down; Greater than 0 = Up |
| 899 | Roll Trim Position | INT | ° | -90 to 90 | 0.01 | Less than 0 = Left; Greater than 0 = Right |
| 900 | Yaw Trim Position | INT | ° | -90 to 90 | 0.01 | Less than 0 = Left; Greater than 0 = Right |
| 901 | Pitch Trim Motor Speed | INT | % | -100 to 100 | 0.01 | Less than 0 = Down; Greater than 0 = Up |
| 902 | Roll Trim Motor Speed | INT | % | -100 to 100 | 0.01 | Less than 0 = Left; Greater than 0 = Right |
| 903 | Yaw Trim Motor Speed | INT | % | -100 to 100 | 0.01 | Less than 0 = Left; Greater than 0 = Right |
| 904 | Collective Trim Motor Speed | INT | % | -100 to 100 | 0.01 | Less than 0 = Down; Greater than 0 = Up |
| 905 | Anti-Torque Pedals Trim Motor Speed | INT | % | -100 to 100 | 0.01 | Less than 0 = Left; Greater than 0 = Right |
| 906 | Light Status | BYTE |  |  |  | Discrete Bits |
| 907-910 | Fuel Pump Status | BYTE |  |  |  | Discrete Bits |
| 911 | Fuel Valve Status | BYTE |  |  |  | Discrete Bits |
| 912-919 | Generic Analog Measurement | UINT | % | 0 to 100 | 0.01 | Indexed by Unit; User Defined |

## Normal Priority Flight Data (1024-1151)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 1024 | Pitch Rate | INT | °/sec | -3000 to 3000 | 0.1 | Less than 0 = Down; Greater than 0 = Up |
| 1025 | Roll Rate | INT | °/sec | -3000 to 3000 | 0.1 | Less than 0 = Left; Greater than 0 = Right |
| 1026 | Yaw Rate | INT | °/sec | -3000 to 3000 | 0.1 | Less than 0 = Left; Greater than 0 = Right |
| 1027 | Turn Rate | INT | °/sec | -3000 to 3000 | 0.1 | Less than 0 = Left; Greater than 0 = Right |
| 1028 | Static Pressure | UINT | inHg |  | 0.001 |  |
| 1029 | Pitot Pressure | UINT | inHg |  | 0.001 |  |
| 1030 | Total Air Temperature | INT | °C | -300 to 300 | 0.01 |  |
| 1031 | Static Air Temperature | INT | °C | -300 to 300 | 0.01 |  |
| 1032 | Density Altitude | DINT | ft | -1,000 to 60,000 |  |  |
| 1033 | True Altitude | DINT | ft | -1,000 to 60,000 |  |  |
| 1034 | GPS Altitude | DINT | ft | -1,000 to 60,000 |  |  |
| 1035 | Wind Speed | UINT | knots | 0 to 2000 | 0.1 |  |
| 1036 | Wind Direction | UINT | ° | 0 to 360 | 0.01 | Magnetic |

## Normal Priority Navigation Data (1152-1279)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 1152 | Next Waypoint Identifier | CHAR[5] |  |  |  |  |
| 1153 | Next Waypoint Latitude | FLOAT | ° | -90 to 90 |  |  |
| 1154 | Next Waypoint Longitude | FLOAT | ° | -180 to 180 |  |  |
| 1155 | Next Waypoint Altitude | DINT | ft | -1000 to 60,000 |  |  |
| 1156 | Next Waypoint ETA | USHORT[3] | UTC |  |  | Hour, Min, Sec |
| 1157 | Next Waypoint ETE | USHORT[3] |  |  |  | Hour, Min, Sec |
| 1158 | Waypoint Identifier | CHAR[5] |  |  |  | Indexed by Waypoint |
| 1159 | Waypoint Latitude | FLOAT | ° | -90 to 90 |  | Indexed by Waypoint |
| 1160 | Waypoint Longitude | FLOAT | ° | -180 to 180 |  | Indexed by Waypoint |
| 1161 | Waypoint Altitude | DINT | ft | -1000 to 60,000 |  | Indexed by Waypoint |
| 1162 | Waypoint ETA | USHORT[3] | UTC |  |  | Indexed by Waypoint; Hour, Min, Sec |
| 1163 | Waypoint ETE | USHORT[3] |  |  |  | Indexed by Waypoint; Hour, Min, Sec |
| 1164 | Waypoint, Distance To | UINT | nm |  |  | Indexed by Waypoint |
| 1165 | Waypoint Minimum Altitude | DINT | ft | -1000 to 60,000 |  | Indexed by Waypoint |
| 1166 | Waypoint Minimum Flight Level | UINT |  |  |  | Indexed by Waypoint |
| 1167 | Waypoint Minimum Radar Level | UINT |  |  |  | Indexed by Waypoint |
| 1168 | Waypoint Maximum Altitude | DINT | ft | -1000 to 60,000 |  | Indexed by Waypoint |
| 1169 | Waypoint Maximum Flight Level | UINT |  |  |  | Indexed by Waypoint |
| 1170 | Waypoint Maximum Radar Level | UINT |  |  |  | Indexed by Waypoint |
| 1171 | Waypoint Planned Altitude | DINT | ft | -1000 to 60,000 |  | Indexed by Waypoint |
| 1172 | Waypoint Reserved |  |  |  |  | Indexed by Waypoint |
| 1173 | Destination Identifier | CHAR[5] |  |  |  |  |
| 1174 | Destination Latitude | FLOAT | ° | -90 to 90 |  |  |
| 1175 | Destination Longitude | FLOAT | ° | -180 to 180 |  |  |
| 1176 | Destination Altitude | DINT | ft | -1000 to 60,000 |  |  |
| 1177 | Destination ETA | USHORT[3] | UTC |  |  | Hour, Min, Sec |
| 1178 | Destination ETE | USHORT[3] |  |  |  | Hour, Min, Sec |
| 1179 | Track Error Angle |  | ° |  |  |  |
| 1180-1215 | Reserved |  |  |  |  |  |
| 1216-1219 | VHF Com Frequency | UINT | MHz |  | 0.01 | Indexed by 0=Current, 1=Standby, >1 = Memory Locations |
| 1220-1223 | VOR/ILS Frequency | UINT | ° | 0 to 359 |  | Indexed by 0=Current, 1=Standby, >1 = Memory Locations |
| 1224-1227 | VOR/ILS Identifier | CHAR[5] |  |  |  |  |
| 1228-1231 | Actual VOR Radial | UINT | ° | 0 to 359.9 | 0.1 |  |
| 1232-1235 | Selected VOR Radial | UINT | ° | 0 to 359.9 | 0.1 |  |
| 1236 | Transponder Code | USHORT[4] |  |  |  |  |
| 1240 | Auto Pilot / FD Mode | WORD |  |  |  | Indexed by 0=AP Mode, 1=Horizontal Mode, 2=Vertical Mode, 255=Status |

## Normal Priority Engine / Aircraft System Data (1280-1407)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 1280-1281 | Cylinder Head Temperature | UINT | °C |  | 0.1 | Indexed by Cylinder |
| 1282-1283 | Exhaust Gas Temperature | UINT | °C |  | 0.1 | Indexed by Cylinder |
| 1284-1285 | Cylinder Head Temp. Rate of Change | UINT | °C/Min |  | 0.1 | Indexed by Cylinder |
| 1286-1287 | Cylinder Head Temp. Deviation | UINT | °C |  | 0.1 |  |
| 1288-1289 | Exhaust Gas Temp.  Rate of Change | UINT | °C/Min |  | 0.1 | Indexed by Cylinder |
| 1290-1291 | Exhaust Gas Temp. Deviation | UINT | °C |  | 0.1 |  |
| 1292-1293 | Carburetor Temperature | UINT | °C |  | 0.1 |  |
| 1294-1297 | Electrical Bus Voltage | UINT | V |  | 0.1 |  |
| 1298-1301 | Electrical Bus Current | UINT | A |  | 0.1 |  |
| 1302-1305 | Generator / Alternator Voltage | UINT | V |  | 0.1 |  |
| 1306-1309 | Generator / Alternator Current | UINT | A |  | 0.1 |  |
| 1310-1311 | Engine Power | UINT | % |  | 0.1 |  |
| 1312-1313 | Total Engine Time | UINT | Hours |  | 0.1 | Indexed by Flight; Index 0 = Total, 1 = last flight, reverse chronological order from there |
| 1314-1315 | Total Engine Time (Tach) | UINT | Hours |  | 0.1 | Indexed by Flight; Index 0 = Total, 1 = last flight, reverse chronological order from there |
| 1316-1317 | Gearbox Speed | UINT | RPM |  |  |  |
| 1318-1319 | Gearbox Oil Pressure Switch | BYTE |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 1320-1321 | Gearbox Oil Temperature Switch | BYTE |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 1322-1323 | Gearbox Oil Quantity Switch | BYTE |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 1324-1325 | Hydraulic Pressure Switch | BYTE |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 1326-1327 | Hydraulic Temperature Switch | BYTE |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 1328-1329 | Hydraulic Fluid Quantity Switch | BYTE |  |  |  | 0 = Normal; -1 = Low; 1 = High |
| 1330-1331 | Gearbox Oil Pressure | UINT | psi |  | 0.01 |  |
| 1332-1333 | Gearbox Oil Temperature | UINT | °C |  | 0.1 |  |
| 1334-1335 | Gearbox Oil Quantity | UINT | % | 0 to 100 | 0.01 |  |
| 1336-1337 | Hydraulic Pressure | UINT | psi |  | 0.01 |  |
| 1338-1339 | Hydraulic Temperature | UINT | °C |  | 0.1 |  |
| 1340-1341 | Hydraulic Fluid Quantity | UINT | % | 0 to 100 | 0.01 |  |
| 1342-1345 | Tire Pressure | UINT | psi |  | 0.01 |  |
| 1346-1349 | Strut Pressure | UINT | psi |  | 0.01 |  |
| 1350 | Flight Time | UINT | Hours |  | 0.1 | Indexed by Flight; Index 0 = last flight, reverse chronological order from there |

## Normal Priority Auxiliary Data (1408-1535)

| ID | Parameter | Type | Units | Range | Mult | Notes |
|---|---|---|---|---|---|---|
| 1408 | Time | USHORT[3],UINT | UTC |  |  | Hour, Min, Sec, mSec |
| 1409 | Date | UINT,USHORT[2] |  |  |  | Year, Month, Day |
| 1410 | Time Zone | SHORT | Hours | -12 to 12 | 0.1 |  |
| 1411 | Cabin Temperature | UINT | °C |  | 0.1 |  |
| 1412 | Panel Dimmer Level | USHORT | % | 0 to 100 |  |  |
| 1413 | Longitudinal Center of Gravity | UINT | %MAC | 0 to 100 | 0.1 |  |
| 1414 | Lateral Center of Gravity | INT | % | -100 to 100 | 0.1 |  |
| 1415 | Aircraft Identifier | CHAR[5] |  |  |  |  |
| 1416 | Aircraft Type | CHAR[5] |  |  |  |  |

---

_230 parameters across 12 groups. Generated by `tools/gen_param_reference.py` from `src/canfix.json` (version 0.7). Do not edit by hand -- edit the master spreadsheet and regenerate._
