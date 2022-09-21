##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
