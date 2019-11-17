class Person:
	def __init__ (self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self):
		print(self.name + " is eating his favorite food = trash")
	def sport(self):
		print(self.name + " is playing his sport = sleeping")
person1 = Person("shoba doba", 72, "ashdod", "other")
person1.eat()
person1.sport()

class bird(object):
	def __init__ (self,name,color,speed):
		self.name = name
		self.color = color
		self.speed = speed
	def getspeed(self):
		return self.speed
	