from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID =   # my telegram ID
    OWNER_USERNAME = ""  # my telegram username
    API_KEY = ""  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresql@localhost:5432/Telegram'  # sample db credentials
    MESSAGE_DUMP = None # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
