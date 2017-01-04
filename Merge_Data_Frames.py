
#os.chdir('/Users/meganstiles/Desktop/Bowen/December 2016/')

#Posts = pd.read_csv('12-18 Metrics.csv',encoding= 'latin-1')
#Engagement = pd.read_csv('12-18 Engagements.csv', encoding= 'latin-1')
#Links = pd.read_csv('12-18 Links.csv', encoding= 'latin-1')
import re
import os
import pandas as pd
import numpy as np
from string import punctuation
from collections import Counter

def merge_fb_files(Posts,Engagements,Links):
    
    #Drop top line (contains information we don't need)
    Posts_clean = Posts.drop([0])
    
    #Convert files to numeric   
    Posts_clean_2 = Posts_clean.convert_objects(convert_numeric=True)
    Engagements_clean = Engagements.convert_objects(convert_numeric=True)
    Links_clean = Links.convert_objects(convert_numeric=True)

    #Subset files with columns I need
    Total = Posts_clean_2[['Post ID', 'Permalink', 'Post Message', 'Lifetime Post organic reach']]
    Engagements_clean_2 = Engagements_clean[['Post ID', 'comment', 'like', 'share']]
    Links_clean_2 = Links_clean[['Post ID','link clicks']]

    #Concatinate columns into One Data Frame
    Data = pd.merge(left = Total,right=Links_clean_2, left_on= 'Post ID', right_on= 'Post ID')
    Data_Final = pd.merge(left = Data, right = Engagements_clean_2, left_on= 'Post ID', right_on= 'Post ID')
  
    #Write out CSV
    Data_Final.to_csv('FB_Clean.csv')

#Twitter = pd.read_csv('tweet_activity_metrics_asdmra_20161212_20161219_en.csv')    
def merge_Twitter_files(file):

    #Subset Data Frame

    Twitter_new = file[[1,2,4,7,8,9,11]]
    
    #Write out to csv
    Twitter_new.to_csv('Tweets_clean.csv')

