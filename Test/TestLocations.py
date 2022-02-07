import unittest
from Models.Locations import Locations


class TestLocations(unittest.TestCase):
    def test_create(self):

        locations = Locations(3, 4, 7)
        self.assertEqual(len(locations.values), 84)

    def test_add(self):

        locations = Locations(3, 4, 7)
        locations.add("New Value", 2, 2, 2)
        self.assertEqual(locations.values[17-1], "New Value")

    def test_get(self):

        locations = Locations(3, 4, 7)
        locations.get(2, 2, 2)
        self.assertEqual(locations.values[17-1], 17)


if __name__ == '__main__':
    unittest.main()
