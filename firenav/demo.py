"""A clearly labelled scripted UI demonstration, NOT an autonomous planner."""
from .model import Mission

def scripted_demo_path(mission: Mission) -> list[tuple[int, int]]:
    """Manually specified teaching animation only; it does not solve tickets."""
    points = [mission.base]
    points += [(x, 1) for x in range(2, 18)]
    points += [(17, y) for y in range(2, 13)]
    return points
