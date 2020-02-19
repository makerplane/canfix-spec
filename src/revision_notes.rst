Revision Notes
==============
.. |date| date:: %B %d, %Y

Version 0.7 - |date|
  * Move specification to Sphinx
  * Move Node Specific Messages to a higher priority than the Two-Way Channels
  * Change Appendix to be Recommended Practices
  * Change Encoder Input data type to INT[2],BYTE.  This adds another axis
    to the encoder as well a byte for discrete switches or buttons.
  * Change Units for Static and Pitot pressures to 0.001 inHg from 0.01 inHg
  * Change Range for Pitch Angle and Angle of Attack to -90 to 90
  * Change waypoint identifier's type from CHAR[4] to CHAR[5]
  * Add milliseconds to Time
  * Add decimal point to Time Zone to account for 1/2 hour timezones
  * Add Tachometer Time parameter
  * Add Aircraft Type parameter
  * Add Selected Airspeed Parameter
  * Add Upper Deck Pressure parameter
  * Add Serial Number to Node Status Message
  * Add Node Description Message
  * Add Paramter Setting function description
  * Add GPS Altitude
  * Change count of Landing Gear Position Switches from 1 to 3
  * Remove Comm Frequency "Set" Parameters (IDs 1216 - 1219)
  * Remove VOR / ILS Frequency "Set" Parameters (IDs 1224 = 1227)
  * Remove Altimeter Setting "Set" Parameter (ID 400)
  * Add General Requirements chapter
  * Change Bit Rate Set message error code to 0xFF
  * Change Node ID Set message response
  * General style, grammer and spelling fixes


Version 0.6 - June 6, 2016
  * Added some device types and reworded some of the descriptions in the appendix.
  * Changed Firmware Update command to return error on failure.
  * Change Index on Encoder Input from none to 'Unit'
  * Changed the count of some of the high priority pilot inputs
  * Changed Generic Switch Count from 8 to 2.  This caused some identifiers to change
  * Add min and max aux data to pitch and roll
  * Add restriction ranges to engine and prop RPM
  * Add encoders, switches and analogs to Normal Priority Pilot Inputs

Version 0.5 - April 17, 2013
  * Added new, better looking diagrams from John Nicol
  * Changed the response of the Node Configuration Command
  * Added VOR/LOC Control Commands, Encoder Input and Generic Analog Control
    Parameters to the High Priority Pilot Control Inputs Group.  Also added
    some of these to the Normal Priority Pilot Control Inputs Group.
  * Added a parameter to separate setting and reporting of the Altimeter setting
  * Added OBI Flags parameter
  * Reduced the number of engines from four to two
  * Reduced the number of navigation information parameters from four to one
  * Separated setting and reporting for radio frequencies
  * Added restricted ranges to RPM parameters

Version 0.4 - January 17, 2013
  * Moved discrete pilot input controls higher in the priority list.
  * Added parameters for Hybrid/Electric propulsion data.
  * Added parameters for ADS-B Traffic.
  * Changed all the altitudes to Double Integers and removed the -1,000 ft offset.
  * Changed all the altitudes to 1 ft resolution instead of 10 ft.
  * Added an appendix with suggested device type codes.
  * Added a section on the Revision process.
  * Clarifications on Node Alarms and Node Specific Messages.
  * Lot's of typos and misspellings fixed.
  * Other minor clarifications.
