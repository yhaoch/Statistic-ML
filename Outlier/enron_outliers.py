#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
#print data_dict.keys()
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)


### your code below
# for item in data:
# 	if item[0] > 20000000:
# 		print item

for item in data_dict:
	print 
	if data_dict[item]["salary"] > 1000000 and data_dict[item]["bonus"] >= 5000000 and data_dict[item]["salary"] != "NaN" and data_dict[item]["bonus"] != "NaN":
		print item

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
