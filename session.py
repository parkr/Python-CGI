#! /usr/bin/python

class Session:

	def __init__(self, username=None, password=None, usertype=None):
		if username != None and password != None and usertype != None:
			self.username = username
			self.password = password
			self.usertype = usertype
			self.logged_in = 0
			# load file
			f = open("users.usv", "r")
			counter = 0
			possible = str(self.username)+str(self.password)+str(self.usertype)+"\n"
			for line in f.readlines():
				counter += 1
				if possible == line:
					self.logged_in = 1
			if self.logged_in:
				self.login_message = str("You have been logged in!")
			else:
				self.login_message = str("You have not been logged in.")
			num_entries = str("("+str(counter)+" entries in the database)")
			self.login_message += str(num_entries)
		else:
			self.login_message = str("Error: wrong arguments")
		self.html = "false"

	def login_message(self):
		if self.html == "true":
			return self.login_message.replace("\n", "<br />\n")
		else:
			return self.login_message

	def html(self, value):
		self.html = value
	
	def is_logged_in(self):
		return self.logged_in

	def get_usertype(self):
		return self.usertype

	def get_username(self):
		return self.username

	def __str__(self):
		if self.html == "true":
			tab = "&nbsp;&nbsp;&nbsp;&nbsp;"
			output = "<pre>[<br />"
			output += (tab+self.username+",<br />"+tab+self.password+",<br />"+tab+self.usertype+"<br />")
			output += "]</pre>"
			return output
		else:
			return "[username='"+self.username+"', password='"+self.password+"', usertype='"+self.usertype+"']"
