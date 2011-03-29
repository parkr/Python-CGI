# My McGill Python Files #

### the extension *.usv* stands for "un-separated values". It is used by the *Session* module in *session.py* ###

#### Usage: ####
	import session
	s = session.Session(username, password)
	s.is_logged_in() #returns 0 if not logged in and 1 if the user was successfully logged in.

or
	from session import Session
	s = Session(username, password)
	s.is_logged_in()
