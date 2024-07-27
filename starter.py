import os
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import ApiIdInvalidError
from config import get_config, prompt_config

def start_client():
    session_name = os.path.join('misc', 'sessions', 'selfdestruct')
    config_file = os.path.join('misc', 'cfg', 'config.cfg')

    os.makedirs(os.path.dirname(session_name), exist_ok=True)

    try:
        api_id, api_hash = get_config(config_file)
        client = TelegramClient(session_name, api_id, api_hash).start()
        return client
    except ApiIdInvalidError:
        print("Ошибка: комбинация API ID/API Hash хуйня.")
        os.remove(config_file)
        api_id, api_hash = prompt_config(config_file)
        client = TelegramClient(session_name, api_id, api_hash).start()
        return client
