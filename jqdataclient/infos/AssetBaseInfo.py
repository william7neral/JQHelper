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
@file: AssetBaseInfo
@time: 2018/11/5 11:23
"""

from jqdatasdk import *


class AssetBaseInfo:
    """
    获取标的基础信息
    """

    def get_all_securities(self, types=[], date=None):
        """
        获取平台支持的所有股票、基金、指数、期货信息

        :param types list: 用来过滤securities的类型, list元素可选: ‘stock’, ‘fund’, ‘index’, ‘futures’, ‘etf’, ‘lof’, ‘fja’, ‘fjb’. types为空时返回所有股票, 不包括基金,指数和期货
        :param date 日期, 一个字符串或者 datetime.datetime/datetime.date 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
        :return pandas.DataFrame
        """
        try:
            return get_all_securities(types=types, date=date)
        except Exception as e:
            print(e)
            return None
