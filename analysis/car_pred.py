#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Desc: 移车数量预测。
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
from matplotlib import pyplot
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression
from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from pandas import Series
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from math import sqrt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot
import numpy

file_path = "/Users/chengpeng/Desktop/workspace/my_project/taicang_data/analysis/train.csv"

# monkey patch around bug in ARIMA class
def __getnewargs__(self):
  return ((self.endog),(self.k_lags, self.k_diff, self.k_ma))

ARIMA.__getnewargs__ = __getnewargs__

def main_task():
    # load data
    series = Series.from_csv(file_path)
    # prepare data
    X = series.values
    X = X.astype('float32')
    # fit model
    model = ARIMA(X, order=(2,1,0))
    model_fit = model.fit(trend='nc', disp=0)
    # bias constant, could be calculated from in-sample mean residual
    bias = 0
    # save model
    model_fit.save('car.pkl')
