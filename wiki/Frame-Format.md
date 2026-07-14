# Frame Format

A quick reference for the CAN-FiX frame layouts. The full, authoritative text is
in the [Frame Definitions chapter](https://billmallard.github.io/canfix-spec/framedef.html)
of the specification.

CAN-FiX uses the **CAN 2.0B base frame** -- an **11-bit identifier** and up to
**8 data bytes**. The identifier both names the message *and* sets its priority:
**lower ID = higher priority** (it wins bus arbitration). All multi-byte values
in the data field are **little-endian** (least-significant byte first).

## How the 11-bit ID space is divided

The identifier tells you which of the four frame formats you are looking at:

| ID range | Frame type | Format |
|---|---|---|
| 1 - 255 | **Node Alarms** (highest priority) | [Node Alarm](#node-alarm-frame) |
| 256 - 1759 | **Parameter data** (the bulk of traffic) | [Normal Data](#normal-data-frame) |
| 1760 - 2015 | **Node-Specific messages** (config, ID, firmware...) | [Node-Specific](#node-specific-frame) |
| 2016 - 2047 | **Two-way connection channels** | (point-to-point payloads) |

Within the parameter-data range, IDs are grouped by category and priority. These
are the groups used by the [Parameter Quick-Reference](Parameter-Reference):

| ID range | Group |
|---|---|
| 256 - 319 | High Priority Pilot Control Inputs |
| 320 - 383 | High Priority Measured Positions |
| 384 - 447 | High Priority Flight Data |
| 448 - 511 | High Priority Navigation Data |
| 512 - 639 | High Priority Engine / Aircraft System Data |
| 640 - 767 | High Priority Auxiliary Data |
| 768 - 895 | Normal Priority Pilot Control Inputs |
| 896 - 1023 | Normal Priority Measured Positions |
| 1024 - 1151 | Normal Priority Flight Data |
| 1152 - 1279 | Normal Priority Navigation Data |
| 1280 - 1407 | Normal Priority Engine / Aircraft System Data |
| 1408 - 1535 | Normal Priority Auxiliary Data |

## Normal Data frame

The heart of the protocol -- a parameter value update. Frame ID = the parameter
ID (see [Parameter Quick-Reference](Parameter-Reference)).

| Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 |
|---|---|---|---|---|---|---|---|
| Node | Index | Function Code | Data LSB | Data | Data | Data | Data MSB |

- **Node** -- the Node ID of the sender (1-255, unique on the network).
- **Index** -- selects an instance of an indexed parameter (e.g. EGT per
  cylinder: 0, 1, 2...). Zero when the parameter is not indexed.
- **Function Code** -- meta data selector + quality flags (see below).
- **Data** -- 1 to 5 bytes, little-endian, encoded per the parameter's
  [data type](Data-Types).

### Function / Status Code byte

A value of **0** means "ordinary value update, good quality" -- the common case.

| Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
|---|---|---|---|---|---|---|---|
| Meta Data 3 | Meta Data 2 | Meta Data 1 | Meta Data 0 | Future | Failure | Quality | Annunciate |

- **Annunciate (bit 0)** -- the value is out of range and should be annunciated
  (e.g. an alarm set point was exceeded).
- **Quality (bit 1)** -- the sender suspects the data; show it flagged (like an
  attitude-indicator flag).
- **Failure (bit 2)** -- the sender knows the data is bad; do not show it,
  indicate the failure.
- **Meta Data (bits 4-7)** -- when non-zero, the data field carries one of 15
  meta-data values for this parameter (alarm set points, V-speeds, scaling)
  instead of the parameter value itself. Meta data shares the parameter's units,
  range and data type. Value 0 = the parameter itself.

> If Quality or Failure is set, use an alternate source for the value if one is
> available.

## Node Alarm frame

Identifiers **1-255**: a real-time alarm from the node whose ID equals the frame
identifier. These are the highest-priority messages on the bus -- use them for
millisecond-critical notifications (e.g. coordinating a fly-by-wire failover),
**not** for annunciating a low oil pressure to the pilot.

| Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 |
|---|---|---|---|---|---|---|---|
| Alarm Code LSB | Alarm Code MSB | Data LSB | Data | Data | Data | Data | Data MSB |

The 16-bit alarm code and the six data bytes are **not** defined by the
specification -- their meaning is left to the implementer.

## Node-Specific frame

Identifiers **1760-2015**: configuration and management messages. The sender's
Node ID is implied by the identifier:

```
Node ID = Frame ID - 1760
```

| Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 |
|---|---|---|---|---|---|---|---|
| Control Code | Data LSB | Data | Data | Data | Data | Data | Data MSB |

For most of these, **Byte 1 is the destination node** (0 = broadcast to all).

### Control codes

| Code | Message | Mandatory | Responds to broadcast |
|---|---|---|---|
| 0 | Node Identification | Yes | Yes |
| 1 | Bit Rate Set | Yes | Yes |
| 2 | Node ID Set | Yes | No |
| 3 | Disable Parameter | Yes | Yes |
| 4 | Enable Parameter | Yes | No |
| 5 | Node Report | Yes | Yes |
| 6 | Node Status Information | No | N/A |
| 7 | Update Firmware | No | No |
| 8 | Two-Way Connection Request | No | No |
| 9 | Node Configuration Set | No | No |
| 10 | Node Configuration Query | No | No |
| 11 | Node Description | No | No |
| 12 - 19 | Parameter Set (8 codes cover index ranges 0-255) | No | N/A |
| 20 - 127 | Reserved for future use | | |
| 128 - 255 | User defined | No | |

**Bit rates** (Bit Rate Set, byte 2): `1` = 125 kbps, `2` = 250 kbps,
`3` = 500 kbps, `4` = 1 Mbps.

See the [Frame Definitions chapter](https://billmallard.github.io/canfix-spec/framedef.html)
for the per-message payloads (Node Identification response, Parameter Set bit
layout, firmware/channel handshakes, etc.).

---

See also: **[Data Types](Data-Types)** · **[Parameter Quick-Reference](Parameter-Reference)** · **[Implementing a Node](Implementing-a-Node)**
