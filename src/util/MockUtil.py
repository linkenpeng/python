import sys
import json

class MockUtil:
    def __init__(self):
        pass
    
    def get_test_data(self, file_path):
        with open(file_path) as f:
            post_data = f.read()
        print(f'post_data: {post_data}')
        json_data = json.dumps(post_data)
        print(f'json_data: {json_data}')
        return json_data