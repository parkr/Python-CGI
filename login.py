#! /usr/bin/python

import cgi

class Session:

	def __init__(self, username, password, usertype):
		self.username = username
		self.password = password
		self.usertype = usertype
		self.logged_in = 0
		# load file
		with open("users.usv", "r") as f:
			counter = 0
			possible = str(self.username)+str(self.password)+str(self.usertype)+"\n"
			print possible
			for line in f:
				counter += 1
				print line
				if possible == line:
					print "You should be logged in"
					self.logged_in = 1
			print 'file read (', counter, "lines )"


	def is_logged_in(self):
		return self.logged_in

	def get_usertype(self):
		return self.usertype

	def get_username(self):
		return self.username

	def __str__(self):
		return "[username='"+self.username+"', password='"+self.password+"', usertype='"+self.usertype+"']"
