database = {}


def store_value(key, value):
    database[key] = value


def get_value(key):
    return database[key] if key in database else None

def delete_value(key):
    if key in database:
        del database[key]

def list_keys():
    return list(database.keys())
