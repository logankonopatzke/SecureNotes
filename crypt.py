import base64

def encrypt(data, key):
    new_data = data + key
    message_bytes = new_data.encode('ascii')
    msg = base64.b64encode(message_bytes)

    return msg.decode('ascii')


def decrypt(data, key):
    message_bytes = data.encode('ascii')
    msg = base64.b64decode(message_bytes)
    raw = msg.decode('ascii')

    return raw[0:len(raw) - len(key)]