#!/bin/bash
echo -e "\033[0;36m _______  _        ______   _______  _______ \033[1;31m _______  _______ 
         \033[0;36m __  __    __     __                         
         \033[0;36m|  \/  |_ _\ \   / /__ _ __   ___  _ __  ___  
         \033[0;36m| |\/| | '__\ \ / / _ \ '_ \ / _ \| '_ \/  _ \ 
         \033[0;36m| |  | | | _ \ V /  __/ | | | (_) | | | | |  |
         \033[0;36m|_|  |_|_|(_) \_/ \___|_| |_|\___/|_| |_| |_ | "
	echo -e "\n		     Author : Gaurav Chaudhary"
	echo -e "\n       	WARNING : Attacking Targets Without Prior \n"
	echo -e "      		  Consent Is Illegal And Punished By Law.  \n"

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
