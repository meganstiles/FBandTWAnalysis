import re
import os
import pandas as pd
import numpy as np
from string import punctuation
from collections import Counter

def get_analysis(file1,file2,file3):
    #Read in File 1 
    file1 = file1.drop([0])
    file1 = file1.convert_objects(convert_numeric=True)

    #Read in File 2
    file2 = file2.convert_objects(convert_numeric=True)

    #Read in File 3
    file3 = file3.convert_objects(convert_numeric=True)

    #Reach
    reach = file1['Lifetime Post organic reach'].sum()
    print("The total organic reach was {0}".format(reach))

    #Likes
    Likes = file2['like'].sum()
    print("The total number of likes was {0}".format(Likes))

    #Comments
    Comments = file2['comment'].sum()
    print('Comments:')
    print(Comments)

    #shares
    Shares = file2['share'].sum()
    print('Shares:')
    print(Shares)

    #Links
    Links = file3['link clicks'].sum()
    print('Links:')
    print(Links)
    
    hashtags = []
    for text in range(1,len(file1)):
        post = file1['Post Message'][text]
        post = re.sub("[:!.,]", '', post)
        hashes = re.findall('#\S*', post)
        for tag in hashes:
            hashtags.append(tag)
    unique_hashtags =np.unique(hashtags)
    unique_hashtags = sorted(unique_hashtags, key= str.lower)
    print('The hashtags used were ' + str(unique_hashtags))
    print('The count of hashtags was:')
    print(Counter(hashtags))
    str1 = ''.join(str(e) for e in unique_hashtags)
    print(str1)
    

#Twitter


def get_Tweets(file1):
    #Read in File 1 
    file1 = file1.convert_objects(convert_numeric=True)

    #Reach
    reach = file1['impressions'].sum()
    print(reach)
    print("The total organic reach was {0}".format(reach))

    #Likes
    Likes = file1['likes'].sum()
    print(Likes)
    print("The total number of likes was {0}".format(Likes))

    #Replies
    Replies = file1['replies'].sum()
    print('Replies:')
    print(Replies)

    #Retweest
    Retweets = file1['retweets'].sum()
    print('Retweets:')
    print(Retweets)

    #Links
    Links = file1['url clicks'].sum()
    print('Links:')
    print(Links)
    
    hashtags = []
    for text in range(1,len(file1)):
        post = file1['Tweet text'][text]
        post = re.sub("[:!.,]", '', post)
        hashes = re.findall('#\S*', post)
        for tag in hashes:
            hashtags.append(tag)
    unique_hashtags =np.unique(hashtags)
    unique_hashtags = sorted(unique_hashtags, key= str.lower)
    print('The hashtags used were ' + str(unique_hashtags))
    print(Counter(hashtags))
    str1 = ''.join(str(e) for e in unique_hashtags)
    print(str1)



def get_FBHashtags(file1):
    file1 = file1.drop([0])
    hashtags = []
    for text in range(1,len(file1)):
        post = file1['Post Message'][text]
        post = re.sub("[:!.,]", '', post)
        hashes = re.findall('#\S*', post)
        for tag in hashes:
            hashtags.append(tag)
    unique_hashtags =np.unique(hashtags)
    unique_hashtags = sorted(unique_hashtags, key= str.lower)
    print('The hashtags used were ' + str(unique_hashtags))
    print(Counter(hashtags))
    str1 = ''.join(str(e) for e in unique_hashtags)
    print(str1)
    file1[1]


def get_TWHashtags(file1):
    hashtags = []
    for text in range(1,len(file1)):
        post = file1['Tweet text'][text]
        post = re.sub("[:!.,]", '', post)
        hashes = re.findall('#\S*', post)
        for tag in hashes:
            hashtags.append(tag)
    unique_hashtags =np.unique(hashtags)
    unique_hashtags = sorted(unique_hashtags, key= str.lower)
    print('The hashtags used were ' + str(unique_hashtags))
    print(Counter(hashtags))
    str1 = ''.join(str(e) for e in unique_hashtags)
    print(str1)
