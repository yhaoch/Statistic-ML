#!/usr/bin/python
#haochuan yang edited 24 July
"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

#####
features_list_1 = ["bonus", "long_term_incentive"]
data_1 = featureFormat( dictionary, features_list_1, remove_any_zeroes=True)
target_1, features_1 = targetFeatureSplit( data_1 )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
feature_train_1, feature_test_1, target_train_1, target_test_1 = train_test_split(features_1, target_1, test_size=0.5, random_state=42)
#color
train_color = "b"
test_color = "r"

### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
reg = LinearRegression()
regr = LinearRegression()
reg.fit(feature_train,target_train)
regr.fit(feature_train_1,target_train_1)
#print reg.coef_[0], reg.intercept_
#print reg.score(feature_train,target_train)
print reg.score(feature_test,target_test)
print regr.score(feature_test_1,target_test_1)



#print accuracy_score(target_test,pred)
#print reg.score(target_test,pred)

### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass

reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="y")
print reg.coef_

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
