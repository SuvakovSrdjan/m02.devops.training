import datastore
def process_and_store(key, raw_value):
    stored_value = raw_value.strip().upper()
    datastore.store_value(key, stored_value)
    return stored_value

def retrieve_processed(key):
    stored_value = datastore.get_value(key)
    return stored_value.lower() if stored_value else None


def update_value(key, raw_value):
    if datastore.get_value(key) is None:
        raise KeyError(f"Key '{key}' does not exist.")
    stored_value = raw_value.strip().upper()
    datastore.store_value(key, stored_value)
    return stored_value

def delete_value(key):
    if datastore.get_value(key) is None:
        return False
    else:
        datastore.delete_value(key)
        return True


def list_all_keys():
    return datastore.list_keys()
