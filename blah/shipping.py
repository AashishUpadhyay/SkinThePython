class ShippingContainer:

    next_serial = 999

    def __init__(self, owner, contents):
        self.owner_code = owner
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1

    @classmethod
    def create_empty(cls):
        return cls('', [])

    @classmethod
    def create_with_owner(cls, owner):
        return cls('', owner, [])

    @classmethod
    def create_with_owner_and_contents(cls, owner, contents):
        return cls('', owner, contents)
