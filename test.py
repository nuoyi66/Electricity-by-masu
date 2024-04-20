import requests
import json
from datetime import datetime
time=datetime.now()
with open('config.json', 'r') as f:
    config_data = json.load(f)
token = config_data['token']
try :
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMzIwNDAyNyIsImFjY051bSI6IjI1MzA4IiwicGVyQ29kZSI6IjIzMjA0MDI3IiwiZXhwIjoxNzE2MTg5MzAxLCJpYXQiOjE3MTM1OTczMDEsImp0aSI6IjlmMTM5NzBmLTQwMTQtNGMyMi05MzQzLTkwMzIwZDM2MTFmMyJ9._rJRi7-9uFHU9Q-fit3vGlq3GNQNH6rxasIL9LIWgAE',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://ykt.masu.edu.cn:8081',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://ykt.masu.edu.cn:8081/easytong_webapp/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'h5Req': 'Y',
    }

    data = {
        'AccNum': config_data['AccNum'],
        'AreaNo': config_data['AreaNo'],
        'BuildingNo': config_data['BuildingNo'],
        'FloorNo': config_data['FloorNo'],
        'ItemNum': config_data['ItemNum'],
        'RoomNo': config_data['RoomNo'],
        'Time': '20240420151540',
        'Sign': '7175f1b5bfce9e2a804286e3fe2e7649',
        'ContentType': 'application/json',
    }

    response = requests.post(
        'http://ykt.masu.edu.cn:8081/easytong_app/GetPayAccInfoNew',
        headers=headers,
        data=data,
        verify=False,
    )
    data=response.text
    data_dict=json.loads(data)
    balance_value = float(data_dict["balance"])
    if (balance_value < 10):
        title = str(time.date()) + '电量低:' + str(balance_value)
        url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title +'&channel=mail' + '&content=' + str(
        time.date()) + '\n当前剩余电量：' + str(balance_value) + '度'
        requests.get(url)
    else:
        print(balance_value)
except Exception:
    url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title +'&channel=mail' + '&content=' + str(
    time.date()) + '\n查询失败'
    requests.get(url)