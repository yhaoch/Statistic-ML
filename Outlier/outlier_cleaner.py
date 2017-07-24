#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    lst = []
    lst1 = []
    temp = []
    for i in range(0,len(predictions)):
        lst.append(math.pow(predictions[i][0] - net_worths[i][0],2))
    temp = sorted(lst,reverse = True)
    for i in range(0,9):
        lst1.append(temp[i])
    #print len(lst1)
    # for item in lst1:
    #     print item

    for i in range(0,len(predictions)):
        if math.pow(predictions[i][0] - net_worths[i][0],2) in lst1:
            continue
        else:
            tup1 = (ages[i][0],net_worths[i][0],math.pow(predictions[i][0] - net_worths[i][0],2))
            cleaned_data.append(tup1)
    # for item in cleaned_data:
    #     print item
    return cleaned_data

