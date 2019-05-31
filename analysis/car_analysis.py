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

from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression

def main_task():
    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    all_car = session.execute("select case_id from case_info where title like '%移车%'")
    session.close()
    list = []
    for car in all_car:
        try:
            list.append(int(car["case_id"][0:8]))
        except:
            pass
    dict = {}
    for item in list:
        if item in dict.keys():
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    x = []
    y = []
    fin_dict = {}
    for key,value in dict.items():
        if value > 10:
            fin_dict[key] = value
    for key in sorted(fin_dict.keys()):
        print(str(datetime.strptime(str(key), '%Y%m%d')) + " : " + str(dict[key]))
        x.append(key)
        y.append(dict[key])
    
    series = Series(y)
    print(series.describe())
    X = [i for i in range(0, len(series))]
    X = np.reshape(X, (len(X), 1))
    model = LinearRegression()
    model.fit(X, y)
    # calculate trend
    trend = model.predict(X)
    # plot trend
    plt.plot(y)
    plt.plot(trend)
    plt.show()
    # detrend
    detrended = [y[i]-trend[i] for i in range(0, len(series))]
    # plot detrended
    plt.plot(detrended)
    plt.show()

    # result = seasonal_decompose(series, model='dditive', freq=1)
    # result.plot()
    # plt.show()

    # plt.figure(figsize=(16, 8))
    # plt.figure(1)
    # plt.subplot(211)
    # series.hist()
    # plt.subplot(212)
    # series.plot(kind='kde')
    # plt.show()

    # series.hist()
    # groups = series.groupby(TimeGrouper('A'))
    # years = DataFrame()
    # for name, group in groups:
    #     years[name.year] = group.values
    # years.boxplot()
    # pyplot.show()
    # # plt.figure(figsize=(16, 8))
    # # plt.title("Trend of Moving Car")
    # # plt.plot(x, y, color='blue', linewidth=1.0)
    # plt.show()