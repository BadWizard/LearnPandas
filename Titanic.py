# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:16:27 2015
loading and manipulating Titanic data from Kaggle
https://www.kaggle.com/c/titanic/details/getting-started-with-python
@author: BadWizard
"""

import os
os.getcwd()
os.chdir('/Users/BadWizard/Documents/Python/codes/Learn/LearnPandas')

import csv as csv 
import numpy as np

# using the methond in Python Cookbook
data=[] 
with open('data/train.csv') as f:
    f_csv = csv.reader(f) 
    headers = next(f_csv) 
    for row in f_csv:
        data.append(row)    
data = np.array(data) 	


number_passengers = np.size(data[:,1].astype(np.float))

number_survived = np.sum(data[:,1].astype(np.float))

proportion_survivors = number_survived/number_passengers

print(str(100*proportion_survivors), ' per cent of the passengers survived')

number_female = np.size(data[data[:,4]=='female',1])
number_female_survived = np.sum(data[data[:,4]=='female',1].astype(np.float))
proportion_female_survivors = number_female_survived/number_female


number_male = np.size(data[data[:,4]=='male',1])
number_male_survived = np.sum(data[data[:,4]=='male',1].astype(np.float))
proportion_male_survivors = number_male_survived/number_male

print('per cent of female survived is  %.2f' % float(proportion_female_survivors*100))
print('per cent of male survived is  %.2f' % float(proportion_male_survivors*100))

testdata = []
with open('data/test.csv') as f:
    test_file_object = csv.reader(f) 
    header = next(test_file_object)
    for row in test_file_object:
        testdata.append(row)    
testdata = np.array(testdata) 	

    
with open('genderbasedmodel.csv','w') as prediction_file:
    prediction_file_object = csv.writer(prediction_file)
    prediction_file_object.writerows(["PassengerId", "Survived"])
    for row in testdata:
        if row[3] == 'female':
            prediction_file_object.writerow([row[0],'1'])    # predict 1
        else:
            prediction_file_object.writerow([row[0],'0'])    # predict 1
            
            
            
                

                    
    
    


            
            
        
