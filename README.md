# 2016 US Bike Share Analysis

## Table of Contents
- [Introduction](#intro)
- [Data Collection and Wrangling](#wrangling)
  - [Condensing the Trip Data](#condensing)
- [Exploratory Data Analysis](#eda)
  - [Statistics](#statistics)
  - [Visualizations](#visualizations)
- [Further Analysis](#eda_continued)
- [Conclusions](#conclusions)

<a id='intro'></a>
## Introduction

This project will attempt to provide insights based on exploratory analysis of bike share share data. The data used for this project is orginally from [Motivate](https://www.motivateco.com/) which is a major bike-share system provider accross the United States.

Three major cities were analysed in this project (New York City, Chicago and Washington DC) and compared to analyse differences of those respective systems with regards to registered, regular and casual users.

This project was part of Udacity's Data Analyst Nanodegree program. The full submitted project can be found in the jupyter notebook file in the project files.

<a id='wrangling'></a>
## Data Collection and Wrangling

The data includes a record of individual trips in 2016. The orginal data source link of each of the three cities is shown below:

- New York City (Citi Bike): [Link](https://www.citibikenyc.com/system-data)
- Chicago (Divvy): [Link](https://www.divvybikes.com/system-data)
- Washington, DC (Capital Bikeshare): [Link](https://www.capitalbikeshare.com/system-data)

The data used for this project can be found in the `/data/` folder of the project files. The data shown in the folders are a 2% sample of the orginal data set.

<a id='condensing'></a>
### Condensing the Trip Data

The functions in this section trim and clean the data. It will also generate new data files showing the five parameters of interest: trip duration, starting month, starting hour, day of the week, and user type.

The functions with summaries in this section are listed below:

- `duration_in_mins(datum, city)` Takes as input a dictionary containing info about a single trip (datum) and its origin city (city) and returns the trip duration in units of minutes 
- `time_of_trip(datum, city)` Takes as input a dictionary containing info about a single trip (datum) and its origin city (city) and returns the month, hour, and day of the week in which the trip was made
- `type_of_user(datum, city)`  Takes as input a dictionary containing info about a single trip (datum) and its origin city (city) and returns the type of system user that made the trip
- `condense_data(in_file, out_file, city)`  This function takes full data from the specified input file and writes the condensed data to a specified output file. The city
argument determines how the input file will be parsed.

<a id='eda'></a>
## Exploratory Data Analysis

This section involves the exploratory analysis of the cleaned data.

<a id='statistics'></a>
### Statistics

The first section shows which city has the highest number of trips, the highest proportion of trips made by subscribers and the highest proportion of trips made by short-term customers. Functions shown below:

- `number_of_trips(filename)` This function reads in a file with trip data and reports the number oftrips made by subscribers, customers, and total overall.
- `duration_of_trips(filename)` This function reads in a file with trip data and reports the average trip length and proportion of rides longer than 30 minutes for each city
- `usertype_average(filename)` This function reads file and returns trip data of different user types

<a id='visualizations'></a>
### Visualizations

This section used `matplotlib` to generate graphical visualisations of trip distribution. This is used to show time duration differences for different user types through positive or negative skews shown by histograms. Washington DC was chosen for anaysis in this section.

- First part of this section was an example of generating a histogram with dummy data to test the libaries worked correctly
- The next histogram showed all trip durations, however it was shown that a limiter was needed to eliminate outliers.
- Lastly, this histogram showed the distribution comparison between normal customers and subscribers. It was shown subsribers peak during periods 0-10 minutes while customers peaked at 18-25 minutes.

<a id='eda_continued'></a>
## Further Analysis

This section shows further anaysis on how usage during rush hours (set as 07:00 to 09:00 and 17:00 to 20:00) changed during weekdays versus weekends for both subscribers and customers in NYC. The aim of this was show how usage habits changed for both usertypes at different stages of the week.

The results are show below (from the visualisations):
- Subscribers: *57.3%* of weekday trips and *50.7%* of weekend trips were during rush hours respectively 
- Customers: *29.59%* of weekday trips and *30.52%* of weekend trips were during rush hours respectively 

<a id='conclusions'></a>
## Conclusions

The anaysis from this project show that it is highly likely that subscribers use bike sharing for commuting to work far more than customers who appear to use bikes more consistently throughout the day. Furthermore subscriber habits change more notably during weekends with a drop of usage during rushour of 6.6% compared to a slight rise of 0.93% for customers.

Considering that most users are subscribers, a potential action point from this analysis is to ensure increased availablity during rushhours on weekdays. Also consider using a marketing strategy that emphasises *leisure* use for non-commuting activity to attract new customers while targeting exisitng customers with *commuting* advantages offered by bike sharing to convert them into subscribers.
