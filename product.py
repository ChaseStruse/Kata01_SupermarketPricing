import deal

class Product:
  name = "Product"
  price = 1.11
  quantity = 0
  deal = deal.Deal
  onSale = False

  def __init__(self):
    self.name = "Product"
    self.price = 0
    self.quantity = 0
    self.onSale = False

  def __init__(self, _name, _price, _quantity, _onSale):
    self.name = _name
    self.price = _price
    self.quantity = _quantity
    self.onSale = _onSale