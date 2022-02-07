class ExpiredError(Exception):
    """
    Exception raised for errors when the package has been expired
    """
    def __init__(self, package_sku, message="Package has been expired"):
        self.package_sku = package_sku
        super().__init__(self.message)

    def __str__(self):
        return f'{self.package_sku} has been expired'
