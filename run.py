#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 11/05/2019

from db import case_db, category_db
from analysis import car_analysis, word_count

if __name__ == '__main__':

    # 数据入库
    category_db.main_task()