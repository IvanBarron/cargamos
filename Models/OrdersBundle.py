import rstr
from .Order import Order
import csv


class OrdersBundle:
    def __init__(self):
        self.orders_bundle = []

    def add_new_order(self, sku, size, expired_at, created_at, address_line1, postal_code,
                      locality, city, state, country, address_line2, notes):
        """
        Add a new order to bundle

        :param sku:
        :param size:
        :param expired_at:
        :param created_at:
        :param address_line1:
        :param postal_code:
        :param locality:
        :param city:
        :param state:
        :param country:
        :param address_line2:
        :param notes:

        :return: None
        """
        # Here we can ignore, tag, rename, etc. the repeated sku.
        # In this case we will create a new one.
        if self.in_bundle(sku):
            sku = self.new_sku()

        self.orders_bundle.append(Order(
            sku=sku, size=size,
            expired_at=expired_at,
            created_at=created_at,
            address_line1=address_line1,
            postal_code=postal_code,
            locality=locality,
            city=city, state=state,
            country=country,
            address_line2=address_line2,
            notes=notes
        ))

    def more_time_for_delivery(self):
        """
        Get the object with more difference between Created_at and expired_at

        :return: Order object with more diference bettwe
        """
        order_list = sorted(self.orders_bundle,
                            key=lambda order: order.time_to_expire().days, reverse=True)

        return order_list[0]

    def read_orders_from_csv(self, file_path):
        """
        Read a file csv and load orders into a instances

        :param file_path:
        :return: None
        """
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.add_new_order(**row)
                line_count += 1

    def in_bundle(self, sku):
        """
        Verify if a sku already exist in bundle.

        :param sku:
        :return: It returns True If SKU is in bundle and False if it isn't
        """
        filter_list = list(filter(lambda order: order.sku == sku, self.orders_bundle))
        if filter_list:
            return True
        else:
            return False

    def new_sku(self):
        """
        Defines a new sku for an order not in this bundle

        :return: A unique SKU
        """
        sku = rstr.xeger(r'[0-9]{8}')
        while self.in_bundle(sku):
            sku = rstr.xeger(r'[0-9]{8}')

        return sku
