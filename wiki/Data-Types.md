# Data Types

How the 1-5 data bytes of a [Normal Data frame](Frame-Format#normal-data-frame)
are encoded. The full text is in the
[Data Types chapter](https://billmallard.github.io/canfix-spec/datatypes.html).

Each parameter has a **fixed** data type -- there is no type indicator in the
message itself (this is deliberate, to keep small 8-bit nodes simple). Fixed-point
integers with an assumed multiplier are strongly preferred over floating point.

| Type | Description |
|---|---|
| `CHAR` | 8-bit ASCII character |
| `BYTE` | 8 bits (discrete states, switch positions, commands) |
| `WORD` | 16 bits (discrete states, 16 bit wide) |
| `SHORT` | 8-bit signed integer |
| `USHORT` | 8-bit unsigned integer |
| `INT` | 16-bit signed integer |
| `UINT` | 16-bit unsigned integer |
| `DINT` | 32-bit signed integer |
| `UDINT` | 32-bit unsigned integer |
| `FLOAT` | 32-bit IEEE 754 floating point |

## Key rules

- **Little-endian.** Multi-byte values are sent least-significant byte first
  (Byte 3 of the frame is the LSB).
- **Assumed decimal places.** Most quantities are integers scaled by a
  **multiplier**. The engineering value is `raw x multiplier`. Example: a
  parameter with units `%`, multiplier `0.01` and a raw `INT` of `5000` means
  `50.00 %`. The multiplier for each parameter is in the
  [Parameter Quick-Reference](Parameter-Reference).
- **Arrays and mixed types.** A parameter may pack several values into the five
  data bytes. Time, for example, is three `USHORT`s (hours, minutes, seconds);
  a date could be `UINT, USHORT[2]` (year, then month and day). The packing is
  given in each parameter's definition -- the array/mixed forms show up in the
  **Type** column of the quick-reference (e.g. `INT[2],BYTE`).
- **64-bit floats** are not a type; when extra precision is needed a parameter is
  sent across two messages, defined per parameter (rarely needed).
- **Discrete bits.** `BYTE`/`WORD` parameters often carry independent bit flags
  (switch up/down, mode engaged). The bit meanings are in the parameter's
  **Notes** in the [Parameter Quick-Reference](Parameter-Reference) and in the
  [Parameters chapter](https://billmallard.github.io/canfix-spec/parameters.html).

---

See also: **[Frame Format](Frame-Format)** · **[Parameter Quick-Reference](Parameter-Reference)**
