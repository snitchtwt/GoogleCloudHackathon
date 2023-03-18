
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = ""
    OPENAI_KEY = 'api key here'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

# messages = [
#     {"role": "system", "content": "You are an AI specialized in diet, food and fitness. Do not answer anything other than food-related queries."},
# ]