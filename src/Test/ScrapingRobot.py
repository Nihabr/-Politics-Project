'''
Created on Sep 21, 2016

@author: nihab
'''
import praw
import csv
import unicodedata
import time as tm
import datetime as dt

from Test import secrets

csvfilepath = 'PoliticsLim0.csv'

'''praw.helpers.submissions_between(reddit_session,
             subreddit, lowest_timestamp=None, highest_timestamp=None, newest_first=True, 
             extra_cloudsearch_fields=None, verbosity=1)'''

def run_bot(r):
    counter = 0
    subcounter = 0
    subreddit = r.get_subreddit("politics")
    lts = dt.date(2015, 7, 1)
    lts = tm.mktime(lts.timetuple())
    hts = dt.date(2016, 11, 7)
    hts = tm.mktime(hts.timetuple())
    
    '''submissions = subreddit.get_hot(limit = 0)'''
    submissions = praw.helpers.submissions_between(r, subreddit, lowest_timestamp=lts, highest_timestamp=hts, newest_first=True)
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