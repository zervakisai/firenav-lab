"""FIRE-003: replace the intentionally incomplete planning function."""
from collections.abc import Iterable

Point = tuple[int, int]

def neighbors(point: Point, width: int, height: int) -> list[Point]:
    """Four-directional neighbors within map boundaries (starter example)."""
    x, y = point
    candidates = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [p for p in candidates if 0 <= p[0] < width and 0 <= p[1] < height]

def manhattan(a: Point, b: Point) -> int:
    """Manhattan-distance heuristic for 4-neighbor A*."""
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def plan_path(start: Point, goal: Point, width: int, height: int,
              blocked: Iterable[Point]) -> list[Point]:
    """TODO FIRE-003: A* shortest grid path, including start and goal.

    Return [] when unreachable or invalid. Do not cross blocked cells.
    HINT: frontier priority queue, g_score dictionary, came_from mapping.
    """
    return []  # Student work: replace after reading issue FIRE-003.
