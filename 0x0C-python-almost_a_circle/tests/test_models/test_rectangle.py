import unittest
from models.Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.b3 = Base()

    def test_id_b3(self):
        self.assertEqual(self.b3.id, 1)


if __name__ == "__main__":
    unittest.main()
