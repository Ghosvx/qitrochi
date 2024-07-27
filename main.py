import os
import time
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import ApiIdInvalidError
from commands import register_all_commands
from helpers import set_profile_photo, get_self_avatar, update_message
from starter import start_client
from colorama import Fore, Style

client = start_client()

me = client.get_me()

os.system('cls' if os.name == 'nt' else 'clear')

print("  _. o _|_ ._ _   _ |_  ", Fore.MAGENTA + "o " + Style.RESET_ALL)
print(" (_| |  |_ | (_) (_ | | ", Fore.CYAN + "| " + Style.RESET_ALL)
print("   |                     ")
print(Fore.CYAN + " v0.02", Fore.RED + "x1" + Style.RESET_ALL)
print(Fore.GREEN + f"Здраствуйте, {me.first_name}!" + Style.RESET_ALL)

start_time = time.time()

register_all_commands(client, start_time, me)

client.run_until_disconnected()
