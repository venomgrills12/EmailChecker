#!/bin/bash
read -p "Enter the Domain: " domain
echo "Checking if domain is valid"
ping -c 2 $domain
if [ $? -eq 0 ]
then
	echo "This is a valid Domain. Making further list"
	python3 email_generator.py
else
	echo "Sorry the server is dead"
fi
