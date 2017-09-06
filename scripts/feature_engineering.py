# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:37:26 2017

@author: Anthony Silva
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Anthony Silva/silvat/ccc/data/total.csv", sep=",", index_col=0)
# Need to change calling numbers to objects without scientific notation.


#Data Preprocessing

# Set up Target Variable
df = df.loc[(df.disposition == "ANS") | (df.disposition == "ABAN"), :]
df["target"] = 0
df.loc[df.disposition == "ABAN", "target"] = 1
df = df.drop("disposition", axis=1)
df["date"] = pd.to_datetime(df["date"])

# Feature Extraction

# Time Period Features
df["call_time_period"] = df["start_time"].str[-2:]
time_period = pd.get_dummies(df["call_time_period"])
df = pd.concat([df,time_period], axis=1)
del df["call_time_period"]

# More Time Features
df["hour"] = df["start_time"].str.extract('(\d\d?)',expand=True)
hour = pd.get_dummies(df["hour"])
df = pd.concat([df, hour], axis=1)
del df["hour"]

#Interaction between Morning and Hour
keep = ["6AM", "7AM" ,"8AM", "9AM", "10AM","11AM", "12PM", "1PM", "2PM", "3PM","4PM"
,"5PM", "6PM", "7PM", "8PM"]
for i in hour.columns:
    name = i+"AM"
    if name in keep:
        df[name] = df["AM"]*df[i]
    name = i+"PM"
    if name in keep:
        df[name] = df["PM"]*df[i]
del i
del name

# Month Features
df["month"] = df["date"].dt.month
month = pd.get_dummies(df["month"])
month.columns = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep",
                 "oct", "nov", "dec"]
df = pd.concat([df, month], axis=1)
del df["month"]

# Day of Week Features
df["weekday"] = df["date"].dt.dayofweek
weekday = pd.get_dummies(df["weekday"])
weekday.columns = ["monday", "tuesday","wednesday","thursday","friday"
                ,"saturday", "sunday"]
df = pd.concat([df, weekday], axis=1)
del df["weekday"]

# Area Code Features
df["call_area_code"] = df["calling_party"].str[:3]
call_area_code = pd.get_dummies(df["call_area_code"])
df = pd.concat([df, call_area_code], axis=1)
del df["call_area_code"]

# Schedule Features
# Number of Employees scheduled to work at a given hour
df["num_workers"] = 2*df["6AM"] + 3*df["7AM"] + 4*df["8AM"] + 4*df["9AM"] + 5*df["10AM"] + 5*df["11AM"] + 6*df["12PM"] + 6*df["1PM"] + 6*df["2PM"] + 4*df["3PM"] + 2*df["4PM"] + 1*df["5PM"] + 1*df["6PM"] + 1*df["7PM"] + 1*df["8PM"]

# Call gets Queued
df["queued"]  = 0
df.loc[df.disposition_time > 10,"queued"] = 1

# Time Stamp
# Create a timestamp field for each obersvation
date_stamp = []
for a in zip(df["date"].dt.year.tolist(),df["date"].dt.month.tolist(),df["date"].dt.day.tolist()):
    if a[1] < 10:
        if a[2] < 10:
            date_stamp.append(str(a[0]) + "0" + str(a[1]) + "0" + str(a[2]))
        else:
            date_stamp.append(str(a[0]) + "0" + str(a[1]) + str(a[2]))            
    else:
        if a[2] < 10:
            date_stamp.append(str(a[0]) + str(a[1]) + "0" + str(a[2]))
        else:
            date_stamp.append(str(a[0]) + str(a[1]) + str(a[2]))

time_stamp = []
for a in zip(df["start_time"].str[:2],df["start_time"].str[-4:-2]):
    if ":" in a[0]:
        time_stamp.append("0" + str(a[0][0]) + str(a[1]))
    else:
        time_stamp.append(str(a[0]) + str(a[1]))

time_of_day = df["start_time"].str[-2:]
clock_stamp = []
for a in zip(time_stamp, time_of_day):
    if a[1] == 'AM':
        if a[0][:2] == "12":
            
            clock_stamp.append(str(int(a[0]) + 1200))
        else:
            clock_stamp.append(a[0])
    else:
        if int(a[0]) < 1000:
            clock_stamp.append(str(int(a[0]) + 1200))
        else:
            clock_stamp.append(a[0])

time_stamp = [int(m+n) for m,n in zip(date_stamp, clock_stamp)]
time_stamp = np.array(time_stamp)
df["timestamp"] = time_stamp

del time_period, time_stamp, keep, time_of_day, clock_stamp
del month
del weekday
del call_area_code
del hour
del date_stamp
del a

df = df.fillna(0)

df.to_csv("C:/Users/Anthony Silva/silvat/ccc/data/df.csv", sep=",")
