
os.chdir('/Users/meganstiles/Desktop/Bowen/December 2016/')

Posts = pd.read_csv('12-18 Metrics.csv',encoding= 'latin-1')
Engagement = pd.read_csv('12-18 Engagements.csv', encoding= 'latin-1')
Links = pd.read_csv('12-18 Links.csv', encoding= 'latin-1')

merge_fb_files(Posts,Engagment, Links):
    
    #Drop top line (contains information we don't need)
    Posts = Posts.drop([0])
    
    #Convert files to numeric   
    Posts = Posts.convert_objects(convert_numeric=True)
    Engagement = Engagement.convert_objects(convert_numeric=True)
    Links = Links.convert_objects(convert_numeric=True)

    #Subset files with columns I need
    Total = Posts[[0,1,2,3, 6, 9]]
    Engagement = Engagement[[1,9,10,11]]
    Links = Links[[1,9]]

    #Concatinate columns into One Data Frame
    Data = pd.concat([Total, Links, Engagement], axis =1, join= 'inner')
    Data = Data[[1,2,3,4,5,7,9,10,11]]

    #Write out CSV
    Data.to_csv('12-18Total.csv')

Twitter = pd.read_csv('tweet_activity_metrics_asdmra_20161212_20161219_en.csv')    
merge_Twitter_files(file):

    #Subset Data Frame

    Twitter_new = file[[1,2,4,7,8,9,11]]
    
    #Write out to csv
    Twitter_new.to_csv('Tweets.csv')

