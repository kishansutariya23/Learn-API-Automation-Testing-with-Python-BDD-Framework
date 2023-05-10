import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('Project4/utilities/properties.ini')
    return config


