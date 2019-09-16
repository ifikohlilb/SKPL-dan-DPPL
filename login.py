def login():
	db_akun = [['uname','pass'],]
	
	uname 	= input("Username	:")
	pswd	= input("Password	:")
	
	while(uname not in db_akun and pswd not in db_akun) :
		uname 	= input("Username	:")
		pswd	= input("Password	:")
	if (uname in db_akun and pswd in db_akun):
		print("login successful")
