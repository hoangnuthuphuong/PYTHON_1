class Payment:
    amount: float
    def __init__(self, amount):
        self.amount = amount


class Cash(Payment):
    cashTendered: float
    def __init__(self, amount, cashTendered):
        super().__init__(amount)
        self.cashTendered = cashTendered

class Check(Payment):
    name: str
    bankID: str
    def __init__(self, amount, name, bankID):
        super().__init__(amount)
        self.name = name
        self.bankID = bankID
    def authorized(self) -> str:
        pass


class Credit(Payment):
    number: str
    type: str
    def __init__(self, amount, number, type, expDate):
        super().__init__(amount)
        self.number = number
        self.type = type
        self.expDate = expDate
    def authorized(self) -> None:
        pass


class Item:
    description: str
    def __init__(self, shippingWeight, description):
        self.shippingWeight = shippingWeight
        self.description = description
    def getPriceForQuantity(self) -> None:
        pass
    def getTax(self) -> None:
        pass
    def inStock(self) -> None:
        pass


class OrderDetail:
    item: Item
    description: str
    taxStatus: str
    def __init__(self, shipping, description, quantity, taxStatus):
        self.quantity = quantity
        self.taxStatus = taxStatus
    def calcSubTotal(self):
        pass
    def calcWeight(self):
        pass
    def calcTax(self):
        pass


class Order:
    payments: [Cash,Check,Credit]
    detail: OrderDetail
    status: str

    def __init__(self, date, status):
        self.date = date
        self.status = status
    def calcSubTotal(self):
        pass
    def calcTax(self):
        pass
    def calcTotal(self):
        pass
    def calcTotalWeight(self):
        pass


class Customer:
    order: list[Order]
    def __init__(self, name: str, address):
        self.name = name
        self.address = address
