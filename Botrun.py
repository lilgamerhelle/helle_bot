import string
from Read import getUser, getMessage
from Bot_Socket import openSocket, sendMessage
from Bot_Initialize import joinRoom
from Bot_Settings import CHANNEL
import sqlite3
import os
import os.path
import shutil
import sys



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
				PATH = "C:\Users\BriansDesktop\Documents\Bot in channel\ " + user + "_Settings.py" 
				if os.path.isfile(PATH) is False:
					print(user + "_Settings.py")
					sendMessage(s, "Joining " + user + "'s channel")
					conn = sqlite3.connect(user +".accdb")
					src="C:\Users\BriansDesktop\Documents\Bot in channel\Settings.py "
					dst="C:\Users\BriansDesktop\Documents\Bot in channel\Renamed_settings\Settings.py"
					shutil.copy(src, dst)
					with open("C:\Users\BriansDesktop\Documents\Bot in channel\Renamed_settings\Settings.py","a") as f:
						f.write("CHANNEL = " + '"' + user + '"' + "")
						f.closed
					os.rename("C:\Users\BriansDesktop\Documents\Bot in channel\Renamed_settings\Settings.py", "C:\Users\BriansDesktop\Documents\Bot in channel\ " + user + "_Settings.py")
				else:
					sendMessage(s, "Im already working for you")
					break
			if "!endbot" in message:
				sys.exit()
				break
				
				