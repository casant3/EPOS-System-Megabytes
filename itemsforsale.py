

### the following is a general class for items for sale

class ItemsForSale:
    def __init__(self, name, price):
        self.name = name
        self.price = price

### now create two sub classes Drink and Food

class Drink(ItemsForSale):
    # inherits name and price from ItemsForSale

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

### at the moment Food and Drink have the same properties (name and price)
### However separate sub classes allow for the addition of food-specific properties 
### for example sell-by date

class Food(ItemsForSale):
    # inherits name and price from ItemsForSale

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


### The following class can act as a container for the food and drink lists
### enables properties such as max number of items

class Menu:
    def __init__(self, name, max_items):
        self.name = name
        self.max_items = max_items
        self.drinks = []                        # create empty list
        self.food_items = []

    # method to add drink object to list

    def add_drink(self, drink):
        if len(self.drinks) < self.max_items:  # remember drinks is the list 
            self.drinks.append(drink)
            return True
        return False

    # method to add food object to list

    def add_food(self, food_item):
        if len(self.food_items) < self.max_items:  
            self.food_items.append(food_item)
            return True
        return False
