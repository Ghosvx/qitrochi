import time
from telethon import events

def register_uptime_command(client, start_time):
    @client.on(events.NewMessage(outgoing=True, pattern='Xuptime'))
    async def uptime_command(event):
        current_time = time.time()
        uptime_seconds = int(current_time - start_time)
        uptime_days = uptime_seconds // 86400
        uptime_seconds %= 86400
        uptime_hours = uptime_seconds // 3600
        uptime_seconds %= 3600
        uptime_minutes = uptime_seconds // 60
        uptime_seconds %= 60
        uptime_message = '💿 Время работы бота: '
        if uptime_days > 0:
            uptime_message += f'{uptime_days} дн. '
        uptime_message += f'{uptime_hours} ч. {uptime_minutes} мин. {uptime_seconds} сек.'
        
        await event.message.edit(uptime_message)
