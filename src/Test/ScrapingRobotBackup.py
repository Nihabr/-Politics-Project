'''
Created on Sep 21, 2016

@author: nihab
'''
import praw
import csv
import unicodedata
import datetime as dt

from Test import secrets

csvfilepath = 'C:/Users/nihab/AppData/Local/Programs/Python/PoliticsLim0.csv'



def run_bot(r):
    counter = 0
    subcounter = 0
    subreddit = r.get_subreddit("politics")
    submissions = subreddit.get_hot(limit = 0)
    columns = ['counter', 'comment body', 'date', 'karma']
    commentlist = [columns]      
    
    for submission in submissions:
        comments = submission.comments
        subcounter += 1
        print (subcounter)
        for comment in comments: 
            if (hasattr(comment,'body')):
                       
                counter += 1
                body = comment.body
                karma = comment.score
                time = comment.created
                time = dt.datetime.fromtimestamp(time)
                c = [counter, body, time, karma]
                commentlist.append(c)
        
    with open(csvfilepath,'w', newline='', encoding='utf8') as mf:
            wr = csv.writer(mf, delimiter=',')
            wr.writerows(commentlist)
            mf.close()                
      
def login():
    r = praw.Reddit(user_agent = secrets.APP_USER_AGENT)
    r.set_oauth_app_info(secrets.APP_ID, secrets.APP_SECRET, secrets.APP_URI)
    r.refresh_access_information(secrets.APP_REFRESH_TOKEN)
    return r    

r = login()
run_bot(r)    