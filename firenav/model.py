"""Small, dependency-free mission model. Coordinates are (x, y) grid cells."""
from dataclasses import dataclass, field

WIDTH, HEIGHT = 20, 15
BASE = (1, 1)
TARGET = (17, 12)
OBSTACLES = {(8, y) for y in range(3, 12)} | {(x, 7) for x in range(10, 15)}

@dataclass
class Mission:
    width: int = WIDTH
    height: int = HEIGHT
    base: tuple[int, int] = BASE
    target: tuple[int, int] = TARGET
    position: tuple[int, int] = BASE
    battery: int = 100
    obstacles: set[tuple[int, int]] = field(default_factory=lambda: set(OBSTACLES))
    fire: set[tuple[int, int]] = field(default_factory=lambda: {(11, 4), (12, 4), (11, 5), (12, 5)})
    route: list[tuple[int, int]] = field(default_factory=list)
    state: str = "READY"
    events: list[str] = field(default_factory=list)

    def inside(self, p: tuple[int, int]) -> bool:
        return 0 <= p[0] < self.width and 0 <= p[1] < self.height

    def blocked(self, p: tuple[int, int]) -> bool:
        return not self.inside(p) or p in self.obstacles or p in self.fire

    def move_one_step(self, next_position: tuple[int, int]) -> bool:
        """Safe grid movement; physics of real aircraft is outside the workshop."""
        x, y = self.position
        nx, ny = next_position
        if self.state not in ("FLYING", "RETURNING"):
            return False
        if self.battery <= 0 or abs(x - nx) + abs(y - ny) != 1 or self.blocked(next_position):
            self.state = "ABORTED"
            self.events.append("Safety stop: unsafe step or empty battery")
            return False
        self.position = next_position
        self.battery -= 1
        if self.position == self.target and self.state == "FLYING":
            self.state = "TARGET_REACHED"
            self.events.append("Reached rescue observation waypoint (not physical rescue)")
        elif self.position == self.base and self.state == "RETURNING":
            self.state = "COMPLETED"
            self.events.append("Returned safely to base")
        return True
