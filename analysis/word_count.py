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
    category_info = ""
    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print("query start...")
    all_item = session.execute("select cc.category from case_category as cc, case_info as ci where cc.categorycode = ci.ctype limit 0,10000")
    print("query end...")
    for item in all_item:
        category_info = category_info + " " + str(item.category).strip()
    session.close()
    # print(category_info)

    # Generate a word cloud image
    wordcloud = WordCloud(
                font_path='/Users/chengpeng/Desktop/workspace/my_project/taicang_data/analysis/SourceHanSerifK-Light.otf',
                width=2000,
                height=1000,
                max_words=40,
                collocations=False,
                background_color='white',
                ).generate(category_info)

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()