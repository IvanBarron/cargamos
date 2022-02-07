class Address:
    """
    A class to represent an Address

    Attributes
        address_line1 (str):
        postal_code (str):
        locality (str):
        city (str):
        state (str):
        country (str):
        address_line2 (str):
        notes (str):

    Methods
        get_full_address(): Calculate the time to expire the package
    """
    def __init__(self, address_line1, postal_code, locality,
                 city, state, country, address_line2, notes):
        """
        A class to represent a Address

        :param (str) address_line1:
        :param (str) postal_code:
        :param (str) locality:
        :param (str) city:
        :param (str) state:
        :param (str) country:
        :param (str) address_line2:
        :param (str) notes:
        """
        self.address_line1 = address_line1
        self.postal_code = postal_code
        self.locality = locality
        self.city = city
        self.state = state
        self.country = country
        self.address_line2 = address_line2
        self.notes = notes

    def __str__(self):
        """
        concatenate all address

        :return: full address as string

        :rtype: str
        """
        return self.address_line1 + ", " + self.locality + ' ' + self.city + ' ' + self.state \
            + ', ' + self.city + ', Code.' + self.postal_code + '\n' + self.notes

    def get_full_address(self):
        """
        Get full address and notes as string

        :return: full address as string

        :rtype: str
        """
        return self.address_line1 + ", " + self.locality + ' ' + self.city + ' ' + self.state \
            + ', ' + self.city + ', Code.' + self.postal_code + '\n' + self.notes
