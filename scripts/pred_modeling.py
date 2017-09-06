# -*- coding: utf-8 -*-
"""
Tony Silva
Predicitive Modeling
"""
import pandas as pd
from  sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("C:/Users/Anthony Silva/silvat/ccc/data/df.csv", sep=",", index_col=0)
df = df.sort_values(by=["timestamp"], ascending=[True])

preds = list(df.columns.values)
remove = ['segment', 'date', 'start_time', 'calling_party', 'dialed_number'
              ,'ans_logid', 'talk_time', 'hold_time', 'acw_time',
              'trans_out', 'conf', 'work_code', 'target']
for i in remove:
    preds.remove(i)
target = "target"

# Create Sampling off of the time stamp variable.