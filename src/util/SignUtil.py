import hashlib

class SignUtil:
    def __init__(self):
        pass

    def get_auth_string(self, config):
        authText = ('accessKey=' + config['accessKey']
                    + '&accessSecret=' + config['accessSecret']
                    + '&timestamp=' + config['timestamp'])
        hash_object = hashlib.sha256(authText.encode())
        authString = hash_object.hexdigest().upper()
        return authString