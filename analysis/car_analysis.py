#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Desc: 移车数量统计。
Author: Kris Peng
Copyright (c) 2019 - Kris Peng <kris.dacpc@gmail.com>
'''
from openpyxl import load_workbook
from pandas import DataFrame
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import *

def main_task():
    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    all_car = session.execute("select case_id from case_info where title like '%移车%'")
    list = []
    for car in all_car:
        list.append(car["case_id"][0:6])
    dict = {}
    for item in list:
        if item.isdigit():
            if item in dict.keys():
                dict[item] = dict[item] + 1
            else:
                dict[item] = 1
    for key,value in dict.items():
        if value > 10:
            print(str(key) + ' : ' + str(value))
    session.close()