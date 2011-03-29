#! /usr/bin/python

class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print "Hello, my name is", self.name, r"."

p = Person("Parker")
p.sayHi()
