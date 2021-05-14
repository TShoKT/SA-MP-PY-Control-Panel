import time
import os
try:
	from samp_client.client import SampClient
	from samp_client.exceptions import SampError, RconError, InvalidRconPassword, ConnectionError
except ImportError:
	os.system("pip install samp-client")
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥#
CJERROR = lambda : write('Ah shit, here we go again\n',0.02)#
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥#
def Features():
	write("""		                                                                                      
----------------------------------------------------------------------------------------------   
-Rcon Cmdlist(0)                               |-Send Rcon password(1)                                              
----------------------------------------------------------------------------------------------                                               
-Restart Server->(GMX)(2)                      |-Show list of players(3)                                             
----------------------------------------------------------------------------------------------                                              
-Say in global server(4)                       |-Turn off Server(5)                                              
----------------------------------------------------------------------------------------------                                               
-Set Rcon passowrd(6)                          |-Show server status(7)                                             
----------------------------------------------------------------------------------------------                                              
-[Reload\\Load\\Unload] FilterScript by name(8)|-Set Server Status and Rules(9)               
----------------------------------------------------------------------------------------------
-Change Gamemode(10)                           |-ban or kick player(11)                                                                                                                    
\n""", 0.001)
def write(String : str, interval : int = 0.02):
	for i in list(String):
		print(i, end="",flush=True)
		time.sleep(interval)

def Exit():
	write("Do you want to exit?[y/n or Everything]: ")
	request = str(input())
	if request =="y":
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		exit()


class Samp():
	def __init__(self):
		self.Before_S()
	def Before_S(self):
		write("Please enter your Samp server address with port: ")
		result = str(input())
		if ":" not in list(result):
			CJERROR()
			write("Please enter port! example => 127.0.0.1:7777\n")
			return self.Before_S()

		result = result.replace(" ", "", result.count(" "))
		self.Address, self.Port = str(result).split(":")
		if (self.Port == "") or (len(self.Port) > 4 or len(self.Port) <4 ):
			CJERROR()
			write("Invalid Port\n")
			return self.Before_S()
		write("Please enter your server's rcon password: ")
		self.Password = input()
		self.Start()
	def Show_Status(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=str(self.Password)) as client:
			info = client.get_server_info()
			Rules = client.get_server_rules_dict()
			has_a_password = "Yes" if info.password else "No"
			write("[---------|Server Status|---------]\n", 0.02)
			write(f"""
|~	Address => {self.Address}:{self.Port}
|~  Hostname => {info.hostname}
|~	Players => {info.players}/{info.max_players}
|~	Mode => {info.gamemode}
|~	Language => {info.language}
|~	Has a password => {has_a_password}
			\n""",0.005)
			write("[---------|Server  Rules|---------]\n", 0.02)
			write(f"""
|~	Lagcomp => {Rules['lagcomp']}  
|~	Mapname => {Rules['mapname']}
|~	Version => {Rules['version']}
|~	Weather => {Rules['weather']}
|~	weburl => {Rules['weburl']}
|~	Worldtime => {Rules['worldtime']}
			\n""",0.005)
	def _0(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			for i in client.rcon_cmdlist():
				write(f"{i}\n",0.003)

	def _1(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			write("Please enter your Rcon command: ")
			cmd = str(input())
			client.send_rcon_command(cmd)
			write("Your command was sent successfully\n")

	def _2(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			client.rcon_gmx()
			write("The server is restarting!\n")
	def _3(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			if not client.rcon_players():
				CJERROR()
				write("No player is currently playing in the server.\n")
			else:
				l = "List of Players:\n"
				for i in client.get_server_clients_detailed():
					l+=f"ID: {i.id}, Name: {i.name}, Score: {i.score}, Ping: {i.ping}\n"
				write(f"{l}\n-----------------------------------------------------------\n",0.001)
	def _4(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:			
			write("Please enter your message: ")
			msg = str(input())
			client.rcon_say(msg)
			write(f"*Admin: {msg}\n")
	def _5(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:			
			client.rcon_exit()
			write("The server is now offline!\n")
	def _6(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			write("Please enter your new Rcon password: ")
			rpass = str(input())
			client.rcon_set_rcon_password(rpass)
	def _7(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			self.Show_Status()
	def _8(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			write("What do you want to do with FilterScript? | Options[reload, load ,unload, cancel]: ")
			Option = str(input())
			Options = ["load", "reload", "unload","cancel"]
			Option = Option.replace(" ", "", Option.count(" ")).lower()
			if Option not in Options:
				CJERROR()
				write("Invalid Option\n")
				self._8()
			else:
				write("Please enter your FilterScript name: ")
				fsname = str(input())
				try:
					if Option == Options[0]:
						client.rcon_loadfs(fsname)
					elif Option == Options[1]:
						client.rcon_reloadfs(fsname)
					elif Option == Options[2]:
						client.rcon_unloadfs(fsname)
					elif Option == Options[3]:
						pass	
				except SampError:
					CJERROR()
					write("Invalid FilterScript name\n")
	def _9(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			write("""
-Set HostName(0)
-Set ModeText(1)
-Set Language(2)
-Set Password(3)
-Set Mapname(4)
-Set Weahter(5)
-Set Weburl(6)
			\n""")
			try:
				f = int(input("Give number of feature: "))
			except ValueError:
				CJERROR()
				write("Please enter number!")
				self._9()
			if f == 0:
				write("Please enter your new Hostname: ")
				n = str(input())
				client.rcon_set_hostname(n)
				write(f"Hostname changed to {n}\n")
			elif f == 1:
				write("Please enter your new Modetext: ")
				n = str(input())
				client.rcon_set_gamemodetext(n)
				write(f"Modetext changed to {n}\n")
			elif f == 2:
				write("Please enter your new Language: ")
				lang = str(input())
				client.rcon_set_language(lang)
				write(f"Language changed to {lang}\n")
			elif f == 3:
				write("Please enter your new password or cancel: ")
				pw = str(input())
				if pw.lower() == "cancel":
					print("Ok")
				else:
					client.rcon_set_password(pw)
					write(f"Password changed to {pw}\n")
			elif f == 4:
				write("Please enter your new Mapname: ")
				mname = str(input())
				client.rcon_set_mapname(mname)
				write(f"Mapname changed to {mname}\n")
			elif f == 5:
				def get_weatherID():
					write("Please enter your new Weather ID: ")
					wid = str(input())
					if wid.isnumeric():
						client.rcon_weather(wid)
						write(f"Weahter ID changed to {wid}\n")
					else:
						write("Please enter number!\n")
						return get_weatherID()
				get_weatherID()
			elif f == 6:
				write("Please enter your new weburl: ")
				url = str(input())
				client.rcon_set_weburl(url)
				write(f"Weburl changed to {url}\n")
			else:
				CJERROR()
				write("Invalid number\n")
	def _10(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			write("Please enter Gamemode name: ")
			Gamemode = str(input())
			client.rcon_changemode(Gamemode)
			write(f"Gamemode changed to {Gamemode}\n")

	def _11(self):
		with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
			write("Please select one of the options | Options[kick, ban, banip, cancel]: ")
			Option = str(input())
			Options =["kick", "ban", "banip", "cancel"]
			Option = Option.replace(" ", "", Option.count(" ")).lower()
			def isnameorid(string, action):
				if action == "kick":
					if string.isnumeric():
						client.rcon_kick(string)
					else:
						pnames = [i.name.lower() for i in client.get_server_clients_detailed()]
						if string.lower() not in pnames:
							CJERROR()
							write("That player is not connected on server!\n")
						else:
							for player in client.get_server_clients_detailed():
								if player.name.lower() == string.lower():
									client.rcon_kick(player.id)

				elif action == "ban":
					if string.isnumeric():
						client.rcon_ban(string)
					else:
						pnames = [i.name.lower() for i in client.get_server_clients_detailed()]
						if string.lower() not in pnames:
							CJERROR()
							write("That player is not connected on server!\n")
							Exit()
						else:
							for player in client.rcon_players():
								if player.name.lower() == string.lower():
									client.rcon_ban(player.id)
			if Option not in Options:
				CJERROR()
				write("Invalid Option\n")
				self._11()
			else:
				if Option == Options[0]:
					write("Please enter player id or name: ")
					nameorid = str(input())
					isnameorid(nameorid, Options[0])
				elif Option == Options[1]:
					write("Please enter player id or name: ")
					nameorid = str(input())
					isnameorid(nameorid, Options[1])
				elif Option == Options[2]:
					write("Please enter player ip")
					ip = str(input())
					client.rcon_banip(ip)
				elif Option == Options[3]:
					pass

	def Start(self):
		try:
			with SampClient(address=str(self.Address), port=int(self.Port), rcon_password=self.Password) as client:
				self.Show_Status()
				if client.rcon_cmdlist() == []:
					raise InvalidRconPassword
				def Continuation():
					def wait():
						Exit()
						Continuation()
					Features()
					try:
						f = int(input("Give number of feature: "))
						flist = [self._0, self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9,self._10,self._11]
						if f > len(flist) or f < 0:
							raise IndexError
						flist[f]()
						wait()
					except IndexError:
						CJERROR()
						write("Invalid Number!\n")
						Continuation()
					except ValueError:
						CJERROR()
						write("Please enter number!")
						Continuation()

				Continuation()
		except ConnectionError:
			CJERROR()
			write("-Your internet is not connected or has a problem\n-The address and port you entered are incorrect\n-The server is offline\n")
			Exit()
			Samp().Start()
		except InvalidRconPassword:
			CJERROR()
			write("The rcon password you have entered is invalid, you can't use this features.\n")
			Exit()
			Samp().Start()
		except Exception as e:
			CJERROR()
			print(e)
			write("If you see a bug, raise it here\n")
			Continuation()

Samp()#RUN
