# CAN-FIX Protocol Specification

**Status:** Open Source Specification — Creative Commons Licensed  
**Format:** Sphinx documentation source (builds to PDF and HTML)  
**Scope:** Experimental Amateur-Built (E-AB) Aircraft Avionics

---

## What This Is

This repository contains the **authoritative specification** for the CAN-FIX communication protocol — the CAN bus implementation of the Flight Information eXchange (FIX) protocol family. CAN-FIX defines how avionics nodes on an aircraft CAN network identify themselves, publish flight data parameters, and consume data from other nodes.

The specification is licensed under Creative Commons, meaning anyone can read, implement, modify, and distribute compliant devices without licensing fees or vendor lock-in.

## Read the Specification Online

- **Full specification (web):** <https://billmallard.github.io/canfix-spec/> — the complete document, rebuilt automatically from this repository on every push.
- **Wiki (quick reference):** <https://github.com/billmallard/canfix-spec/wiki> — a friendly companion with a [parameter quick-reference](https://github.com/billmallard/canfix-spec/wiki/Parameter-Reference) table, a [frame-format](https://github.com/billmallard/canfix-spec/wiki/Frame-Format) cheat-sheet, and an [implementer's quick-start](https://github.com/billmallard/canfix-spec/wiki/Implementing-a-Node).
- **PDF:** build it locally with `make latexpdf` (see [Building the Documentation](#building-the-documentation)).

## What CAN-FIX Defines

- **Parameter namespace:** Every flight data value (airspeed, altitude, heading, GPS position, engine temperatures, control surface positions, etc.) has a named identifier. Parameters are organized by type and support multiple simultaneous sources (e.g., two independent EGT sensors for two engines).
- **Frame structure:** How 11-bit CAN identifiers are allocated across parameter types, node IDs, and index bytes for multi-instance data.
- **Node types and device IDs:** Standard device type identifiers so nodes can announce their role on the network.
- **Multi-source design:** The protocol explicitly accommodates redundant nodes publishing the same parameter type using separate identifier ranges, avoiding CAN arbitration conflicts.
- **Data types:** float, int, bool, string with defined units and ranges per parameter.

## Parameter Coverage

The specification covers the full avionics parameter set for a modern aircraft:

| Domain | Example Parameters |
|---|---|
| Navigation | LAT, LONG, ALT, IAS, TAS, GS, heading, track |
| AHRS | Pitch, roll, yaw rate, accelerations |
| Engine (×2) | RPM, MAP, EGT (×N cylinders), CHT, oil temp/pressure, fuel flow |
| Control surfaces | Pitch, roll, yaw, flap, trim positions |
| Electrical | Bus voltage, current, alternator status |
| Fuel | Quantity (×N tanks), flow, pressure |
| COM/NAV radios | Active/standby frequencies |
| Systems | Gear position, door status, general annunciators |

## Repository Contents

| Path | Description |
|---|---|
| `src/CAN-FIX.ods` | **Master parameter spreadsheet** — the source of truth for all parameter definitions |
| `src/canfix.json` | Machine-readable parameter definitions (*generated* from `CAN-FIX.ods`) |
| `src/canfix.xml` | XML form of parameter definitions (*generated* from `CAN-FIX.ods`) |
| `src/parameters.rst` | Human-readable parameter list (*generated* from `CAN-FIX.ods`) |
| `src/framedef.rst` | CAN frame format specification |
| `src/datatypes.rst` | Data type definitions |
| `src/physical.rst` | Physical layer requirements (wiring, termination, bit rate) |
| `src/requirements.rst` | Protocol requirements |
| `src/practices.rst` | Recommended implementation practices |
| `tools/gen_param_reference.py` | Generates the wiki parameter quick-reference from `canfix.json` |
| `tools/sync_wiki.sh` | Mirrors `wiki/` to the GitHub wiki clone for publishing |

> **Editing parameters:** change `src/CAN-FIX.ods` (the master), then regenerate
> the derived files with the commands below. Do not hand-edit `canfix.json`,
> `canfix.xml`, or `parameters.rst` — they are overwritten on every build.

## Building the Documentation

Requires Python with Sphinx and supporting packages:

```bash
sudo pip install pyexcel pyexcel-ods sphinx
sudo apt install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texlive-xetex latexmk
cd src
python canfix_json.py   # regenerate canfix.json   from CAN-FIX.ods
python canfix_xml.py    # regenerate canfix.xml     from CAN-FIX.ods
python parameters.py    # regenerate parameter_list from CAN-FIX.ods
make latexpdf           # builds PDF  -> src/_build/latex
make html               # builds HTML -> src/_build/html
```

The web specification at <https://billmallard.github.io/canfix-spec/> is built
and published automatically by GitHub Actions (`.github/workflows/docs.yml`) on
every push to `master`, so the online copy always matches the repository.

## Important Disclaimer

> This specification is developed for Experimental Amateur-Built aircraft use only.  
> It is not FAA-approved avionics software or a certified communication standard.  
> All implementations are the builder's responsibility.
