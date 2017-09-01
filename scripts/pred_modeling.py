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

preds = list(df.columns.values)
remove = ['segment', 'date', 'start_time', 'calling_party', 'dialed_number'
              ,'ans_logid', 'talk_time', 'hold_time', 'acw_time',
              'trans_out', 'conf', 'work_code', 'target']
for i in remove:
    preds.remove(i)
target = "target"


train, test = train_test_split(df, test_size=.3)
train_x = train[preds]
train_y = train[target]

test_x = test[preds]
test_y = test[target]

model = LogisticRegression()
model.fit(train_x, train_y)
predictions = model.predict(test_x)

print(classification_report(test_y, predictions))
print(confusion_matrix(test_y, predictions))