from datetime import datetime


class Package:
    """
    A class to represent a Package
    ...
    Attributes
        sku (str): Id for package instance
        size (str): size of package
        expired_at (datetime): date when package will expire
        created_at (datetime): date when package was created
        counter: number of instances that have been created from this class

    Methods
        time_to_expire(): Calculate the time to expire the package
        time_since_created(): Calculate the time since the package was expired
    """
    counter = 0

    def __init__(self, sku, size, expired_at, created_at):
        """
        Constructs all the necessary attributes for the package object.

        :param (str) sku: Package's ID
        :param (str) size: size of package
        :param (str) expired_at: date when package will expire
        :param (str) created_at: date when package was created
        """
        self.sku = sku
        self.size = size
        self.expired_at = datetime.strptime(expired_at, "%Y-%m-%d %H:%M")
        self.__created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M")

        Package.counter += 1

    def time_to_expire(self):
        """
        Calculate the time to expire the package

        :return: timedelta object which contains days, hours, minutes and seconds to package expires

        :rtype: datetime.timedelta
        """
        time_to_expire = self.expired_at - self.__created_at
        return time_to_expire

    def time_since_created(self):
        """
        Calculate the time since the package was expired


        :return: timedelta object which contains days, hours, minutes and seconds since the package was created

        :rtype: datetime.timedelta
        """
        time_since_created = datetime.now() - self.__created_at
        return time_since_created
