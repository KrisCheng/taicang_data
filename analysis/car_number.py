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
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
import re

from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression

car_number_reg = r"([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}(([0-9]{5}[DF])|([DF]([A-HJ-NP-Z0-9])[0-9]{4})))|([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]{1})"

def main_task():
    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    all_car = session.execute("select content from case_info where title like '%移车%'")
    session.close()
    list = []
    dict = {}
    car_count = 0
    for car in all_car:
        try:
            car_number = re.search(car_number_reg, car.content, re.M|re.I).group()
            car_count = car_count + 1
            if(car_number in dict.keys()):
                dict[car_number] = dict[car_number] + 1
            else:
                dict[car_number] = 1
        except:
            pass
    list = sorted(dict.items(), key = lambda item:item[1], reverse = True)
    print("所有车辆的数目 : " + str(car_count))
    count_20 = 0
    count_10 = 0
    count_5 = 0
    for item in list:
      if(item[1] >= 10):
            count_10 = count_10 + 1
      if(item[1] >= 5):
            count_5 = count_5 + 1        
      if(item[1] >= 20):
            count_20 = count_20 + 1  
                 
    print(">=5 车辆的数目 : " + str(count_5))
    print(">=10 车辆的数目 : " + str(count_10))
    print(">=20 车辆的数目 : " + str(count_20))