import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import CHANNEL
import sqlite3
import os
import copy
import shutil


s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
			if "You Suck" in message:
				sendMessage(s, "No, you suck!")
				break
			if "!commands" in message:
				sendMessage(s, "My built in commands can be found at https://github.com/lilgamerhelle/helle_bot/blob/master/Commands")
				break
			if CHANNEL == "helle_bot" and "!join" in message:
				sendMessage(s, "Joining " + user + "'s channel")
				conn = sqlite3.connect(user +".accdb")
				shutil.copy('Settings.py', "*.*")
				os.rename('Settings.py', user + ' Settings.py') 
				with open(user + ' Settings.py','a') as f:
					f.write('CHANNEL = ' + '"' + user + '"')
				
				