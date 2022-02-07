class Locations:
    """
        Represent a Locations object (The Cube)
    """
    def __init__(self, rows, columns, cells):
        self.positions = {}
        self.values = []
        self.rows = rows
        self.columns = columns
        self.cells = cells

        default_number = 1

        for cell in range(1, self.cells+1):
            for col in range(1, self.columns+1):
                for row in range(1, self.rows+1):
                    self.positions[(row, col, cell)] = default_number
                    default_number += 1

        self.values = list(self.positions.values())

    def add(self, value, position_x, position_y, position_z):
        """
        Add the new value at location (x, y, z)

        :param value:
        :param position_x:
        :param position_y:
        :param position_z:

        :return: None
        """
        try:
            index = self.positions[(position_x, position_y, position_z)]
            self.values[index-1] = value
        except KeyError:
            print(f"Position {position_x}, {position_y}, {position_z} doesn't exist in locations")
        except IndexError:
            print("index was calculated wrong")

    def get(self, position_x, position_y, position_z):
        """
        return the Value at position (x, y, z)

        :param position_x:
        :param position_y:
        :param position_z:

        :return: Value at position (x, y, z)
        """
        value = self.positions[(position_x, position_y, position_z)]

        return str(value)

    def view_locations(self):
        print("Z, Y, X")
        for z in range(1, self.cells+1):
            for y in range(1, self.columns+1):
                for x in range(1, self.rows+1):
                    print(f"{z}, {y}, {x} => {self.values[self.positions[(x,y,z)] - 1]}")

