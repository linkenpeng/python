# -*- coding: utf-8 -*-
class ConfigUtil:
    def __init__(self):
        pass

    def get_config(self, file_path):
        config = {}
        with open(file_path) as file:
            for line in file:
                kv = line.split('=')
                config[kv[0]] = kv[1].strip('\n')
        return config