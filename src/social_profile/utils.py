import uuid

def get_random_code(value)-> str:
    code = str(uuid.uuid5(uuid.NAMESPACE_DNS, value))[:8].replace("-", "").lower()
    return code
