# config.py - Production Forwarder Configuration
import os
from dotenv import load_dotenv

load_dotenv()

# --- API Credentials ---
API_ID = 20000000  # REPLACE with your real API ID
API_HASH = 'your_api_hash_here' # REPLACE with your real API HASH
SESSION_NAME = 'production_stealth_v2'

# --- Source & Targets ---
SOURCE_CHAT_ID = -1001234567890
MESSAGE_ID = 12345
TARGETS = {
    -1009876543210: None,       # Regular Group
    -1001112223334: 456,        # Forum Topic ID 456
}

# --- S24 Ultra / Android 14 Fingerprint ---
DEVICE_MODEL = "SM-S928B"
SYSTEM_VERSION = "Android 16"
APP_VERSION = "10.14.3"
LANG_CODE = "en-US"
SYSTEM_LANG_CODE = "en-US"

# --- Stealth & Timing (Production Grade) ---
FORWARD_JITTER = (60, 180)      # 1–3 minutes between each forward
HUMAN_NOISE_INTERVAL = (1800, 3600)  # 30–60 minutes for "Human Noise" tasks
TYPING_DURATION = 5
SCROLL_LIMIT = 3
LOG_FILE = "bot.log"
