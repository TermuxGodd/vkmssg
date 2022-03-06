import vk
import vk_api
import pyfiglet
from colorama import init, Fore, Back, Style
import random
import time
import os
import sys

banner = """
██╗░░░██╗██╗░░██╗░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗
██║░░░██║██║░██╔╝██╔══██╗██╔══██╗████╗░████║████╗░████║
╚██╗░██╔╝█████═╝░██║░░╚═╝██║░░██║██╔████╔██║██╔████╔██║
░╚████╔╝░██╔═██╗░██║░░██╗██║░░██║██║╚██╔╝██║██║╚██╔╝██║
░░╚██╔╝░░██║░╚██╗╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝
"""

subscribe = """
Подписаться на автора в Telegram? (yes/no)
"""
print(Fore.CYAN + banner)
print(Fore.CYAN + subscribe)

choose = input('--> ')

if choose == "yes":
    os.system("termux-open-url 'https://t.me/TerPackZ'")
    print("Если вы подписались, перезапустите скрипт :)")
    exit()
else:
    token = input("Введите токен: ")
    user_id = input("Введите айди страницы: ")
    posts_id = input("Введите айди поста: ")
    msgs = input("Введите сообщение: ")
    session = vk.Session(access_token=token)
    apivk = vk.API(session, v=5.95)
    number = 0
while True:
    try:
        print(apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs,
                                       guid=random.randint(0, 9999999999)))
        print("Комментарий добавлен")
        print(number)
        number += 1
    except:
        pass
    time.sleep(1.5)

