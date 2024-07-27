from telethon import events

def register_help_command(client):
    @client.on(events.NewMessage(outgoing=True, pattern='Xhelp'))
    async def help_command(event):
        help_text = """
<b>🆘 Доступные команды:</b>

<b>Основные:</b>
- <code>Xping</code>: Пинг??
- <code>Xtime [секунды]</code>: Текущее время на хосте или перевод секунд в ЧЧ:ММ:СС
- <code>Xuptime</code>: Время работы бота.
- <code>Xinfo</code>: Информация о боте.

<b>Аватарки:</b>
- <code>Xava</code>: Флудит аватарками.

<b>Управление:</b>
- <code>Xrestart</code>: Перезапуск селфбота.
- <code>Xstop</code>: Остановка селфбота.

<b>Для подробной информации о команде используйте:</b>
<code>Xhelp <команда></code>
        """
        await event.edit(help_text, parse_mode='html')

    @client.on(events.NewMessage(outgoing=True, pattern='Xhelp (.*)'))
    async def detailed_help_command(event):
        command = event.pattern_match.group(1)
        detailed_texts = {
            'ping': """
<b>📶 Xping:</b>
Проверка пинга. 

<b>Использование:</b>
<code>Xping</code>
            """,
            'time': """
<b>⏰ Xtime [секунды]:</b>
Показывает текущее время или переводит заданное количество секунд в формат ЧЧ:ММ:СС.

<b>Использование:</b>
<code>Xtime [секунды]</code>
            """,
            'uptime': """
<b>⏳ Xuptime:</b>
Показывает время работы бота с момента его запуска.

<b>Использование:</b>
<code>Xuptime</code>
            """,
            'info': """
<b>ℹ️ Xinfo:</b>
Предоставляет информацию о селфботе.

<b>Использование:</b>
<code>Xinfo</code>
            """,
            'ava': """
<b>🖼️ Xava:</b>
Флудит аватарками

<b>Использование:</b>
<code>Xava</code> или <code>Xava [аргумент]</code>

<b>Аргументы:</b>
- <code>stop</code>: Прекращает процесс смены аватарок. Команда завершит текущий цикл установки и остановит все дальнейшие изменения аватарок.
- <code>resume</code>: Возобновляет процесс смены аватарок после того, как он был остановлен.
- <code>change</code>: В процессе подменивает файл аватарки на тот, что был скачан из ответа на медиа.


            """,
            'restart': """
<b>🔄 Xrestart:</b>
Перезапускает селфбота.

<b>Использование:</b>
<code>Xrestart</code>
            """,
            'stop': """
<b>🛑 Xstop:</b>
Останавливает работу селфбота.

<b>Использование:</b>
<code>Xstop</code>
            """
        }

        detailed_text = detailed_texts.get(command, "<b>Неизвестная команда.</b>")
        await event.edit(detailed_text, parse_mode='html')
