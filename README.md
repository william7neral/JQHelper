# JQHelper
聚宽数据请求功能模块，将请求方式转化为HTTP

## 启动
运行api/app.py中的main函数，启动服务

## 启动成功验证
打开浏览器，输出http://127.0.0.1:5000，若出现时间，则表示服务启动成功

## 请求示例
```
import requests

post_data = {
        "start_date": "2018-11-7",
    }
res = requests.post(url="http://127.0.0.1:5000/get_trade_days",json=post_data)
print(res.text)
```

---
输出结果：

```
{
	"params": {
		"start_date": "2018-11-7"
	},
	"time": "2018-11-12 10:28:21",
	"func_name": "get_trade_days",
	"return_result": {
		"0": {
			"0": 1541548800000
		},
		"1": {
			"0": 1541635200000
		},
		"2": {
			"0": 1541721600000
		},
		"3": {
			"0": 1541980800000
		}
	},
	"records_count": 4
}
```
