#Import Funtions
os.chdir('/Users/meganstiles/Desktop/github/FBandTWAnalysis/')
import Social_Analysis as so
import Merge_Data_Frames as me 
#Set Working Directory to location of source files:
os.chdir('/Users/meganstiles/Desktop/Bowen/February 2017/')

#Read in Files
Posts = pd.read_csv('Feb 5 Metrics.csv',encoding= 'latin-1')
Engagement = pd.read_csv('Feb 5 Engagements.csv', encoding= 'latin-1')
Links = pd.read_csv('Feb 5 Links.csv', encoding= 'latin-1')

#Analyze Facebook Insights
so.get_analysis(Posts, Engagement, Links)

#Twitter Analysis

#Set Working Directory

os.chdir('/Users/meganstiles/Desktop/Bowen/January 2017/')

#Read in file

Tweets = pd.read_csv('Feb 5 Tweets.csv')

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

#Fix Date

Tweets['time'][1]
type(Tweets['time'][1])
list = []
for i in range(0,len(Tweets)):
    x = re.sub('+0000', '', Tweets['time'][i])
    list.append(x)

Tweets['Date'] = list

Tweets.to_csv('Tweets.Date.csv')