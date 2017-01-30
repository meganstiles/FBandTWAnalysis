#Import Funtions
os.chdir('/Users/meganstiles/Desktop/FBandTWAnalysis/')
import Social_Analysis as so
import Merge_Data_Frames as me 
#Set Working Directory to location of source files:
os.chdir('/Users/meganstiles/Desktop/Bowen/January 2017/')

#Read in Files
Posts = pd.read_csv('Jan 22 Metrics.csv',encoding= 'latin-1')
Engagement = pd.read_csv('Jan 22 Engagements.csv', encoding= 'latin-1')
Links = pd.read_csv('Jan 22 Links.csv', encoding= 'latin-1')

#Analyze Facebook Insights
so.get_analysis(Posts, Engagement, Links)

#Twitter Analysis

#Set Working Directory

os.chdir('/Users/meganstiles/Desktop/Bowen/January 2017/')

#Read in file

Tweets = pd.read_csv('Jan 22 Tweets.csv')

so.get_Tweets(Tweets)

#Merge FB Data Sets

#Posts_file = pd.read_csv('Metrics 12-25.csv',encoding= 'latin-1')
#Engagement_file = pd.read_csv('Engagements 12-25.csv', encoding= 'latin-1')
#Links_file = pd.read_csv('Links 12-25.csv', encoding= 'latin-1')

me.merge_fb_files(Posts,Engagement, Links)

#Clean Twitter DF

me.merge_Twitter_files(Tweets)

#Facebook Hashtags

so.get_FBHashtags(Posts)

