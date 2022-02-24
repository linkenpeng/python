#!/usr/bin/env python

import time
import hashlib
import requests

""""
  Args:
      params:
          接口接受参数
  Returns:
      sign
"""
def get_sign(params):
    apiKey = ""
    apiPwd = ""

    timestamp = int(time.time() * 1000)
    params['api_key'] = apiKey
    params['timestamp'] = timestamp

    sorted(params)
    pre_list = [str(k) + "=" + str(v) for k, v in params.items()]
    pre_str = "&".join(pre_list)

    print(pre_str)

    res_str = apiKey + apiKey + apiPwd + "a" + pre_str + apiKey + "b" + apiPwd

    ##hash_obj = hashlib.sha256(bytes(apiPwd, encoding="utf-8"))

    api_sign = hashlib.sha256(res_str.encode('utf-8')).hexdigest()


    ##hash_obj.update(res_str.encode('utf-8'))
    ##api_sign = hash_obj.hexdigest()

    print(api_sign)
    return api_sign

def get_api_data(params, api_url):
    api_sign = get_sign(params)
    params['api_sign'] = api_sign
    print(params)
    response_data = requests.post(api_url, params)
    return response_data.content.decode()

if __name__ == '__main__':
    api_url = "https://mystore-uat.watsonsestore.com.cn/spaceage/user/info";
    params = {'access_token': 'SADZ1AT1FyGmwOkCvpROy6XZ'}
    json_data = get_api_data(params, api_url)
    print(json_data)

