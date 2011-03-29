#!/usr/bin/env python

def read_in_file(filename):
	f = open(filename, "r")
	return f.read()

try:
	import traceback, sys, os, cgi
	from session import Session
	# The following makes errors go to HTTP client's browser
	# instead of the server logs.
	sys.stderr = sys.stdout

	print 'Content-type: text/html\n'
	form = cgi.FieldStorage()
	username = str(form.getvalue("username"))
	password = str(form.getvalue("password"))
	usertype = str(form.getvalue("usertype"))

	#print standard header
	print read_in_file("header.html.pyt") % ("Login")

	u = Session(username, password, usertype)
	u.html("true")
	print u.login_message()
	print u

	#print bottom of page
	print read_in_file('bottom.html.pyt')
        
except Exception, e:
	import traceback
        print 'Content-type: text/html\n'
        print
        print '<html><head><title>'
        print str(e)
        print '</title>'
        print '</head><body>'
        print '<h1>TRACEBACK</h1>'
        print '<pre>'
        traceback.print_exc()
	traceback.prunt_stack()
        print '</pre>'
        print '</body></html>'
