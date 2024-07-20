from telethon import events

def register_help_command(client):
    @client.on(events.NewMessage(outgoing=True, pattern='Xhelp'))
    async def help_command(event):
        help_text = """
<b>🆘 Список доступных команд:</b>

<b>Основные команды:</b>
- <code>Xping</code>: Пинг Понг!
- <code>Xtime [секунды]</code>: Вывод текущего времени или, если есть аргументы переводит секунды в ЧЧ:ММ:СС 
- <code>Xuptime</code>: Время работы селфбота.
- <code>Xinfo</code>: Информация о селфботе.

<b>!!клепать аватарки тут!!:</b>
- <code>Xava</code>: Зацикливает установку вашей аватарки.

<b>Управление ботом:</b>
- <code>Xrestart</code>: Перезапуск селфбота.
- <code>Xstop</code>: Остановка работы селфбота.
        """
        await event.edit(help_text, parse_mode='html')
