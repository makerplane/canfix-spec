# Background: CANaerospace and why CAN-FiX exists

CAN-FiX was born from Phil Birkelbach's frustrations with
**CANaerospace**, the 1998 aviation CAN protocol it most resembles.
This page gives the history: what CANaerospace is, where it went, and
what CAN-FiX deliberately did differently. (Researched 2026-07-05;
sources at the bottom.)

## What CANaerospace is

CANaerospace is an application-layer protocol over CAN, created in
**1998 by Michael Stock** of Stock Flight Systems — an aerospace
engineering firm in Farchach (Berg, Bavaria) specialized in flight-test
instrumentation. Design highlights:

- Big-endian, **self-identifying messages**: 8-byte payload = 4-byte
  header (Node-ID, data type, service code, message code) + 4 bytes of
  data — half of every frame is metadata.
- Priority-ordered logical channels (emergency events, node services,
  normal operation data, user-defined, debug) over a standard
  identifier distribution (IDs 300–1799).
- The same parameter may be sent with **different data types**, and
  **alternative identifier distributions may coexist** on one bus.
- Free to download and use — genuinely open for its era.

The flexibility was deliberate: in a flight-test lab you want to put
arbitrary new parameters on the bus quickly.

## Its pedigree

- **NASA AGATE (2001):** published by NASA as the databus standard of
  the Advanced General Aviation Transport Experiments consortium, which
  carried it into research aircraft, simulators and UAVs worldwide.
- **Rotax iS engines (2012–present):** the Rotax 912iS/915iS ECUs speak
  CANaerospace — it ships in essentially every new injected-Rotax
  installation today.
- **ARINC 825 (2007–present):** an AEEC working group (Airbus, Boeing,
  GE, Rockwell Collins, Vector, and Stock Flight Systems itself) used
  CANaerospace as the basis for ARINC 825, the certified-aviation CAN
  standard — still actively revised, with CAN FD in later revisions.

## Current status: frozen, not failed

The open spec's last revision is **V1.7 (2006)** — two decades
untouched, with no active steward. stockflightsystems.com survives as a
legacy brochure site; the commercial products (Rotax iS EMU, MT
propeller control, CANaerospace loggers) are sold today by RS Flight
Systems GmbH of Berg — likely a Reiser/Stock venture carrying the
product line forward (probable, not confirmed). The certified world
absorbed CANaerospace into ARINC 825; the protocol itself keeps flying
inside Rotax ECUs.

## Why CAN-FiX — Birkelbach, August 2013

The primary source is the MakerPlane forum thread
[*"What's wrong with CANaerospace?"*](http://makerplane.org/forum/viewtopic.php?t=216):

> "With it you can send the same parameter over the bus with different
> data types. This is a great feature if what you are after is
> flexibility. **The problem with flexibility in a communication
> protocol is that it forces complexity at the end points.**"

> "CA also allows for multiple identifier distributions to exist on the
> bus at the same time. It would be up to the end points to determine
> if the data that they are receiving is what they think it is."

> "CAN-FIX is a much more rigid protocol… **There is only one way to
> send airspeed on CAN-FIX.**"

Concretely, CAN-FiX:

- replaced the data-type byte with an **index byte** — up to 256
  instances of a parameter (all your EGTs) instead of type negotiation
  (see [Frame Format](Frame-Format));
- pinned **one canonical encoding per parameter** (see
  [Data Types](Data-Types)), so a $2 microcontroller needs no
  type-handling layer;
- put **metadata on the bus** (V-speeds, ranges, alarm setpoints);
- targeted the Experimental/Amateur-Built ecosystem under a Creative
  Commons license.

A fair framing: CANaerospace optimizes for the flight-test lab
(flexibility first); CAN-FiX optimizes for a fixed avionics ecosystem
of heterogeneous cheap nodes (rigidity first). Both are rational in
their own domains.

## Family tree

```
Bosch CAN (1986, automotive)
 ├─ CANopen / DeviceNet (industrial)
 ├─ NMEA 2000 (marine)
 └─ CANaerospace (1998, GA / research / flight test)
     ├─ ARINC 825 (2007, certified transport; CAN FD later)
     ├─ UAVCAN (2014) ─┬─ DroneCAN (2022)
     │                 └─ Cyphal (2022)
     └─ CAN-FiX (~2012, MakerPlane — experimental aviation)
```

## Sources

- [Wikipedia — CANaerospace](https://en.wikipedia.org/wiki/CANaerospace)
- [MakerPlane forum — "What's wrong with CANaerospace?" (Aug 2013)](http://makerplane.org/forum/viewtopic.php?t=216)
- [CAN-FiX Overview (makerplane.org)](https://makerplane.org/can-fix-overview/)
- [CANaerospace V1.7 specification (PDF)](https://www.stockflightsystems.com/tl_files/downloads/canaerospace/canas_17.pdf)
- [Stock Flight Systems — ARINC 825 presentation (PDF)](https://files.stockflightsystems.com/_5_Arinc_825/ARINC825_Presentation.pdf)
- [arinc-825.com — The ARINC825 Standard](https://www.arinc-825.com/the-arinc825-standard/)
- [Vector application note — CAN-based protocols in Avionics (PDF)](https://cdn.vector.com/cms/content/know-how/_application-notes/canopen/AN-ION-1-0104_CAN-based_protocols_in_Avionics.pdf)
- [RS Flight Systems](https://www.rs-flightsystems.com/)
- [Wikipedia — Cyphal](https://en.wikipedia.org/wiki/Cyphal)
- [Zubax — Cyphal vs DroneCAN](https://zubax.com/blog/on-the-key-differences-between-cyphal-and-dronecan-formerly-uavcan/2038)
