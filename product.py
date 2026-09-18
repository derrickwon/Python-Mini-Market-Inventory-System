class Product:
    # class constructor
    def __init__(self, name, category, quantity, unit_price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price

    # getters
    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_quantity(self):
        return self.quantity

    def get_total_value(self):
        return self.calculate_value()

    #function to calculate total with quantity × unit price
    def calculate_value(self):
        return self.quantity * self.unit_price

    #functions to display items in format
    def display(self):
        print(f"{self.name}\t{self.category}\t\t{self.quantity}\t\t\tRM{self.unit_price}\t\tRM{self.calculate_value():.2f}")