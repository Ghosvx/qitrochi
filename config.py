import os
import re

def get_config(config_file):
    config_dir = os.path.dirname(config_file)
    os.makedirs(config_dir, exist_ok=True)

    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.read().splitlines()
        if len(lines) >= 2:
            return lines[:2]
        else:
            return prompt_config(config_file)
    else:
        return prompt_config(config_file)

def prompt_config(config_file):
    print("Заполните поля ниже.")
    print("🔎 Если вы не знаете где взять данные, то идите нахуй.")

    while True:
        api_id = input("Введите API ID: ")
        if api_id.isdigit() and len(api_id) > 5:
            break
        else:
            print("Некорректный API ID. Пожалуйста, введите правильный API ID.")

    while True:
        api_hash = input("Введите API Hash: ")
        if re.match(r"^[0-9a-fA-F]{32}$", api_hash):
            break
        else:
            print("Некорректный API Hash. Пожалуйста, введите правильный API Hash.")

    with open(config_file, 'w') as f:
        f.write(api_id + '\n')
        f.write(api_hash + '\n')

    print("Готово! Эти данные не надо будет вводить в будущем.")
    return api_id, api_hash