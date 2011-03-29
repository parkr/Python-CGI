#! /usr/bin/python

import cgi

def main():
	print "Content-type: text/plain\n"
	form = cgi.FieldStorage()
	weight = int(form.getvalue("weight"))
	print "A person of a normal activity level requires ",
	print weight*.4,
	print "g of protein per day."
	print "If you are more active, try to eat ",
	print weight*.6,
	print "g of protein per day."
	
main()
