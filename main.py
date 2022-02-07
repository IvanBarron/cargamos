import csv
from Models.OrdersBundle import OrdersBundle
from Models.Locations import Locations


if __name__ == "__main__":
    """
    Test main flow
    """
    ROWS = 3
    COLUMNS = 4
    DEEP = 7

    bundle = OrdersBundle()
    bundle.read_orders_from_csv("/Users/IBH/Desktop/cargamos/orders.csv")
    print(f"{len(bundle.orders_bundle)} orders have been loaded")

    cube = Locations(ROWS, COLUMNS, DEEP)
    cube.add("Hola", 3, 4, 7)
    cube.view_locations()