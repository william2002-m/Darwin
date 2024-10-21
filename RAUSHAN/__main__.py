from flask import Flask
from RAUSHAN import LOGGER, AMBOT

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    LOGGER.info("The PURVI CHAT BOT Started.")
    # Run Flask server on port 8000
    app.run(host="0.0.0.0", port=8000)
    # Start the bot
    AMBOT().run()
