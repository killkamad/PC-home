import copy

class Beverage:
	def __init__(self, name, price, ingredients=[]):
		self.name = name
		self.price = price
		self.ingredients = ingredients
		
	def __str__(self):
		return self.name + " - " + str(self.price) 
		
	def __repr__(self):
		return self.name + " - " + str(self.price) 


class Coffee(Beverage):
	def add_syrup(self, syrup):
		if not isinstance(syrup, Syrup):
			raise Exception("Only syrups are allowed in coffee")
		self.ingredients.append(syrup)
		self.price += syrup.price


class EspressoCoffee(Coffee):
	def calc_price(self):
		return self.price


class AlternativeCoffee(Coffee):
	def calc_price(self):
		return self.price * 1.1


class Tea(Beverage):
	def calc_price(self):
		return self.price + 100
		
	def add_spice(self, spice):
		if not isinstance(spice, Spice):
			raise Exception("Only spices are allowed in tea")
		self.ingredients.append(spice)
		self.price += spice.price


class Ingredient:
	def __init__(self, name, price):
		self.name = name
		self.price = price
		
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name
		

class Spice(Ingredient):
	pass
	

class Syrup(Ingredient):
	pass


class CoffeeShop:
	def __init__(self):
		self.menu = []
		self.ingredients = []
		self.orders = []
		
	def add_menu(self, item):
		if not isinstance(item, Beverage):
			raise Exception("Not beverage")
		self.menu.append(item)	
		
	def add_ingredient(self, item):
		if not isinstance(item, Ingredient):
			raise Exception("Not ingredient")
		self.ingredients.append(item)
		
	def display_menu(self):
		print("Our items")
		for i, item in enumerate(self.menu):
			print(i, "-", item)
			
		print("Our additional ingredients")
		for i, item in enumerate(self.ingredients):
			print(i, "-", item)
			
	
	def order(self, index_menu, index_ingredient=None):
		item = copy.deepcopy(self.menu[index_menu])
		if index_ingredient is not None:
			if isinstance(item, Coffee):
				item.add_syrup(self.ingredients[index_ingredient])
			if isinstance(item, Tea):
				item.add_spice(self.ingredients[index_ingredient])		
		self.orders.append(item)
		
	def report(self):
		total = 0
		beverages_counters = {}
		for order in self.orders:
			total += order.calc_price()
			if order.name+str(order.ingredients) in beverages_counters:
				beverages_counters[order.name+str(order.ingredients)] += 1
			else:
				beverages_counters[order.name+str(order.ingredients)] = 1
		print("Total order", len(self.orders))
		print("Total money", total)
		print("Average order", total/len(self.orders))
		beverages_counters = \
				[(k, beverages_counters[k]) for k in sorted(beverages_counters, key=beverages_counters.get, reverse=True)]
		for order, counter in beverages_counters:
			print(order, counter)
			
CityChoto = CoffeeShop()

CityChoto.add_ingredient(Syrup("Coconut", 300))
CityChoto.add_ingredient(Syrup("Vanilla", 200))
CityChoto.add_ingredient(Spice("Ginger", 100))
		
CityChoto.add_menu(EspressoCoffee("Cappuccino", 750))
CityChoto.add_menu(EspressoCoffee("Coconut Latte", 1000, [CityChoto.ingredients[0]]))
CityChoto.add_menu(EspressoCoffee("Latte", 500))
CityChoto.add_menu(Tea("Black Default", 900))
CityChoto.add_menu(AlternativeCoffee("Turkic Coffee", 750))

CityChoto.display_menu()

CityChoto.order(2, 0)
CityChoto.order(2)
CityChoto.order(2, 1)
CityChoto.order(0)
CityChoto.order(0)
CityChoto.order(2, 1)
CityChoto.order(2, 1)
CityChoto.order(2, 1)
CityChoto.order(1)
CityChoto.order(4)
CityChoto.order(3)
CityChoto.order(4)

CityChoto.report()
