# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

DataSet = pd.read_csv('train_data.csv')
train_rows=len(DataSet)
train_cols=len(DataSet.columns)
X_train = DataSet.ix[:,2:train_cols-1]
Y_train = DataSet.ix[:,train_cols-1]
#clf = svm.SVC()
#clf.fit(training_train_set, training_target_set)

X_new = SelectKBest(chi2, k=10).fit(X_train,Y_train)
X_new = X_new.get_support()
X_new=X_new.tolist()
X_new_index = [i for i, x in enumerate(X_new) if x == True]
top_10_features = X_train.columns.values[X_new_index].tolist()

resultFile = open("top_10_features.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
for item in top_10_features:
    wr.writerow([item,])
    #print item