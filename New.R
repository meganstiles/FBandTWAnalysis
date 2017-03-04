setwd("~/Desktop/Bowen/February 2017/")

FB.2<- read.csv('FB_Clean.csv')


#Replace NAs with 0

FB.2[is.na(FB.2)] <- 0

FB.2$Engagement = (FB.2$comment + FB.2$like + FB.2$share)

#Create Date Column
Dates <- format(as.POSIXct(strptime(FB.2$Posted,"%m/%d/%y %H:%M %p",tz="")) ,format = "%m/%d/%y")
FB.2$Date<- as.Date(Dates, '%m/%d/%y')

Two_weeks<- rbind(FB.2, FB_Weekly_Data)

##Week 3

setwd('~/Desktop/Bowen/February 2017/Feb 12 2017/')

FB.3<- read.csv('FB_Clean.csv')


#Replace NAs with 0

FB.3[is.na(FB.3)] <- 0

FB.3$Engagement = (FB.3$comment + FB.3$like + FB.3$share)

Three_weeks<- rbind(Two_weeks, FB.3)
total = sum(Three_weeks$Lifetime.Post.organic.reach)
total
length(Three_weeks$Post.ID)
total/length(Three_weeks$Post.ID)


total_engagement = sum(Three_weeks$Engagement)
avg_engagement = total_engagement/length(Three_weeks$Post.ID)
avg_engagement
