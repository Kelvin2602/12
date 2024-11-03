from dotenv import load_dotenv
import os

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_IDS = [int(id) for id in os.getenv('ADMIN_IDS', '').split(',') if id]

# Break Time Limits (minutes)
LUNCH_BREAK_LIMIT = 30
SMOKE_BREAK_LIMIT = 10
RESTROOM_BREAK_LIMIT = 5

# Shift Settings
AUTO_END_SHIFT_HOUR = 2  # 2 AM