#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Desc: 移车数量预测。
Author: Kris Peng
Copyright (c) 2019 - Kris Peng <kris.dacpc@gmail.com>
'''

# load and evaluate the finalized model on the validation dataset
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy

file_path = "/Users/chengpeng/Desktop/workspace/my_project/taicang_data/analysis/test.csv"

def main_task():
      
  # load and prepare datasets
  dataset = Series.from_csv(file_path)
  X = dataset.values.astype('float32')
  history = [x for x in X]
  validation = Series.from_csv(file_path)
  y = validation.values.astype('float32')
  # load model
  model_fit = ARIMAResults.load('car.pkl')
  # make first prediction
  predictions = list()
  yhat = float(model_fit.forecast()[0])
  predictions.append(yhat)
  history.append(y[0])
  print('>Predicted=%.3f, Expected=%3.f' % (yhat, y[0]))
  # rolling forecasts
  for i in range(1, len(y)):
  # predict
    model = ARIMA(history, order=(2,1,0))
    model_fit = model.fit(trend='nc', disp=0)
    yhat = float(model_fit.forecast()[0])
    predictions.append(yhat)
    # observation
    obs = y[i]
    history.append(obs)
    print('>Predicted=%.3f, Expected=%3.f' % (yhat, obs))
  # report performance
  rmse = sqrt(mean_squared_error(y, predictions))
  print('RMSE: %.3f'  % rmse)
  pyplot.plot(y)
  pyplot.plot(predictions, color='red')
  pyplot.show()
