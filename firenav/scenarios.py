"""FIRE-001: reproducible synthetic training scenario helpers."""
from .model import Mission

def load_starter_mission() -> Mission:
    return Mission()

def spread_fire_once(mission: Mission) -> None:
    """TODO FIRE-001: choose a deterministic expansion rule, bounds and exclusions.

    Suggested first step: expand exactly one safe cell eastward if inside grid.
    Add unit tests before trying stochastic spread.
    """
    mission.events.append("Fire change requested; fire expansion not implemented yet")
