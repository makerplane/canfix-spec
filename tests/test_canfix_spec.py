"""
Structural validation tests for canfix.json.

Run from the repo root:
    python -m pytest tests/ -v
"""
import json
import os
import pytest

SPEC_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "canfix.json")

# Base types per the CAN-FIX spec; compound types (e.g. INT[2],BYTE) are split on ','
# and array suffixes (e.g. CHAR[2]) are stripped before lookup.
VALID_BASE_TYPES = {"BYTE", "WORD", "SHORT", "USHORT", "FLOAT", "DOUBLE", "CHAR", "BOOL",
                    "INT", "UINT", "LONG", "ULONG", "DINT", ""}


@pytest.fixture(scope="module")
def spec():
    with open(SPEC_PATH, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def parameters(spec):
    return spec["parameters"]


@pytest.fixture(scope="module")
def groups(spec):
    return spec["groups"]


@pytest.fixture(scope="module")
def status(spec):
    return spec["status"]


# ── Top-level structure ────────────────────────────────────────────────────────

class TestTopLevelStructure:
    def test_has_parameters_key(self, spec):
        assert "parameters" in spec

    def test_has_groups_key(self, spec):
        assert "groups" in spec

    def test_has_status_key(self, spec):
        assert "status" in spec

    def test_parameter_count(self, parameters):
        assert len(parameters) == 230, (
            f"Expected 230 parameters, got {len(parameters)}"
        )

    def test_group_count(self, groups):
        assert len(groups) == 17

    def test_status_count(self, status):
        assert len(status) == 10


# ── Parameter required fields ─────────────────────────────────────────────────

class TestParameterRequiredFields:
    def test_all_have_id(self, parameters):
        missing = [p.get("name", "?") for p in parameters if "id" not in p]
        assert not missing, f"Parameters missing 'id': {missing}"

    def test_all_have_name(self, parameters):
        missing = [p.get("id", "?") for p in parameters if "name" not in p or not p["name"]]
        assert not missing, f"Parameters missing 'name': {missing}"

    def test_all_have_count(self, parameters):
        missing = [p.get("id", "?") for p in parameters if "count" not in p]
        assert not missing, f"Parameters missing 'count': {missing}"

    def test_all_have_type(self, parameters):
        missing = [p.get("id", "?") for p in parameters if "type" not in p]
        assert not missing, f"Parameters missing 'type': {missing}"

    def test_all_have_index_key(self, parameters):
        missing = [p.get("id", "?") for p in parameters if "index" not in p]
        assert not missing, f"Parameters missing 'index' key (may be null): {missing}"

    def test_all_have_metadata_key(self, parameters):
        missing = [p.get("id", "?") for p in parameters if "metadata" not in p]
        assert not missing, f"Parameters missing 'metadata' key: {missing}"


# ── Parameter ID constraints ──────────────────────────────────────────────────

class TestParameterIds:
    def test_ids_are_integers(self, parameters):
        non_int = [p["name"] for p in parameters if not isinstance(p["id"], int)]
        assert not non_int, f"Non-integer IDs: {non_int}"

    def test_ids_are_unique(self, parameters):
        ids = [p["id"] for p in parameters]
        seen = set()
        dupes = []
        for i in ids:
            if i in seen:
                dupes.append(i)
            seen.add(i)
        assert not dupes, f"Duplicate parameter IDs: {dupes}"

    def test_ids_in_parameter_range(self, parameters):
        # Parameters live in IDs 256–1759 per the CAN-FIX spec
        out_of_range = [p["id"] for p in parameters if not (256 <= p["id"] <= 1759)]
        assert not out_of_range, f"Parameter IDs outside 256–1759: {out_of_range}"

    def test_ids_sorted_ascending(self, parameters):
        ids = [p["id"] for p in parameters]
        assert ids == sorted(ids), "Parameter list is not sorted by ID"


# ── Parameter type constraints ────────────────────────────────────────────────

class TestParameterTypes:
    def test_types_are_strings(self, parameters):
        non_str = [p["id"] for p in parameters if not isinstance(p["type"], str)]
        assert not non_str, f"Non-string types: {non_str}"

    def test_types_are_valid(self, parameters):
        import re
        def base_types(type_str):
            # Split compound types on ',' then strip array notation e.g. CHAR[2] → CHAR
            parts = [t.strip() for t in type_str.split(",")]
            return [re.sub(r"\[\d+\]$", "", p) for p in parts]

        invalid = []
        for p in parameters:
            for bt in base_types(p["type"]):
                if bt not in VALID_BASE_TYPES:
                    invalid.append((p["id"], p["type"], bt))
        assert not invalid, f"Unrecognized base types: {invalid}"

    def test_count_is_positive_integer(self, parameters):
        bad = [p["id"] for p in parameters
               if not isinstance(p["count"], int) or p["count"] < 1]
        assert not bad, f"Parameters with invalid count: {bad}"


# ── Min/max constraints ───────────────────────────────────────────────────────

class TestMinMax:
    @staticmethod
    def _parse_number(s):
        # Some values use comma-formatted numbers e.g. "60,000" → 60000
        return float(str(s).replace(",", ""))

    def test_min_max_parseable_as_float(self, parameters):
        bad = []
        for p in parameters:
            for key in ("min", "max"):
                if key in p and p[key] is not None:
                    try:
                        self._parse_number(p[key])
                    except (TypeError, ValueError):
                        bad.append((p["id"], key, p[key]))
        assert not bad, f"Non-numeric min/max values: {bad}"

    def test_min_less_than_max_where_present(self, parameters):
        violations = []
        for p in parameters:
            if "min" in p and "max" in p and p["min"] is not None and p["max"] is not None:
                try:
                    mn = self._parse_number(p["min"])
                    mx = self._parse_number(p["max"])
                    if mn >= mx:
                        violations.append((p["id"], p["name"], mn, mx))
                except (TypeError, ValueError):
                    violations.append((p["id"], p["name"], p["min"], p["max"]))
        assert not violations, f"min >= max: {violations}"

    def test_multiplier_parseable_as_float(self, parameters):
        bad = []
        for p in parameters:
            if "multiplier" in p and p["multiplier"] is not None:
                try:
                    float(p["multiplier"])
                except (TypeError, ValueError):
                    bad.append((p["id"], p["multiplier"]))
        assert not bad, f"Non-numeric multipliers: {bad}"


# ── Group constraints ─────────────────────────────────────────────────────────

class TestGroups:
    def test_groups_have_required_fields(self, groups):
        for g in groups:
            assert "name" in g, f"Group missing 'name': {g}"
            assert "startid" in g, f"Group missing 'startid': {g}"
            assert "endid" in g, f"Group missing 'endid': {g}"

    def test_group_startid_lte_endid(self, groups):
        violations = [
            (g["name"], g["startid"], g["endid"])
            for g in groups
            if g["startid"] > g["endid"]
        ]
        assert not violations, f"Groups with startid > endid: {violations}"

    def test_group_ids_cover_0_to_2047(self, groups):
        covered = set()
        for g in groups:
            for i in range(g["startid"], g["endid"] + 1):
                covered.add(i)
        assert 0 in covered
        assert 2047 in covered

    def test_every_parameter_id_falls_in_a_group(self, parameters, groups):
        def in_any_group(pid):
            return any(g["startid"] <= pid <= g["endid"] for g in groups)

        orphans = [p["id"] for p in parameters if not in_any_group(p["id"])]
        assert not orphans, f"Parameter IDs not covered by any group: {orphans}"


# ── Status entries ────────────────────────────────────────────────────────────

class TestStatus:
    def test_status_have_required_fields(self, status):
        for s in status:
            assert "type" in s, f"Status entry missing 'type': {s}"
            assert "description" in s, f"Status entry missing 'description': {s}"
            assert "datatype" in s, f"Status entry missing 'datatype': {s}"

    def test_status_descriptions_are_nonempty(self, status):
        empty = [s.get("type") for s in status if not s.get("description")]
        assert not empty, f"Status entries with empty description: {empty}"


# ── Spot-check well-known parameters ─────────────────────────────────────────

class TestKnownParameters:
    def _get(self, parameters, pid):
        return next((p for p in parameters if p["id"] == pid), None)

    def test_flap_control_switches_id_256(self, parameters):
        p = self._get(parameters, 256)
        assert p is not None
        assert p["name"] == "Flap Control Switches"
        assert p["type"] == "BYTE"

    def test_trim_switches_id_258(self, parameters):
        p = self._get(parameters, 258)
        assert p is not None
        assert p["name"] == "Trim Switches"
        assert p["type"] == "WORD"
