"""FIRE-002: mission state, battery budget and safe return workflow."""
from .model import Mission
from .planner import plan_path

def start_rescue_observation(mission: Mission) -> bool:
    """TODO FIRE-002: verify valid route, battery reserve and initial state."""
    mission.events.append("Start blocked: implement mission checks (FIRE-002)")
    return False

def request_return_to_base(mission: Mission) -> bool:
    """TODO FIRE-002: calculate safe return route and reject unsafe return."""
    mission.events.append("Return requested: implement safe-return logic")
    return False
