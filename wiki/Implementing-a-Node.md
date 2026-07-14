# Implementing a Node

A practical get-started checklist for building a CAN-FiX node. It summarizes the
specification; the binding rules are in the
[Requirements](https://billmallard.github.io/canfix-spec/requirements.html) and
[Best Practices](https://billmallard.github.io/canfix-spec/practices.html)
chapters, with frame details in
[Frame Definitions](https://billmallard.github.io/canfix-spec/framedef.html).

## 1. Pick a Node ID and bit rate

- Choose a **Node ID** in **1-255**, unique on the network (0 is the broadcast
  address, never a real node).
- Use the **CAN 2.0B base frame** (11-bit identifier) only.
- Default to a network **bit rate** the installation agrees on -- the protocol
  defines `125k / 250k / 500k / 1M` and a [Bit Rate Set](Frame-Format#control-codes)
  message to change it.
- Read the bus as you transmit (standard CAN arbitration); a lower identifier
  always wins, so your most critical parameters belong at lower IDs.

## 2. Produce your parameters

For each thing your node measures:

1. Find (or choose) its parameter ID in the
   [Parameter Quick-Reference](Parameter-Reference). The **frame ID is the
   parameter ID**.
2. Build the [Normal Data frame](Frame-Format#normal-data-frame):
   - Byte 0 = your Node ID
   - Byte 1 = Index (0 if the parameter is not indexed)
   - Byte 2 = Function Code (0 for a good-quality value)
   - Bytes 3-7 = the value, **little-endian**, in the parameter's
     [data type](Data-Types) (`raw = engineering / multiplier`)
3. Transmit it periodically. Send only what your node is responsible for.

**Quality matters.** When a reading is suspect or failed, set the **Quality** or
**Failure** bit in the Function Code rather than sending a silently-wrong value.
Set **Annunciate** when a value crosses an alarm threshold. See
[the Function/Status code](Frame-Format#function--status-code-byte).

**Send your meta data.** If a parameter has alarm set points or ranges (e.g. oil
pressure limits, V-speeds), the *measuring* node should transmit them as meta data
(Function Code meta-data bits 1-15) so every display stays consistent without
separate configuration. This is a core design principle of CAN-FiX.

## 3. Handle the mandatory node-specific messages

Every node **must** respond to these [control codes](Frame-Format#control-codes)
(Node-Specific frames, ID = `1760 + your Node ID`):

| Code | Message | What your node must do |
|---|---|---|
| 0 | Node Identification | Reply with the spec revision you implement (`0x01` for this spec); optionally follow with a [Node Description](https://billmallard.github.io/canfix-spec/framedef.html#node-description) string |
| 1 | Bit Rate Set | Change CAN bit rate immediately and permanently |
| 2 | Node ID Set | Change your Node ID, then announce success on the new ID |
| 3 | Disable Parameter | Stop broadcasting the named parameter |
| 4 | Enable Parameter | Resume broadcasting the named parameter |
| 5 | Node Report | Immediately send every parameter you own, plus its meta data |

Optional messages (firmware update, two-way channels, node configuration,
node status, point-to-point Parameter Set) are described in the
[Frame Definitions chapter](https://billmallard.github.io/canfix-spec/framedef.html).

## 4. Consume what you need

To use data from the bus, just listen for the relevant parameter IDs and decode
per [Data Types](Data-Types). Respect the **Quality / Failure** flags -- fall
back to an alternate source when set. Remember that **one parameter should have
one producer**: if two nodes broadcast the same parameter they will conflict, so
use Disable/Enable Parameter (or a Node Report at startup) to resolve duplicates.

## Reference implementations

- **C / Arduino:** the [can-fix-arduinolib](https://github.com/makerplane/can-fix-arduinolib)
  library implements the node-specific protocol and parameter framing.
- **Python:** the [python-canfix](https://github.com/birkelbach/python-canfix)
  package (and MakerPlane's FIX-Gateway, which bridges CAN-FiX to other
  transports) are useful references for decode/encode.

---

See also: **[Frame Format](Frame-Format)** · **[Data Types](Data-Types)** · **[Parameter Quick-Reference](Parameter-Reference)**
