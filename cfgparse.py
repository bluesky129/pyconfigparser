def get_item(config, section, key):
    """
    Return property value or throw an Exception if it cannot be found.
    
    :param config: Configuration parser instance.
    :param section: Section name in configuration with property to look for.
    :param key: Name of the key to look for in section.
    :return: Key string value.
    """
    try:
        # Python 3
        section = config[section]
        if key not in section:
            raise Exception('"{0}" configuration section must provide "{1}".'.format(section, key))
        return section[key]
    except AttributeError:
        # Python 2
        if not config.has_option(section, key):
            raise Exception('"{0}" configuration section must provide "{1}".'.format(section, key))
        return config.get(section, key)


def get_item_default(config, section, key, default_value):
    """
    Return property value or provided default value if it cannot be found.
    
    :param config: Configuration parser instance.
    :param section: Section name in configuration with property to look for.
    :param key: Name of the key to look for in section.
    :param default_value: Value to return if key cannot be found.
    :return: Key string value or default value.
    """
    try:
        # Python 3
        section_dict = config[section]
        return section_dict[key] if key in section_dict else default_value
    except AttributeError:
        # Python 2
        return config.get(section, key) if config.has_option(section, key) else default_value