import os

class Config:

    RESTOURANT_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    RESTOURANT_API_KEY = os.environ.get('RESTOURANT_API')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}