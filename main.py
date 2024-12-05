from telethon import TelegramClient, sync
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
CHANNEL_USERNAME = '@ielts_thematic_tests'
DOWNLOAD_PATH = '/Users/asrornomozov/Desktop/ListeningAudio'
START_MESSAGE_ID = 270

client = TelegramClient('session_name', API_ID, API_HASH)
client.start()

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)


def download_mp3_files_from_channel(channel, download_path, start_message_id):
    messages = client.get_messages(channel, limit=127, offset_id=start_message_id)
    for msg in messages:
        if msg.file and msg.file.name and msg.file.name.endswith('.mp3'):
            print(f"Yuklanmoqda: {msg.file.name}")
            file_path = client.download_media(msg, file=download_path)
            if file_path:
                print(f"Yuklandi: {file_path}")
            else:
                print(f"Xato: Fayl yuklanmadi - {msg.file.name}")


download_mp3_files_from_channel(CHANNEL_USERNAME, DOWNLOAD_PATH, START_MESSAGE_ID)

client.disconnect()
