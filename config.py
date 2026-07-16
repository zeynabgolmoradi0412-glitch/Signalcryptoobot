import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Binance
EXCHANGE = "binance"
TIMEFRAME = "15m"

# Scan settings
SCAN_INTERVAL = 300  # 5 minutes

# Technical indicators
RSI_PERIOD = 14
EMA_FAST = 20
EMA_SLOW = 50
EMA_TREND = 200

# Signal score
MIN_SCORE = 8
