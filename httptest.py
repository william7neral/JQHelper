#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
                             _ooOoo_
                            o8888888o
                            88" . "88
                            (| -_- |)
                             O\ = /O
                         ____/`---'\____
                        .   ' \\| |// `.
                        / \\||| : |||// \
                      / _||||| -:- |||||- \
                        | | \\\ - /// | |
                      | \_| ''\---/'' | |
                       \ .-\__ `-` ___/-. /
                    ___`. .' /--.--\ `. . __
                 ."" '< `.___\_<|>_/___.' >'"".
                | | : `- \`.;`\ _ /`;.`/ - ` : | |
                  \ \ `-. \_ __\ /__ _/ .-` / /
          ======`-.____`-.___\_____/___.-`____.-'======
                             `=---='

          .............................................
                    佛祖保佑             永无BUG
//=============================================
@version: 1.0
@author: louhong 
@file: test
@time: 2018/11/5 16:52
"""
if __name__ == '__main__':
    import requests

    # post_data = {
    #     "types": ["etf"],
    # }
    # res = requests.post(url="http://127.0.0.1:5000/get_all_securities", data=post_data)
    post_data = {
        "start_date": "2018-11-7",
    }
    res = requests.post(url="http://127.0.0.1:5000/get_trade_days",json=post_data)
    print(res.text)
