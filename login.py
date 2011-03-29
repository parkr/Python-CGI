# /usr/bin/python

from session import Session
import cgi

form = cgi.FieldStorage()
username = str(form.getvalue("username"))
password = str(form.getvalue("password"))
usertype = str(form.getvalue("usertype"))

#print standard header
with open("header.html.pyt", "r") as header:
	print header.read() % ("Login")

u = Session(username, password, usertype)
print u.is_logged_in()

#print bottom of page
with open("bottom.html.pyt", "r") as bottom:
	print bottom.read()
