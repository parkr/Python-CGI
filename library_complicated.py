#! usr/bin/python

users = {'parker': {'password':'password', 'type': 'reader'}, 'ruth': {'password':'password', 'type': 'librarian'}}
is_librarian = 0
books = {}

def login(user, pwd):
	global users
	global is_librarian
	if user in users:
		if pwd == users[user]['password']:
			print "You're logged in"
			if users[user]['type'] == 'librarian':
				print "You're logged in as a librarian"
				is_librarian = 1
			else:
				print "Welcome, reader!"
				is_librarian = 0
			return 1
		else:
			return 0
	else:
		print "User does not exist"
		return 0
	return 0

def add(user, password, usertype):
	global users
	if not users.has_key(user):
		users[user]['password'] = password
		users[user]['type'] = usertype
		return 1
	else:
		print "User already exists"
		return 0
	return 0

def delete(user):
	global users
	if users.has_key(user):
		del users[user]
		return 1
	else:
		print "User doesn't exist"
		return 0
	return 0

def add_book(title):
	global books
	if not books.has_key(title):
		books[title] = "in stock"
		return 1
	else:
		print "Book already in the inventory! Sorry!"
		return 0
	return 0

def del_book(title):
	global books
	if books.has_key(title) and books[title] != "borrowed":
		del books[title]
		return 1
	else:
		print "Book not in inventory or has been borrowed"
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
login(username, password)
choice = 'h'
while choice != 'q':
	print "What would you like to do? (enter 0 to quit)"
	print "a: add user"
	print "d: delete user"
	if is_librarian:
		print '''ab: add book
db: delete book
b: borrow book
r: return book'''
	else:
		print '''b: borrow book
r: return book'''
	choice = raw_input("So what'll it be? ")
	if choice == "a":
		add_user(raw_input("Username: "), raw_input("Password: "), raw_input("Type? (librarian or reader?)"))
	elif choice == "d":
		del_user(raw_input("Username: "))
	elif choice == "b":
		borrow(raw_input("Title: "))
	elif choice == "r":
		retur(raw_input("Title: "))
	elif is_librarian and choice == "ab":
		add_book(raw_input("Title: "))
	elif is_librarian and choice == "db":
		del_book(raw_input("Title: "))
	else:
		print "That's not an option"
	print "This menu has not been implemented yet"
	choice = 0
