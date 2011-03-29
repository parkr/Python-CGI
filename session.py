#! /usr/bin/python

import cgi

class Session:

	def __init__(self, username=None, password=None, usertype=None):
		if username != None and password != None and usertype != None:
			self.username = username
			self.password = password
			self.usertype = usertype
		else:
			form = cgi.FieldStorage()
			self.username = str(form.getvalue("username"))
			self.password = str(form.getvalue("password"))
			self.usertype = str(form.getvalue("usertype"))
		self.logged_in = 0
		# load file
		with open("users.usv", "r") as f:
			counter = 0
			possible = str(self.username)+str(self.password)+str(self.usertype)+"\n"
			for line in f:
				counter += 1
				if possible == line:
					self.logged_in = 1
			print '(', counter, "entries )"
			if self.logged_in:
				print "You have been logged in!"
			else:
				print "You have not been logged in."


	def is_logged_in(self):
		return self.logged_in

	def get_usertype(self):
		return self.usertype

	def get_username(self):
		return self.username

	def __str__(self):
		return "[username='"+self.username+"', password='"+self.password+"', usertype='"+self.usertype+"']"
