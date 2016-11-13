'''
Created on Nov 13, 2016

@author: nihab
'''

import csv

pydir = 'C:/Users/nihab/AppData/Local/Programs/Python/'
filename = 'csvfile2.csv'
newfilename = 'SciptTest.csv'



def somefunction():
    
    with open (pydir+filename, 'r', encoding='utf8') as csvfile:
            comments = csv.reader(csvfile, delimiter = ',')
            
            trumpCounter = 0
            hillaryCounter = 0
            
            for idx, comment in enumerate(comments):
                if (idx != 0):
                    body = comment[1].lower()
                    
                    trumpCounter += body.count('donald')
                    trumpCounter += body.count('trump')
                    
                    hillaryCounter += body.count('hillary')
                    hillaryCounter += body.count('clinton')
            csvfile.close()
            print(trumpCounter)
            print(hillaryCounter)
            
somefunction()
            
            