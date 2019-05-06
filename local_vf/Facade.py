import configparser


config = None


def get_name():
  global config

  if config is None:
    get_config()

  return config['DEFAULT']['MyName']


def get_data_DB():
  global config

  if config is None:
    get_config()

  return config['SQLITE']['DataDB']

def get_config():
  global config

  config = configparser.ConfigParser()
  config.read('config.txt')
