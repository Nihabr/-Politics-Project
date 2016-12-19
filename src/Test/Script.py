'''
Created on Nov 10, 2016

@author: nihab
'''

import csv
from operator import itemgetter


pydir = 'C:/Users/nihab/AppData/Local/Programs/Python/'
filename = 'DatasetV1.csv'
commentlist = []
newfilename = 'DatasetV1Sorted.csv'

def somefunction():
    with open (pydir+filename, 'r', encoding='utf8') as csvfile:
            comments = csv.reader(csvfile, delimiter = ',')
            counter = 0
            
            for idx, comment in enumerate(comments):
                if (idx != 0):
                    counter += 1
                    body = comment[1]
                    karma = comment[3]
                    time = comment[2]
                    c = [counter, body, time, karma]
                    commentlist.append(c)
            
            csvfile.close()                
            sc = sorted(commentlist, key=itemgetter(2))
            
            
            

    with open (pydir+newfilename, 'w', encoding='utf8', newline='') as mf:
            wr = csv.writer(mf, delimiter=',')
            wr.writerows(sc)
            mf.close()

somefunction()