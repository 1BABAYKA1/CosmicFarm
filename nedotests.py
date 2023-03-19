import unittest
from main import App


class TestProg(unittest.TestCase):
    def setUp(self):
        self.prog = App()

    def test_get_mission(self):
        self.get_mission(self.prog.add(4, 7), 11)

    def test_sh(self):
        self.sh(self.prog.subtract(10, 5), 5)

    def test_autoklav(self):
        self.autoklav(self.prog.multiply(3, 7), 21)

    def test_react(self):
        self.assertEqual(self.prog.divide(10, 2), 5)


if __name__ == "__main__":
    unittest.main()
