import unittest
from models.base import Base
"""This class make the unittest of the class Base
"""


class TestBase(unittest.TestCase):
    """This is the unittest for the Base class
    """
    def setUp(self):
        """This methode permit to create an instance of object
        """
        self.b3 = Base(12)

    def test_id_b3(self):
        """This methods permit to test the sortie of function
        """
        self.assertEqual(self.b3.id, 12)


if __name__ == "__main__":
    """The entry point of the program
    """
    unittest.main()
