#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Desc: 词频统计。
Author: Kris Peng
Copyright (c) 2019 - Kris Peng <kris.dacpc@gmail.com>
'''

import os
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from config.config import *
from util.util import *

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def main_task():
    job_info = ""
    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    all_job_relation = fetch_all_jobrelation(session=session)

    for job_relation in all_job_relation:
        job_info = job_info + " " + str(job_relation.job_name).strip()
    # print(job_info)

    session.close()

    # Generate a word cloud image
    wordcloud = WordCloud(
                font_path='/Users/chengpeng/Desktop/workspace/my_project/InternetSurvivalSpider/spider/no_scrapy/analysis/SourceHanSerifK-Light.otf',
                repeat=False,
                width=400,
                height=200,
                background_color='black',
                scale=15,
                ).generate(job_info)

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()