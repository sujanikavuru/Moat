import configparser

config = configparser.RawConfigParser()
config.read('./configurations/conf.ini')


class ReadConfig:

    @staticmethod
    def getApplicationURl():
        url = config.get('AppUrl', 'baseURL')
        return url

    @staticmethod
    def getSearchInput():
        search_word = config.get('SearchInput', 'SearchText')
        return search_word


