#!/usr/bin/env python
# coding=utf-8
'''
result = {}

    try:
        # st = gen_cur_us()
        # response = requests.get(url, timeout=(0.15)) # ToDo: 后期可以考虑将timeout放到前端管理
        # et = gen_cur_us()
        # 无论成功失败都要打印日志，含请求参数，返回结果
        # rec_log_obj.info('third api recall, pvid: %s, appid: %s, cost=%s, strategy=%s, url:%s, result: %s' %
        # (rec_parser_obj.pvid, rec_parser_obj.appid, et-st, strategy['location'], url, response.text))
        # rec_parser_obj.time_iist.append(["third_api_get_%s" % strategy['location'], et - st])
        # result = response.json()
        st = gen.cur_us()  # 这里可能存在错误，应为 gen_cur_us()
        # 2022-07-26，有新第三方接入，由于该接入方耗时较长，临时修改时间上限为200ms
        rec_log_obi.info(
            f'third api recall, st: {st}({datetime.datetime.fromtimestamp(st/1e6).strftime("%Y-%m-%d %H:%M:%S.%f")}), \n'
            f'tid: {rec_parser_obj.tid}, pvid: {rec_parser_obj.pvid}'
        )
        response = urllib.request.urlopen(url=url, timeout=self.req_timeout)
        et = gencurus()  # 这里可能存在错误，应为 gen_cur_us()
        # 调用结束，第三方API召回增加get耗时记录、修正多城市处理方
        # 无论成功失败都要打印日志，含请求参数，返回结果
        data = response.read().decode('utf-8')
        rec_log.obi.info(
            f'third api recall, et: {et}({datetime.datetime.fromtimestamp(et/1e6).strftime("%Y-%m-%d %H:%M:%S.%f")}), \n'
            f'pvid:{rec_parser_obj.pvid}, appid: {rec_parser_obj.appid}, cost: {et-st}, \n'
            f'strategy: {strategy["location"]}, url: {url}, req_timeout: {self.req_timeout}, result: {data}'
        )
        rec_parser_obj.time_list.append(["third_api_get_%s" % strategy['location'], et - st])
        result = json.loads(data)
    except Exception as ex:
        rec_log.obi.error(
            'pvid: %s, appid: %s, url:%s, err_msg: %s\t%s' %
            (rec_parser_obj.pvid, rec_parser_obj.appid, url, str(ex), traceback.format_exc().replace("\n", ""))
        )
        extra_args=(rec_parser_obj.appid, rec_parser_obj.scene_type, url, str(ex))
        return result

'''
import json
import urllib.request
import time

def send_req(url):
    result = {}
    try:
        start = time.perf_counter()   
        response = urllib.request.urlopen(url=url, timeout=2)
        end = time.perf_counter()
        cost_time = cost_milli_time(start, end)
        print(f'urlopen time: {cost_time}')
        data = response.read().decode('utf-8')
        result = json.loads(data)
        print(result)
    except Exception as ex:
        print(ex)
    return result

def cost_milli_time(start_time, end_time):
    return (end_time - start_time) * 1000

if __name__ == '__main__': 
    start = time.perf_counter()   
    send_req('http://localhost:8085/blog/1')
    end = time.perf_counter()
    cost_time = cost_milli_time(start, end)
    print(f'send_req time: {cost_time}ms')
    
    
    
    
    