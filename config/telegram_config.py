import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
MY_TELEGRAM_ID = os.getenv('MY_TELEGRAM_ID')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
BOT_ID = os.getenv('BOT_ID')
