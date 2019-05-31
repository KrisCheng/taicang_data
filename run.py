#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 11/05/2019

from db import case_db, category_db
from analysis import car_analysis, word_count, car_pred, car_result

if __name__ == '__main__':

    # 数据入库
    # category_db.main_task()

    # 数据分析
    # word_count.main_task()
    # car_analysis.main_task()
    # car_pred.main_task()
    car_result.main_task()