#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng

import os, fnmatch
from config.config import *
from model.case import Case
from model.casecategory import CaseCategory

# file util

def mkdirs_if_not_exists(directory_):
    """
    create a new folder if it does not exist
    """
    if not os.path.exists(directory_) or not os.path.isdir(directory_):
        os.makedirs(directory_)

# db util

def fetch_all_case(session):
    return session.query(Case) \
    .all()
