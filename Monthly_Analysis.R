
#Set WD
setwd("~/Desktop/Bowen/January 2017")


##############################
#### Facebook Analysis########
##############################

#Read in File

FB_Data<- read.csv('FB_clean.csv')

#Replace NAs with 0

FB_Data[is.na(FB_Data)] <- 0

#Create Total Engagement Column

FB_Data$Engagement = (FB_Data$comment + FB_Data$like + FB_Data$share)

#find Total Reach for Month

sum(FB_Data$Lifetime.Post.organic.reach)
#Separate Posts by type

FB_Link_Posts<- FB_Data[FB_Data$Type == 'Link',]
FB_Photo_Posts<- FB_Data[FB_Data$Type == 'Photo',]
FB_SharedVideo_Posts<- FB_Data[FB_Data$Type == 'SharedVideo',]
FB_Status_Posts<- FB_Data[FB_Data$Type == 'Status',]

#Find Reach of posts by type

print( 'The reach of link posts is:')
sum(FB_Link_Posts$Lifetime.Post.organic.reach)

print( 'The reach of photo posts is:')
sum(FB_Photo_Posts$Lifetime.Post.organic.reach)

print( 'The reach of SharedVideo posts is:')
sum(FB_SharedVideo_Posts$Lifetime.Post.organic.reach)

print( 'The reach of Status posts is:')
sum(FB_Status_Posts$Lifetime.Post.organic.reach)

#Find Total Engagement by Post Type

print('The engaagement of link posts is:')
sum(FB_Link_Posts$Engagement)

print('The engaagement of photo posts is:')
sum(FB_Photo_Posts$Engagement)

print('The engaagement of SharedVideo posts is:')
sum(FB_SharedVideo_Posts$Engagement)

print('The engaagement of status posts is:')
sum(FB_Status_Posts$Engagement)

###############################
###Twitter Analysis###########
##############################

#Read in Data

TW_Data<- read.csv('December_Tweets.csv')

#Find Total Reach for Month

sum(TW_Data$impressions)

#Create Engagement Column
TW_Data$Total_Engagement<- (TW_Data$retweets + TW_Data$replies + TW_Data$likes + TW_Data$url.clicks)

#Find Total Engagement
sum(TW_Data$Total_Engagement)
