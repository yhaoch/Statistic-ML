#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn import cross_validation

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features,labels,test_size = 0.3, random_state = 42)

count_poi = 0
for item in labels_test:
	if item == 1:
		count_poi += 1
print count_poi
print(len(labels_test))

all_zero = [] 

for i in range(0,len(labels_test)):
	all_zero.append(float(0))
print all_zero
print labels_test

clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)



pred = clf.predict(features_test)
print pred,len(pred)
print accuracy_score(all_zero,pred)
print precision_score(labels_test,pred), recall_score(labels_test, pred)

