import unittest
from Models.OrdersBundle import OrdersBundle


class TestOrdersBundle(unittest.TestCase):
    def test_read_orders_from_csv(self):

        test_bundle = OrdersBundle()
        test_bundle.read_orders_from_csv("/Users/IBH/Desktop/cargamos/test.csv")

        self.assertEqual(len(test_bundle.orders_bundle), 10)

    def test_more_time_for_delivery(self):

        test_bundle = OrdersBundle()
        test_bundle.read_orders_from_csv("/Users/IBH/Desktop/cargamos/test.csv")

        self.assertEqual(test_bundle.more_time_for_delivery().sku, "08614048")


if __name__ == '__main__':
    unittest.main()