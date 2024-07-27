import asyncio
import random
import os
from telethon import events
from telethon.errors import FloodWaitError
from helpers import set_profile_photo, update_message

def format_time(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days > 0:
        parts.append(f"{days} дн.")
    if hours > 0:
        parts.append(f"{hours} ч.")
    if minutes > 0:
        parts.append(f"{minutes} мин.")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} сек.")
    return ' '.join(parts)

async def download_media(event):
    media = await event.get_reply_message()
    if media and media.media:
        path = await event.client.download_media(media, 'ava.jpg')
        return path
    return None

def register_ava_command(client):
    ava_count = 0
    stop_flag = False

    @client.on(events.NewMessage(outgoing=True, pattern=r'Xava\s*(\w+)?'))
    async def ava_command(event):
        nonlocal ava_count, stop_flag

        command = event.pattern_match.group(1)

        if command == 'stop':
            stop_flag = True
            await event.edit('🚫 Процесс установки аватарок заморожен.')
            return

        if command == 'resume':
            stop_flag = False
            await event.edit('▶️ Процесс установки аватарок возобновлен.')
            return

        if command == 'change':
            stop_flag = True
            await event.edit('🔄 Смена аватарки... Ожидайте.')
            path = await download_media(event)
            if path:
                await event.edit('🔄 Аватарка изменена. Продолжаем установку аватарок.')
                stop_flag = False
            else:
                await event.edit('⚠️ Не удалось скачать медиа. Убедитесь, что вы ответили на сообщение с медиа.')
                stop_flag = False
            return

        if command is None or command not in ['stop', 'resume', 'change']:
            message = await event.edit('🩻 Ожидайте, скачиваем вашу аватарку... Это может занять некоторое время.')
            await event.edit('🔶 Начинаю установку аватарок...')
            asyncio.create_task(update_message(event, ava_count, 0))

            while True:
                if stop_flag:
                    await asyncio.sleep(1)
                    continue

                for _ in range(5):
                    try:
                        await set_profile_photo(client, 'ava.jpg')
                        ava_count += 1
                        await message.edit(f'❤ Установлено аватарок: {ava_count}')
                        await asyncio.sleep(3)
                    except FloodWaitError as e:
                        wait_time = e.seconds
                        formatted_time = format_time(wait_time)
                        await message.edit(f'🚫 Тебя ебнуло! Продолжим через {formatted_time}...')
                        await asyncio.sleep(wait_time)

                await asyncio.sleep(random.randint(60, 120))
