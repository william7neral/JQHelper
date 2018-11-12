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
@file: TradeMarketInfo
@time: 2018/11/5 11:24
"""

from jqdatasdk import *


class TradeMarketInfo:
    """
    交易行情信息
    """

    def get_trade_days(self, start_date=None, end_date=None, count=None):
        """
        获取指定日期范围内的所有交易日

        :return numpy.ndarray, 包含指定的 start_date 和 end_date, 默认返回至 datatime.date.today() 的所有交易日
        """
        try:
            return get_trade_days(start_date=start_date, end_date=end_date, count=count)
        except Exception as e:
            print(e)
            return None

    def get_all_trade_days(self):
        """
        获取所有交易日

        :return 包含所有交易日的 numpy.ndarray, 每个元素为一个 datetime.date 类型.
        """
        try:
            return get_all_trade_days()
        except Exception as e:
            print(e)
            return None

    def get_price(self, security, start_date=None, end_date=None, frequency='daily', fields=None, skip_paused=False,
                  fq='pre', count=None):
        """
        获取一支或者多只证券的行情数据

        :param security 一支证券代码或者一个证券代码的list
        :param count 与 start_date 二选一，不可同时使用.数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据
        :param start_date 与 count 二选一，不可同时使用. 字符串或者 datetime.datetime/datetime.date 对象, 开始时间
        :param end_date 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期.
        :param frequency 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟
        :param fields 字符串list, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持以下属性 ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']
        :param skip_paused 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充, 上市前或者退市后数据都为 nan
        :return 如果是一支证券, 则返回pandas.DataFrame对象, 行索引是datetime.datetime对象, 列索引是行情字段名字; 如果是多支证券, 则返回pandas.Panel对象, 里面是很多pandas.DataFrame对象, 索引是行情字段(open/close/…), 每个pandas.DataFrame的行索引是datetime.datetime对象, 列索引是证券代号.
        """
        try:
            return get_price(security=security, start_date=start_date, end_date=end_date, frequency=frequency,
                             fields=fields, skip_paused=skip_paused, fq=fq, count=count)
        except Exception as e:
            print(e)
            return None
