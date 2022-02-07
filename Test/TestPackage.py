import unittest
from Models.Package import Package
from datetime import datetime, timedelta


class TestPackage(unittest.TestCase):

    def test_expire_time(self):
        package = Package("11111111", "20 X 20", "2022-02-06 10:00", "2022-02-01 10:00")
        self.assertEqual(package.time_to_expire().days, 5)

    def test_time_since_created(self):

        created_at = datetime.now() - timedelta(days=5)
        package = Package("11111111", "20 X 20",  datetime.now().strftime("%Y-%m-%d %H:%M"),
                          created_at.strftime("%Y-%m-%d %H:%M"))

        self.assertEqual(package.time_since_created().days, 5)


if __name__ == '__main__':
    unittest.main()