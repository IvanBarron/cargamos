from .Package import Package
from .Address import Address
from datetime import datetime, timedelta
from MyExceptions.MyExceptions import ExpiredError


class Order(Package):
    """
    A class to represent an Order

    Attributes
        size (str):
        expired_at (str):
        created_at (str):
        address (Address):

    Methods
        deliver_oder(): Mark as delivered the package if this has not been expired
    """

    def __init__(self, sku, size, expired_at, created_at, address_line1, postal_code, locality,
                 city, state, country, address_line2="", notes=""):
        """
        Constructs all the necessary attributes for the Order object.

        :rtype: object
        :param (str) sku:
        :param (str) size:
        :param (str) expired_at:
        :param (str) created_at:
        :param (str) address_line1:
        :param (str) postal_code:
        :param (str) locality:
        :param (str) city:
        :param (str) state:
        :param (str) country:
        :param (str) address_line2:
        :param (str) notes: (optional)

        """
        super().__init__(sku, size, expired_at, created_at)
        self.delivery_address = Address(address_line1, postal_code, locality,
                                        city, state, country, address_line2, notes)
        self.delivery_at = None
        self.is_delivered = False

    def deliver_order(self):
        """
        Mark as delivered the package if this has not been expired

        :return: None

        :exception (Exception): The package has been expired
        """
        if self.expired_at > datetime.now():
            self.is_delivered = True
            self.delivery_at = datetime.now()
        else:
            raise ExpiredError(self.sku)

    def test_deliver_order(self, days):
        """


        :return: None

        :exception (Exception): The package has been expired
        """
        if self.expired_at < datetime.now():
            self.is_delivered = True
            self.delivery_at = self.created_at + timedelta(days=days)

        else:
            raise ExpiredError(self.sku)