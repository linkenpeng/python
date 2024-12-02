import sys
import json

sys.path.append('../')

class MockUtil:
    def __init__(self):
        pass

    def get_config(self, file_path):
        config = {}
        with open(file_path) as file:
            for line in file:
                kv = line.split('=')
                config[kv[0]] = kv[1].strip('\n')
        return config

    def get_test_data(self, file_path):
        with open(file_path) as f:
            post_data = f.read()
        print(f'post_data: {post_data}')
        json_data = json.dumps(post_data)
        print(f'json_data: {json_data}')
        return json_data