class Apparel:
    counter = 100

    def __init__(self, price, item_type):
        Apparel.counter += 1
        self.item_id = f"{item_type[0].upper()}{Apparel.counter}"
        self.price = price
        self.item_type = item_type

    def calculate_price(self):
        self.price += self.price * 0.05

    def get_item_id(self):
        return self.item_id

    def get_price(self):
        return self.price

    def get_item_type(self):
        return self.item_type

    def set_price(self, price):
        self.price = price


class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "Cotton")
        self.discount = discount

    def calculate_price(self):
        super().calculate_price()
        self.price -= self.price * (self.discount / 100)
        self.price += self.price * 0.05

    def get_discount(self):
        return self.discount


class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.points = 0

    def calculate_price(self):
        super().calculate_price()
        if self.price > 10000:
            self.points = 10
        else:
            self.points = 3
        self.price += self.price * 0.10

    def get_points(self):
        return self.points


cotton_item = Cotton(1000, 10)
cotton_item.calculate_price()
print(f"Cotton Item ID: {cotton_item.get_item_id()}, "
      f"Price: {cotton_item.get_price()}, "
      f"Discount: {cotton_item.get_discount()}")

silk_item = Silk(12000)
silk_item.calculate_price()
print(f"Silk Item ID: {silk_item.get_item_id()}, "
      f"Price: {silk_item.get_price()}, "
      f"Points: {silk_item.get_points()}")
