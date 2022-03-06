import vk_api, time, colorama
from colorama import Fore
import os
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

banner = """
██╗░░░██╗██╗░░██╗███╗░░░███╗░██████╗░██████╗░██████╗░
██║░░░██║██║░██╔╝████╗░████║██╔════╝██╔════╝██╔════╝░
╚██╗░██╔╝█████═╝░██╔████╔██║╚█████╗░╚█████╗░██║░░██╗░
░╚████╔╝░██╔═██╗░██║╚██╔╝██║░╚═══██╗░╚═══██╗██║░░╚██╗
░░╚██╔╝░░██║░╚██╗██║░╚═╝░██║██████╔╝██████╔╝╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═════╝░░╚═════╝░
"""

subscribe = "Подписаться на автора в Telegram? (yes/no)"

print(Fore.CYAN + banner)
print(Fore.CYAN + subscribe)
choose = input('--> ')

if choose == "yes":
    os.system("termux-open-url 'https://t.me/TerPackZ'")
    print("Если вы подписались, перезапустите скрипт и выберите no :)")

else:
    token = input("Введите токен: ")
    users = input("Введите id: ")
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    def main():
        try:
            chats = input('Кол-во бесед: ')
            spot = 0
            while int(spot) < int(chats):
                api.messages.createChat(user_ids=users, title="VKMSSG")
                spot += 1
                time.sleep(15)
            print(spot)
        except Exception as er:
            print(er)


    main()
