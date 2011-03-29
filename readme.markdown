# My McGill Python Files #

### the extension *.usv* stands for "un-separated values". It is used by the *Session* module in *login.py* ###

#### Usage: ####
	import login
	session = login.Session(username, password, usertype)
	session.is_logged_in() #returns 0 if not logged in and 1 if the user was successfully logged in.
