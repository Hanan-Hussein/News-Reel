import os
# print(os.environ)
class Config:
    """
    This are the general configurations for the projects
    """
    NEWS_APP_API_KEY=os.environ.get('NEWS_APP_API_KEY')
    NEWS_BASE_URL_SOURCES = 'http://newsapi.org/v2/top-headlines/sources?apikey={}&language=en'
    NEWS_BASE_URL_ARTICLES = 'http://newsapi.org/v2/top-headlines?sources={}&apikey={}&language=en'
    NEWS_BASE_URL_CATEGORIES = 'http://newsapi.org/v2/top-headlines?category={}&apikey={}&language=en'
    NEWS_BASE_URL_TOP_STORIES = 'http://newsapi.org/v2/top-headlines?country={}&apiKey={}&page={}&PageSize={}&language=en'
class ProdConfig(Config):
    """
    This are the configurations for the production environment

    Args:
        Config : The main configuration
    """
    pass

class DevConfig(Config):
    """
    This are the configurations for the development environment

    Args:
        Config : The main configuration
    """
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}