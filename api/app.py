import sys

sys.path.append('..')

import json
import pandas as pd
from flask import Flask, request
from datetime import datetime
from jqdataclient import JQHelper

app = Flask(__name__)
helper = JQHelper()


@app.route('/')
def get_server_time():
    return str(datetime.now())


def get_params(req):
    """
    获取请求json
    :param req:
    :return:
    """
    data = req.get_data(as_text=True)
    params = {} if data is None or data.strip() == '' else json.loads(data)
    return params


def packet_result(params, func_name, json_file):
    """
    包装返回结果
    :param params:
    :param func_name:
    :param json_file:
    :return:
    """
    dct = json.loads(json_file)
    result = json.dumps({
        "params": params,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "func_name": func_name,
        "return_result": dct,
        "records_count": len(dct)
    })
    print(result)

    return result


@app.route('/get_all_securities', methods=['POST'])
def get_all_securities():
    params = get_params(request)
    df = helper.AssetBaseInfo.get_all_securities(**params)
    json_file = pd.DataFrame(df).to_json(orient='index', force_ascii=False)
    return packet_result(params, "get_all_securities", json_file)


@app.route('/get_trade_days', methods=['POST'])
def get_trade_days():
    params = get_params(request)
    df = helper.TradeMarketInfo.get_trade_days(**params)
    json_file = pd.DataFrame(df).to_json(orient='index', force_ascii=False)
    return packet_result(params, "get_trade_days", json_file)


@app.route('/get_all_trade_days', methods=['POST'])
def get_all_trade_days():
    params = get_params(request)
    df = helper.TradeMarketInfo.get_all_trade_days(**params)
    json_file = pd.DataFrame(df).to_json(orient='index', force_ascii=False)
    return packet_result(params, "get_all_trade_days", json_file)


@app.route('/get_price', methods=['POST'])
def get_price():
    params = get_params(request)
    df = helper.TradeMarketInfo.get_price(**params)
    json_file = pd.DataFrame(df).to_json(orient='index', force_ascii=False)
    return packet_result(params, "get_price", json_file)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
