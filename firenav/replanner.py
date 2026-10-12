"""FIRE-004: dynamic mission replanning. Intentionally a student task."""
from .model import Mission
from .planner import plan_path

def replan_when_needed(mission: Mission) -> bool:
    """TODO FIRE-004: review fire, blocked route, battery budget and alternatives.

    Only update mission.route after a safe candidate route has been verified.
    Return True if route was changed; False otherwise.
    Never represent this prototype as a flight safety certified controller.
    """
    return False
