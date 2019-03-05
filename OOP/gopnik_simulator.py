import random

class City:
	def __init__(self):
		self.gopniks = []
		self.victims = []
		self.cops = []

		for i in range(20):
			g = Gopnik(figher_skill=random.gauss(50, 25), 
						fear_factor=random.gauss(50, 25),
						speed=random.gauss(50, 25))
			self.gopniks.append(g)

		for i in range(60):		
			g = Victim(figher_skill=random.gauss(35, 25), 
						fear_factor=random.gauss(25, 25),
						speed=random.gauss(50, 25),
						price_of_phone=max(0, random.gauss(100000, 50000)))
			self.victims.append(g)

		for i in range(3):
			g = Cop(figher_skill=random.gauss(50, 25), 
					speed=random.gauss(50, 25))
			self.cops.append(g)

	def nextDay(self):
		print("\n\n\n\nNextDay")
		# Gop-stop
		for i in range(random.randrange(5, 10)):
			gopnik = self.gopniks[random.randrange(0, len(self.gopniks))]
			victim = self.victims[random.randrange(0, len(self.victims))]
			gopnik.rams(victim)

		# Cop-stop
		for i in range(random.randrange(1, 4)):
			gopnik = self.gopniks[random.randrange(0, len(self.gopniks))]
			cop = self.cops[random.randrange(0, len(self.cops))]
			cop.rams(gopnik)

		print("!!!!", len(self.gopniks), "gopniks left")
		for i, gopnik in enumerate(self.gopniks):
			print(gopnik.money, end=',  ')
			if gopnik.money > 10000:
				gopnik.money -= 10000
				gopnik.hunger = max(0, gopnik.hunger-10)
			else:
				gopnik.hunger += 20
				if gopnik.hunger >= 100:
					print("Good Night, Sweet Prince ", gopnik.figher_skill, "(((")
					del self.gopniks[i]



class Gopnik:
	def __init__(self, figher_skill, fear_factor, speed):
		self.speed = speed
		self.figher_skill = figher_skill
		self.fear_factor = fear_factor
		self.money = 0
		self.phones = []
		self.hunger = 0 # 100
		self.is_in_jail = False

	def rams(self, victim):
		if self.fear_factor > victim.fear_factor + 33:
			print("Gopnik casts fear on victim, he gives the phone")
			self.money += victim.price_of_phone
			victim.price_of_phone = max(0, random.gauss(100000, 50000)) 
		elif random.randrange(0, 2):
			#Run
			if self.speed > victim.speed:
				print("Victim runs away, but gopnik catches it))))))))")
				self.money += victim.price_of_phone
				victim.price_of_phone = max(0, random.gauss(100000, 50000))
			else:
				print("Victim ran away")
		else:
			#Fight
			if self.figher_skill > victim.figher_skill:
				print("They fight, gopnik wins")
				self.money += victim.price_of_phone
				victim.price_of_phone = max(0, random.gauss(100000, 50000))
			else:
				print("Victim beats gopnik((((")
				if victim.fear_factor > self.fear_factor:
					print("Victim takes all of the gopnik's money((((((")
					self.money = 0

class Victim:
	def __init__(self, figher_skill, fear_factor, speed, price_of_phone):
		self.speed = speed
		self.figher_skill = figher_skill
		self.fear_factor = fear_factor
		self.money = 0
		self.price_of_phone = price_of_phone


class Cop:
	def __init__(self, figher_skill, speed):
		self.speed = speed
		self.figher_skill = figher_skill
		self.money = 0
		self.heads = 0

	def rams(self, gopnik):
		if random.randrange(0, 2):
			#Run
			if self.speed > gopnik.speed:
				print("Gopnik is caught")
				gopnik.money = 0
				gopnik.hunger += 25
				self.heads += 1
				if self.heads % 3 == 0:
					if random.randrange(0, 2):
						self.figher_skill += 10
					else:
						self.speed += 10
			else:
				print("Gopnik ran away")
		else:
			if self.figher_skill < gopnik.figher_skill:
				print("Cop and gopnik fight, gopnik wins")
				gopnik.money += 100000
			else:
				print("Cop beats gopnik((((")
				gopnik.money = 0
				gopnik.hunger += 40
				self.heads += 1
				if self.heads % 3 == 0:
					if random.randrange(0, 2):
						self.figher_skill += 10
					else:
						self.speed += 10


almaty = City()
for i in range(10000):
	almaty.nextDay()
	print("Day Number", i)
	if len(almaty.gopniks) == 0:
		print("No more gopniks")
		break
