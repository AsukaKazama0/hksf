from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Generating a new one
api_id = 7577827
api_hash = "042f47a7b2413583d1d80cd261e82f35"
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())

# Converting SQLite (or any) to StringSession
with TelegramClient(name, api_id, api_hash) as client:
    print(StringSession.save(client.session))

# Usage
string = '1aaNk8EX-YRfwoRsebUkugFvht6DUPi_Q25UOCzOAqzc...'
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hi'))