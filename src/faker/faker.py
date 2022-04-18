from faker import Faker
import pandas as pd

fake = Faker(["zh_CN"])
Faker.seed(0)

def get_data():
    key_list = ["姓名","详细地址","所在省份","手机号","身份证号","出生年月","邮箱"]
    name = fake.name()
    address = fake.address()
    province = address[:3]
    number = fake.phone_number()
    id_card = fake.ssn()
    birth_date = id_card[6:14]
    email = fake.email()
    info_list = [name,address,province,number,id_card,birth_date,email]
    person_info = dict(zip(key_list,info_list))
    return person_info


df = pd.DataFrame(columns=["姓名","详细地址","所在省份","手机号","身份证号","出生年月","邮箱"])
for i in range(10000):
    person_info = [get_data()]
    df1 = pd.DataFrame(person_info)
    df = pd.concat([df,df1])
df.to_excel("模拟数据.xlsx",index=None)