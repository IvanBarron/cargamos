import unittest
from Models.Order import Order
from datetime import datetime, timedelta
from MyExceptions.MyExceptions import ExpiredError


class TestOrder(unittest.TestCase):
    def Test_deliver_order(self):

        created_at = datetime.now() - timedelta(days=5)
        expired_at = created_at + timedelta(days=4)

        order = Order("54947713", "34 X 2", expired_at.strftime("%Y-%m-%d %H:%M"), created_at("%Y-%m-%d %H:%M"),
                      "xnqgbpp #52", "19272", "Skell", "Kharkiv", "Mamoudzou", "Gabon", "LPBnHYK", "iVBRquA169oy")

        self.assertRaises(ExpiredError, order.deliver_order())


if __name__ == '__main__':
    unittest.main()