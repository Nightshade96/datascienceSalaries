# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:29:15 2022

@author: Night
"""

import glassdoor_scapper as gs
import pandas as pd
import os

path =  "C:/Users/Night/OneDrive/Personal/PersonalProjects/datascienceSalaries/chromedriver.exe"

#os.getcwd()
df =  gs.get_jobs('data scientist', 2, False, path, 15)     


   