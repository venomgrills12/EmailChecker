import socket
import smtplib
import dns.resolver


def email_exists(email, mxRecord):
	host = socket.gethostname()

	# SMTP lib setup (use debug level for full output)
	server = smtplib.SMTP()
	server.set_debuglevel(0)

	# SMTP Conversation
	server.connect(mxRecord)
	server.helo(host)
	server.mail('gaurav12022003@gmail.com')
	code, message = server.rcpt(str(email))
	server.quit()

	# Assume 250 as Success
	if code == 250:
		return True
	else:
		return False

with open('wordlist.txt', 'r') as wordlist:
	emails = wordlist.read().splitlines()
	for email in emails:
		records = dns.resolver.query('emailhippo.com', 'MX')
		mxRecord = records[0].exchange
		mxRecord = str(mxRecord)
		if email_exists(email, mxRecord):
			print(f"{email} exists.")
		else:
			print(f"{email} DOESN'T work.")
