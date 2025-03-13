from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27758016"))
API_HASH = getenv("API_HASH", "8d34cfffe27ab461eabbf0091b1a27df")
BOT_TOKEN = getenv("BOT_TOKEN", "7616922989:AAHbdtrlRiglOthKAGOO2cyN9TAsWxVvqDc")
OWNER_ID = int(getenv("OWNER_ID", "7364852621"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fireteam875:fireteam875@cluster0.z4jsh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUPPORT_GRP = getenv("SUPPORT_GRP", "https://t.me/THE_ARCHITECT_II")
UPDATE_CHNL = getenv("UPDATE_CHNL", "THE_ARCHITECT_II")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Shunn_Mizushino")

# Random Start Images
IMG = [
    "https://graph.org/file/62d62bb8916c551d16605-a2aa0f7d5e3ef85ecb.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAxkBAAEBJhJn0zy3Dyb8tB90aW_kTRDSXF22TwACEAgAAuX8EVa5r3qLhL4JaTYE",
    "CAACAgUAAxkBAAEBJhBn0zyiL5zlac377Su-PjI_iiqjFgAC-w8AAtf9qVZNgS1UEqYsFDYE",
    "CAACAgUAAxkBAAEBJg5n0zyClxv-W42IoNCt1vcLg2NxxgACeAwAAsjxoFbK7ORKLb-drzYE",
]


EMOJIOS = [
    "🎲",
    "🔥",
    "⚡️",
    "⛈",
    "🌩",
    "🌦",
    "☀️",
    "💫",
    "🐳",
    "🦑",
]
