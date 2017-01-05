library(dplyr)
library(lubridate)

#Set WD
setwd("~/Desktop/Bowen/January 2017")


##############################
#### Facebook Analysis########
##############################

#Read in File
FB_Weekly_Data<- read.csv('FB_Clean_Weekly12-5.csv')

#Replace NAs with 0

FB_Weekly_Data[is.na(FB_Weekly_Data)] <- 0

#Create Total Engagement Column
FB_Weekly_Data$Engagement = (FB_Weekly_Data$comment + FB_Weekly_Data$like + FB_Weekly_Data$share)

#Create Date Column
Dates <- format(as.POSIXct(strptime(FB_Weekly_Data$Posted,"%m/%d/%y %H:%M %p",tz="")) ,format = "%m/%d/%y")
FB_Weekly_Data$Date<- as.Date(Dates, '%m/%d/%y')

#Create Month Column
Month<- month(as.POSIXlt(FB_Weekly_Data$Date, format = '%m/%d/%y'))
FB_Weekly_Data$Month = month.abb[Month]
#Create Week Column
FB_Weekly_Data$Week = format.Date(FB_Weekly_Data$Date, format = "%V")

#####################
#### REACH ##########
#####################

#Group By Week

by_week<- group_by(FB_Weekly_Data, Week)
average_reach<- summarise(by_week, mean_reach = mean(Lifetime.Post.organic.reach))
average_reach

#Rename columns in Average Reach Data Frame
i = 0
for (i in 1: nrow(average_reach)){
  if (average_reach$Week[i] == '49') {
    average_reach$Week[i] = 'December 5'
  } else if (average_reach$Week[i] == '50'){
    average_reach$Week[i] = 'December 12'
  } else if (average_reach$Week[i] == '51') {
    average_reach$Week[i] = 'December 19'
  } else if (average_reach$Week[i] == '52') {
    average_reach$Week[i] = 'December 26'
  }
}

#Write out CSV with Average Daily post Data
write.csv(average_reach, file = 'Average_Daily_Reach.csv')

#######################
#### Engagement########
#######################

average_Engagement<- summarise(by_week, mean_engagement = mean(Engagement))
average_Engagement

#Rename columns in Average Engagement Data Frame
i = 0
for (i in 1: nrow(average_reach)){
  if (average_Engagement$Week[i] == '49') {
    average_Engagement$Week[i] = 'December 5'
  } else if (average_Engagement$Week[i] == '50'){
    average_Engagement$Week[i] = 'December 12'
  } else if (average_Engagement$Week[i] == '51') {
    average_Engagement$Week[i] = 'December 19'
  } else if (average_Engagement$Week[i] == '52') {
    average_Engagement$Week[i] = 'December 26'
  }
}


#Write out CSV with Average Daily post Data
write.csv(average_Engagement, file = 'Average_Daily_Engagement.csv')
######################
###Monthly Average####
######################

#Set WD
setwd("~/Desktop/Bowen")

Historical_Data<- read.csv('Historical_Clean.csv')

#Replace NAs with 0

Historical_Data[is.na(Historical_Data)] <- 0

#Create Total Engagement Column
Historical_Data$Engagement = (Historical_Data$comment + Historical_Data$like + Historical_Data$share)

#Create Date Column
Dates <- format(as.POSIXct(strptime(Historical_Data$Posted,"%m/%d/%y %H:%M %p",tz="")) ,format = "%m/%d/%y")
Historical_Data$Date<- Dates

#Create Month Column
Month<- month(as.POSIXlt(Historical_Data$Date, format = '%m/%d/%y'))
Historical_Data$Month = month.abb[Month]

#Find Average Reach by Month

by_month<- group_by(Historical_Data, Month)
average_monthly_Reach<- summarise(by_month, average_reach_month = mean(Lifetime.Post.organic.reach))
average_monthly_Reach

#Write out CSV
write.csv(average_monthly_Reach, file = 'Historical Average Reach By Month.csv')

#Find Average Engagement
average_monthly_engagement<- summarise(by_month, average_monthly_engagement = mean(Engagement))
average_monthly_engagement

#Write out CSV
write.csv(average_monthly_engagement, file = 'Historical Average Engagement.csv')


##############################
##### Likes Analysis ########
#############################
setwd("~/Downloads")

#Combine Data frames into 1
Likes_1 = read.csv('Historical Likes 1.csv')
Likes_2 = read.csv('Historical Likes_2.csv')

Likes_total = rbind(Likes_1, Likes_2)

#Create Net new likes column
Likes_total$Net_Likes = (Likes_total$Daily.New.Likes - Likes_total$Daily.Unlikes)

#Create Month Column

#set as date
Likes_total$Date<- as.Date(Likes_total$Date, '%m/%d/%y')

#Create Month Column
Month<- month(as.POSIXlt(Likes_total$Date, format = '%m/%d/%y'))
Likes_total$Month = month.abb[Month]

#Group By Month
by_month = group_by(Likes_total, Month)

############ 
Likes = read.csv('Weekly Likes.csv')
Likes_subset = Likes[, c('Date', 'Lifetime.Total.Likes')]

