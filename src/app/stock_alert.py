# -*- coding: utf-8 -*-
"""
持仓监控脚本 —— 每晚 15:05 跑
功能：跌破20日线 / 放量1.5倍  → 邮件+微信提醒
作者：你本人
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/src')
import tushare as ts
import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from util.ConfigUtil import ConfigUtil

# ========== 1. 改成你自己的 ==========
MY_STOCKS = {'601138.SH': 1, '000858.SZ': 1}   # 代码: 持仓手数（随便填）
ConfigUtil = ConfigUtil()
config = ConfigUtil.get_config('src/config/prd.txt')
# https://tushare.pro/register → 个人中心 → 接口TOKEN
TU_TOKEN   = config['TU_TOKEN']
# https://sct.ftqq.com → 微信扫码 → 拿到 SENDKEY
SCT_KEY    = config['SCT_KEY']
MAIL_USER  = config['MAIL_USER']
MAIL_PASS  = config['MAIL_PASS']
MAIL_TO    = config['MAIL_TO']
# =======================================

ts.set_token(TU_TOKEN)
pro = ts.pro_api()

def send_wechat(title):
    url = f'https://sctapi.ftqq.com/{SCT_KEY}.send'
    requests.post(url, data={'title': title, 'desp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

def send_mail(body):
    msg = MIMEText(body)
    msg['Subject'] = '持仓预警'
    msg['From'] = MAIL_USER
    msg['To'] = MAIL_TO
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
        smtp.login(MAIL_USER, MAIL_PASS)
        smtp.send_message(msg)

def alert():
    codes = ','.join(MY_STOCKS.keys())
    today = datetime.now().strftime('%Y%m%d')
    # 当日行情
    daily = pro.daily(trade_date=today, ts_code=codes)
    # 20 日均线
    ma20d = {}
    for code in MY_STOCKS:
        df = pro.daily(ts_code=code, start_date=(datetime.now()-timedelta(30)).strftime('%Y%m%d'))
        # 1. 跌破20日线
        print(df['close'])
        ma20 = df['close'].rolling(20).iloc[-1]
        ma20d[code] = ma20
    # 比对
    alerts = []
    for _, row in daily.iterrows():
        code, close, vol = row.ts_code, row.close, row.vol
        # 1. 跌破20日线
        if close < ma20d[code]:
            alerts.append(f'{code} 收盘价 {close} 跌破20日线 {ma20d[code]:.2f}')
        # 2. 放量
        df = pro.daily(ts_code=code, start_date=(datetime.now()-timedelta(10)).strftime('%Y%m%d'))
        avg_vol = df['vol'][-5:].mean()
        if vol > avg_vol * 1.5:
            alerts.append(f'{code} 放量 {vol/avg_vol:.1f} 倍')
    if alerts:
        text = '\n'.join(alerts)
        send_wechat('持仓预警')
        send_mail(text)
        print('已发送提醒:\n', text)
    else:
        print('一切正常，无提醒')

if __name__ == '__main__':
    alert()