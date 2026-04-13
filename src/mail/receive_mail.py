import os
import time
import requests
from datetime import datetime, timedelta
import pymysql
from dotenv import load_dotenv

load_dotenv()

# -------------------
# 1. Graph 认证
# -------------------
def get_graph_token():
    url = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "scope": "https://graph.microsoft.com/.default"
    }
    resp = requests.post(url, data=data)
    resp.raise_for_status()
    return resp.json()["access_token"]

# -------------------
# 2. 获取最近新邮件
# -------------------
def get_new_emails(token, last_check_time):
    headers = {
        "Authorization": f"Bearer {token}",
        "Prefer": "outlook.body-content-type='text,html'"
    }
    # 筛选：最近N分钟未读/新邮件
    filter_time = last_check_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    params = {
        "$filter": f"receivedDateTime ge {filter_time}",
        "$orderby": "receivedDateTime desc",
        "$select": "id,subject,from,toRecipients,ccRecipients,receivedDateTime,body,hasAttachments"
    }
    url = "https://graph.microsoft.com/v1.0/me/messages"
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json().get("value", [])

# -------------------
# 3. 数据库插入
# -------------------
def insert_mail(db_conn, mail):
    cursor = db_conn.cursor()
    sql = """
    INSERT IGNORE INTO outlook_mails
    (mail_id, subject, sender_name, sender_email, to_list, cc_list,
     received_at, body_plain, body_html, has_attach)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # 解析发件人
    sender = mail.get("from", {}).get("emailAddress", {})
    sender_name = sender.get("name", "")
    sender_email = sender.get("address", "")

    # 解析收件人
    def parse_recipients(rcpts):
        return "; ".join([f"{r['emailAddress']['name']} <{r['emailAddress']['address']}>"
                          for r in rcpts]) if rcpts else ""

    to_list = parse_recipients(mail.get("toRecipients", []))
    cc_list = parse_recipients(mail.get("ccRecipients", []))

    # 时间
    received_at = mail["receivedDateTime"].replace("T", " ").replace("Z", "")

    # 正文
    body_plain = mail["body"].get("content", "") if mail["body"]["contentType"] == "text" else ""
    body_html = mail["body"].get("content", "") if mail["body"]["contentType"] == "html" else ""

    cursor.execute(sql, (
        mail["id"],
        mail.get("subject", ""),
        sender_name,
        sender_email,
        to_list,
        cc_list,
        received_at,
        body_plain[:65535],
        body_html[:65535],
        1 if mail.get("hasAttachments", False) else 0
    ))
    db_conn.commit()
    cursor.close()

# -------------------
# 4. 主循环
# -------------------
def main():
    db_conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        charset="utf8mb4"
    )
    last_check = datetime.utcnow() - timedelta(minutes=10)  # 初始拉10分钟内
    interval = int(os.getenv("CHECK_INTERVAL", 60))

    print("Outlook 自动入库服务启动...")
    while True:
        try:
            token = get_graph_token()
            mails = get_new_emails(token, last_check)
            if mails:
                print(f"发现 {len(mails)} 封新邮件")
                for m in mails:
                    insert_mail(db_conn, m)
            last_check = datetime.utcnow()
            time.sleep(interval)
        except Exception as e:
            print(f"错误: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()