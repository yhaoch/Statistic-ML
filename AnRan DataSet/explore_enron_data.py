#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#how many people
count_people = 0
for item in enron_data:
	count_people += 1
print(count_people)

#how many features for each people
# count = 0
# for item in enron_data:
# 	print(len(enron_data[item]))
#print(count)

#POIs
num_pois = 0;
for item in enron_data:
	if enron_data[item]["poi"] == 1:
		num_pois += 1
print(num_pois) 

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

# Wesley Colwell 
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#Jeffrey K Skilling
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print(enron_data["COLWELL WESLEY"])
#Most money
max_money = 0
people = {"SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"}
name = ""
for item in people:
	print(enron_data[item]["total_payments"])
	if enron_data[item]["total_payments"] != "":
		max_money = max(max_money, enron_data[item]["total_payments"])

#quantified salary
num_quantify = 0
num_email = 0
for item in enron_data:
	if enron_data[item]["salary"] != 'NaN':
		num_quantify += 1
	if enron_data[item]["email_address"] != 'NaN':
		num_email += 1
print(num_quantify)
print(num_email)

#
count_NaN = 0.0
for item in enron_data:
	if enron_data[item]["total_payments"] == 'NaN':
		count_NaN += 1
print(count_NaN)
print(count_NaN / count_people)

#poi
count_poi = 0.0
for item in enron_data:
	if enron_data[item]["poi"] == True:
		count_poi += 1
print(count_poi )

