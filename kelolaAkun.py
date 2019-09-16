def kelolaAkun():
	nama 	= input("Nama	: ")
	email 	= input("Email	: ")
	ttl	= input("TTL	: ")
	
#Fungsi Input Gender
	gender_choice = False
	gender = input("Jenis Kelamin(L/P)	:")
	while (not gender_choice):
		if (gender != 'L' or gender != 'P'):
			print("masukkan L/P!")
			gender = input("Jenis Kelamin(L/P)	:")
		else :
			gender_choice = True;

	Bio	= input("Bio	: ")
