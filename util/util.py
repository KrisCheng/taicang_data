#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

import os, fnmatch
from config.config import *
from model.job_relation import JobRelation
from model.job_requirement import JobRequirement


# file util


def mkdirs_if_not_exists(directory_):
    """
    create a new folder if it does not exist
    """
    if not os.path.exists(directory_) or not os.path.isdir(directory_):
        os.makedirs(directory_)

def file_list_end_with(file_end, base_file_path = DATA_BASE_PATH):
    return fnmatch.filter(os.listdir(base_file_path), "*" + file_end)

# db util

def fetch_all_case(session):
    return session.query(JobRelation) \
    .all()
