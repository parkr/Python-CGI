#!/usr/bin/env python
try:
        import traceback, sys, os, cgi
        # The following makes errors go to HTTP client's browser
        # instead of the server logs.
        sys.stderr = sys.stdout
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

        
except Exception, e:
        print 'Content-type: text/html\n'
        print
        print '&lt;html&gt;&lt;head&gt;&lt;title&gt;'
        print str(e)
        print '&lt;/title&gt;'
        print '&lt;/head&gt;&lt;body&gt;'
        print '&lt;h1&gt;TRACEBACK&lt;/h1&gt;'
        print '&lt;pre&gt;'
        traceback.print_exc()
        print '&lt;/pre&gt;'
        print '&lt;/body&gt;&lt;/html&gt;'
print "Content-Type: text/html\n\n"