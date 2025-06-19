#  This file was modified to support environment variables securely.
#  Original credits preserved: @MrMNTG @MusammilN

import os

SESSION = os.environ.get("SESSION")  # Session name for Pyrogram Client
API_ID = int(os.environ.get("API_ID"))  # Telegram API ID
API_HASH = os.environ.get("API_HASH")  # Telegram API Hash
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Bot Token from BotFather
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))  # Log channel/chat ID
KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL")  # URL to ping to keep alive
DEFAULT_AUTH_CHANNELS = eval(os.environ.get("DEFAULT_AUTH_CHANNELS", "[]"))  # Default auth channel list
LOG_STR = os.environ.get("LOG_STR", "✅ Bot deployed successfully!")  # Startup log message
