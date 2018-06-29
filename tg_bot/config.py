from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 136761746  # my telegram ID
    OWNER_USERNAME = "__init__"  # my telegram username
    API_KEY = "601399246:AAEdhxmrfeoccTQtiY0c7sRI_S9VpVS8qz0"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresql:5432/Telegram'  # sample db credentials
    MESSAGE_DUMP = None # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [5522373,138312364,97492356,167623566]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
