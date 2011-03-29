#! /usr/bin/python

class Session:

	def __init__(self, username=None, password=None):
		if username != None and password != None:
			self._username = username
			self._password = password
			self._admin = 0
			self._logged_in = 0
			# load file
			f = open("users.usv", "r")
			counter = 0
			possible_a = str(self._username)+str(self._password)+str("sysop\n")
			possible_u = str(self._username)+str(self._password)+str("user\n")
			for line in f.readlines():
				counter += 1
				if possible_a == line:
					self._logged_in = 1
					self._admin = 1
					self._usertype = str("sysop")
				elif possible_u == line:
					self._logged_in = 1
					self._usertype = str("user")
			if self._logged_in:
				self._login_message = str("You have been logged in!\n")
			else:
				self._login_message = str("You have not been logged in.\n")
			num_entries = str("("+str(counter)+" entries in the database)\n")
			self._login_message += str(num_entries)
		else:
			self._login_message = str("Error: wrong arguments\n")

	def login_message(self):
		if self._html == "true":
			output = self._login_message
			return output.replace("\n", "<br />\n")
		else:
			return self._login_message

	def html(self, value):
		self._html = value
	
	def is_logged_in(self):
		return self._logged_in

	def get_usertype(self):
		return self._usertype

	def get_username(self):
		return self._username

	def __str__(self):
		if self._html == "true":
			tab = "&nbsp;&nbsp;&nbsp;&nbsp;"
			output = "<pre>[<br />"
			output += (tab+self._username+",<br />"+tab+self._password+",<br />"+tab+self._usertype+"<br />")
			output += "]</pre>"
			return output
		else:
			return "[username='"+self._username+"', password='"+self._password+"', usertype='"+self._usertype+"']"
