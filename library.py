#! usr/bin/python

users = {'parker': 'password', 'ruth': 'password'}
user_permissions = {'parker': 'reader', 'ruth': 'librarian'}
is_librarian = 0
books = {}

def login(user, pwd):
	global users
	global user_permissions
	if user in users:
		if pwd == users[user]:
			print "You're logged in"
			if user_permissions[user] == "librarian":
				print "You're logged in as a librarian"
				is_librarian = 1
			return 1
		else:
			return 0
	else:
		print "User does not exist"
		return 0
	return 0

def add(user, password, usertype):
	global users
	global user_permissions
	if not users.has_key(user):
		users[user] = password
		user_permissions[user] = usertype
		return 1
	else:
		print "User already exists"
		return 0
	return 0

def delete(user):
	global users
	global user_permissions
	if users.has_key(user):
		del users[user]
		del user_permissions[user]
		return 1
	else:
		print "User doesn't exist"
		return 0
	return 0

def add_book(title, status):
	global books
	if not books.has_key(title):
		books[title] = status
		return 1
	else:
		print "Book already in the inventory! Sorry!"
		return 0
	return 0

def del_book(title, status):
	global books
	if books.has_key(title):
		del books[title]
		return 1
	else:
		print "Book not in inventory"
		return 0
	return 0

def borrow(title):
	global books
	if books.has_key(title) and books[title] != "borrowed":
		books[title] = "borrowed"
		print "%s has been borrowed. You have 2 weeks to enjoy it before it's due."
		return 1
	else:
		print "Looks like either the book doesn't exist or it's currently borrowed."
		return 0
	return 0

def retur(title):
	global books
	if books.has_key(title) and books[title] == "borrowed":
		books[title] = "in stock"
		print "You've successfully returned your book"
		return 1
	else:
		print "Looks like either the book is in stock already or the book isn't in the database"
		return 0
	return 0


username = str(raw_input("Enter your username: "))
password = str(raw_input("Enter your password: "))
choice = 1
while choice:
	print "What would you like to do? (enter 0 to quit)"
	print "1: add user"
	print "2: delete user"
	if is_librarian:
		print '''3: add book
4: delete book
5: borrow book
6: return book'''
	else:
		print '''3: borrow book
4: return book'''
	choice = int(raw_input("So what'll it be? "))
	print "This menu has not been implemented yet"
	choice = 0
