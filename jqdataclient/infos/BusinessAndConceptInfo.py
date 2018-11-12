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
@file: BusinessAndConceptInfo
@time: 2018/11/5 11:28
"""

from jqdatasdk import *


class BusinessAndConceptInfo:
    """
    行业概念信息
    """

    def get_industries(self, name='zjw'):
        try:
            return get_industries(name=name)
        except Exception as e:
            print(e)
            return None
