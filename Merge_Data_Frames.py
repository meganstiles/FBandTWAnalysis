
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
def merge_fb_files(file1,file2,file3):
    
    #Drop top line (contains information we don't need)
    file1_clean = file1.drop([0])
    
    #Convert files to numeric   
    file1_clean_2 = file1_clean.convert_objects(convert_numeric=True)
    file2_clean = file2.convert_objects(convert_numeric=True)
    file3_clean = file3.convert_objects(convert_numeric=True)

    #Subset files with columns I need
    Total = file1_clean2[[0,1,2,3, 6, 9]]
    file2_clean_2 = file2_clean[[1,9,10,11]]
    file3_clean_2 = file3_clean[[1,9]]

    #Concatinate columns into One Data Frame
    Data = pd.concat([Total, file3_clean_2,file2_clean_2], axis =1, join= 'inner')
    Data = Data[[1,2,3,4,5,7,9,10,11]]

    #Write out CSV
    Data.to_csv('12-18Total.csv')

#Twitter = pd.read_csv('tweet_activity_metrics_asdmra_20161212_20161219_en.csv')    
def merge_Twitter_files(file):

    #Subset Data Frame

    Twitter_new = file[[1,2,4,7,8,9,11]]
    
    #Write out to csv
    Twitter_new.to_csv('Tweets.csv')

