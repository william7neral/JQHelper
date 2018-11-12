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
@file: JQHelper
@time: 2018/11/5 13:38
"""

from jqdatasdk import *

import jqdataclient.infos as client


class JQHelper:
    AssetBaseInfo = None
    TradeMarketInfo = None
    BusinessAndConceptInfo = None

    def __init__(self):
        auth('18867105560', '5ff@0u7f')
        self.AssetBaseInfo = client.AssetBaseInfo()
        self.TradeMarketInfo = client.TradeMarketInfo()
        self.BusinessAndConceptInfo = client.BusinessAndConceptInfo()

    @staticmethod
    def normalize_code(code):
        return normalize_code(code)


if __name__ == '__main__':
    helper = JQHelper()
    result = helper.TradeMarketInfo.get_price('000001.XSHE', end_date='2018-11-5 13:29:00', count=1, frequency='1m',
                                              fq=None)
    print(result)
