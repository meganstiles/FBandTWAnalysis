#Import Funtions
os.chdir('/Users/meganstiles/Desktop/FBandTWAnalysis/')
import Social_Analysis as so
import Merge_Data_Frames as me 
#Set Working Directory to location of source files:
os.chdir('/Users/meganstiles/Desktop/Bowen/December 2016/')

#Read in Files
Posts = pd.read_csv('Metrics 12-25.csv',encoding= 'latin-1')
Engagement = pd.read_csv('Engagements 12-25.csv', encoding= 'latin-1')
Links = pd.read_csv('Links 12-25.csv', encoding= 'latin-1')

#Analyze Facebook Insights
so.get_analysis(Posts, Engagement, Links)

#Twitter Analysis

#Set Working Directory

os.chdir('/Users/meganstiles/Desktop/Bowen/December 2016/')

#Read in file

Tweets = pd.read_csv('tweet_activity_metrics_asdmra_20161219_20161226_en.csv')

so.get_Tweets(Tweets)

#Merge FB Data Sets

Posts_file = pd.read_csv('Metrics 12-25.csv',encoding= 'latin-1')
Engagement_file = pd.read_csv('Engagements 12-25.csv', encoding= 'latin-1')
Links_file = pd.read_csv('Links 12-25.csv', encoding= 'latin-1')

me.merge_fb_files(Posts_file,Engagement_file, Links_file)

#Clean Twitter DF

me.merge_Twitter_files(Tweets)