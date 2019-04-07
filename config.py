class Config(object):

    def __init__(self, config_name):
        filename = '{}.conf'.format(config_name)
        with open(filename, 'r') as config:
            for line in config.readlines():
                attr, value = line.strip().split('=')
                setattr(self, attr, value)
