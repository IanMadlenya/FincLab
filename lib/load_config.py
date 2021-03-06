"""
Module: To load settings from config.ini
"""

from configparser import ConfigParser


def load_config(section='MySQL_root', filename='config.ini'):
    """
    Read database configuration file and return a dictionary object.

    :param filename: name of the configuration file
    :param section: section of database configuration

    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to 'mysql'
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file.'.format(section, filename))

    return db


if __name__ == '__main__':
    print(load_config())
