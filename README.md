# JQHelper
聚宽数据请求功能模块，将请求方式转化为HTTP
'''
import requests

post_data = {
        "start_date": "2018-11-7",
    }
res = requests.post(url="http://127.0.0.1:5000/get_trade_days",json=post_data)
print(res.text)
'''
