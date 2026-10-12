"""Small green starter tests; other tests are intentionally exercises."""
import unittest
from firenav.model import Mission
from firenav.planner import neighbors, manhattan, plan_path

class StarterTests(unittest.TestCase):
    def test_inside_and_blocked(self):
        m=Mission()
        self.assertTrue(m.inside((0,0)))
        self.assertFalse(m.inside((-1,0)))
        self.assertTrue(m.blocked((8,4)))
        self.assertFalse(m.blocked(m.base))

    def test_heuristic(self):
        self.assertEqual(manhattan((0,0),(3,4)),7)
        self.assertEqual(len(neighbors((0,0),20,15)),2)

    def test_student_planner_pending(self):
        # When FIRE-003 is finished, replace this with path validity assertions.
        self.assertEqual(plan_path((0,0),(3,0),5,5,set()),[])

if __name__=="__main__":
    unittest.main()
