import random

FILENAME = "wordlist.txt"

def wordlist_generator():
	existing_emails = set()
	with open(FILENAME, 'w') as wordlist:
		fname = input("Enter first name: ")
		lname = input("Enter last name: ")
		domain = input("Enter domain: ")

		email: list = []

		for _ in range(1000):
			email = []
			infront = random.randint(0,15)
			inback = random.randint(0,3)
			capitalize = random.randint(0,15)
			email.append(fname)
			if infront == 0:
				# This would reduce the possibilty of generating an email id with number after first name, which happens, but is rare.
				email.append(str(random.randint(0,9999)))
			email.append(lname)
			if inback:
				email.append(str(random.randint(0,9999)))
			email.append(f"@{domain}")
			str_email = ''.join(email)
			if str_email not in existing_emails:
				wordlist.write(str_email + '\n')
				existing_emails.add(str_email)

			if capitalize == 0:
				# Again, to reduce the probability of a captialised email, which are rare, although not zero.
				email = []
				email.append(fname.capitalize())
				if infront == 0:
					email.append(str(random.randint(0,9999)))
				email.append(lname.capitalize())
				if inback:
					email.append(str(random.randint(0,9999)))

				email.append(f"@{domain}")
				str_email = ''.join(email)
				if str_email not in existing_emails:
					wordlist.write(str_email + '\n')
					existing_emails.add(str_email)


if __name__ == '__main__':
	wordlist_generator()
