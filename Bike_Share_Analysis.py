## 2016 US Bike Share Activity 
## Introduction
 
# Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. 
# Bicycle-sharing systems allow users to rent bicycles for short trips, typically 30 minutes or less. 
# Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. 
# These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.
# In this project, we will perform an exploratory analysis on data provided by [Motivate](https://www.motivateco.com/), a bike-share system provider for many major cities in the United States. 
# We will compare the system usage between three large cities: New York City, Chicago, and Washington, DC. 
# We will also see if there are any differences within each system for those users that are registered, regular users and those users that are short-term, casual users.

## Data Collection and Wrangling
 
# import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
import calendar

def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    with open(filename, 'r') as f_in:
        # csv library to set up a DictReader object
        trip_reader = csv.DictReader(f_in)
        # DictReader object to read the first trip from the data file and store it in a variable
        first_trip = next(trip_reader)
        # Print the first trip
        pprint(first_trip)
    # output city name and first trip for later testing
    return (city, first_trip)

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip

def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    """
    # Identify column name by city
    column = ()
    function = ()
    if city == 'NYC':
        column = 'tripduration'
        function = 60
    elif city == 'Chicago':
        column = 'tripduration'
        function = 60
    elif city == 'Washington':
        column = 'Duration (ms)'
        function = 60000  
    # Assign time to duration variable
    duration = ()  
    duration = (datum[column])  
    # Convert time to minutes and return
    duration = int(duration) / function
    return duration

# A test to check that the code works. There should be no output if all of
# the assertions pass. 
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001

def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    """
    # Identify column name and timedate format by city
    column = ()
    if city == 'NYC':
        column = 'starttime'
        datetime_format = '%m/%d/%Y %H:%M:%S'
    elif city == 'Chicago':
        column = 'starttime'
        datetime_format = '%m/%d/%Y %H:%M'
    elif city == 'Washington':
        column = 'Start date'
        datetime_format = '%m/%d/%Y %H:%M'   
    # Extract datetime to variable
    dateandtime = datum[column]   
    # Convert to datetime object format
    dateeb = datetime.strptime(dateandtime, datetime_format)  
    # Extract required outputs
    month = dateeb.month
    hour = dateeb.hour
    day_of_week = dateeb.weekday()
    day_of_week = calendar.day_name[day_of_week]
    return (month, hour, day_of_week)

# A test to check that the code works. There should be no output if all of
# the assertions pass.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    assert time_of_trip(example_trips[city], city) == tests[city]

def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.
    """
    # Identify column name  by city
    column = ()
    if city == 'NYC':
        column = 'usertype'
    elif city == 'Chicago':
        column = 'usertype'
    elif city == 'Washington':
        column = 'Member Type'   
    # Extract member/user type
    user_type = datum[column]
    # Convert to standard format
    if city =='Washington':
        if user_type == 'Registered':
            user_type = 'Subscriber'
        elif user_type == 'Casual':
            user_type = 'Customer'
    return user_type

# A test to check that the code works. There should be no output if all of
# the assertions pass. 
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    assert type_of_user(example_trips[city], city) == tests[city]

def condense_data(in_file, out_file, city):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    """ 
    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        
        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        #set up csv DictReader object 
        trip_reader = csv.DictReader(f_in)
        # collect data from and process each row
        for row in trip_reader:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point = {}
            new_point['duration'] = duration_in_mins(row, city)
            new_point['month'] = time_of_trip(row, city)[0]
            new_point['hour'] = time_of_trip(row, city)[1]
            new_point['day_of_week'] = time_of_trip(row, city)[2]
            new_point['user_type'] = type_of_user(row, city)
            # write the processed information to the output file
            trip_writer.writerow(new_point)
            
# Run this cell to check code works
city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',
                            'out_file': './data/Washington-2016-Summary.csv'},
             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',
                         'out_file': './data/Chicago-2016-Summary.csv'},
             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',
                     'out_file': './data/NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
    condense_data(filenames['in_file'], filenames['out_file'], city)
    print_first_point(filenames['out_file'])

def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        
        # initialize count variables
        n_subscribers = 0
        n_customers = 0
        # tally up ride types
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            else:
                n_customers += 1
        # compute total number of rides
        n_total = n_subscribers + n_customers
        # return tallies as a tuple
        return(n_subscribers, n_customers, n_total)

data_file = './examples/BayArea-Y3-Summary.csv'
city_file = {'Washington':('./data/Washington-2016-Summary.csv'), 'Chicago': ('./data/Chicago-2016-Summary.csv'), 'NYC':('./data/NYC-2016-Summary.csv')}
    
Total = {}
Subscriber_proportion = {}
Customer_proportion = {}
    
for city, filenames in city_file.items():
    Total[city] = number_of_trips(filenames)[2]
    Subscriber_proportion[city] = ((number_of_trips(filenames)[0] / number_of_trips(filenames)[2]) * 100)
    Customer_proportion[city] = ((number_of_trips(filenames)[1] / number_of_trips(filenames)[2]) * 100)

max_total = max(Total, key=Total.get)
print('City with most trips:', max_total)
max_subscriber_proportion = max(Subscriber_proportion, key=Subscriber_proportion.get)
print('City with highest proportion of subscribers:', max_subscriber_proportion)
max_customer_proportion = max(Customer_proportion, key=Customer_proportion.get)
print('City with highest proportion of customers:', max_customer_proportion)

def duration_of_trips(filename):
    """
    This function reads in a file with trip data and reports the average trip length and 
    proportion of rides longer than 30 minutes for each city
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        # initialize total time and count variables
        total_minutes = 0
        total_30 = 0
        count_trips = 0
        # convert to float, sum total duration and count
        for row in reader:
            if float(row['duration']) > 30:
                total_minutes += float(row['duration']) 
                total_30 += 1 #float(row['duration']) 
                count_trips += 1
            else:
                total_minutes += float(row['duration']) 
                count_trips += 1        
        # finds average and proportion over 30
        avg_trip = total_minutes / count_trips
        avg_trip = round(avg_trip, 1)
        proportion_over30 = (total_30 / count_trips) * 100
        proportion_over30 = round(proportion_over30, 1)
        return(avg_trip, proportion_over30)

data_file = './examples/BayArea-Y3-Summary.csv'
city_file = {'Washington':('./data/Washington-2016-Summary.csv'), 'Chicago': ('./data/Chicago-2016-Summary.csv'), 'NYC':('./data/NYC-2016-Summary.csv')}
        
for city, filename in city_file.items():
    duration_of_trips(filename)
    print('{} has an average trip duration of {} minutes with {} % of rides over 30 minutes'.format(city, duration_of_trips(filename)[0], duration_of_trips(filename)[1]))

# Within Chicago, customers have a significantly longer average trip duration of 41.7 minutes compared to subscribers at just 12.5 minutes.                                            ##

def usertype_average(filename):
    """
    This function reads file and returns trip data of different user types
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        # initialize total time and count variables by usertype
        sub_total_minutes = 0
        cus_total_minutes = 0
        sub_count_trips = 0
        cus_count_trips = 0
        # convert to float, sum total duration and count
        for row in reader:
            if row['user_type'] == 'Subscriber':
                sub_total_minutes += float(row['duration'])  
                sub_count_trips += 1
            elif row['user_type'] == 'Customer':
                cus_total_minutes += float(row['duration']) 
                cus_count_trips += 1    
        # finds average duration by user
        sub_avg_trip = sub_total_minutes / sub_count_trips
        sub_avg_trip = round(sub_avg_trip, 1)
        cus_avg_trip = cus_total_minutes / cus_count_trips
        cus_avg_trip = round(cus_avg_trip, 1)
        return(sub_avg_trip, cus_avg_trip)    

city_file = {'Washington':('./data/Washington-2016-Summary.csv'), 'Chicago': ('./data/Chicago-2016-Summary.csv'), 'NYC':('./data/NYC-2016-Summary.csv')}
        
for city, filename in city_file.items():
    usertype_average(filename)
    print('{} : Subscribers have an average trip duration of {} minutes, Customers have an average trip duration of {} minutes '.format(city, usertype_average(filename)[0], usertype_average(filename)[1]))
    
# load graphic library
import matplotlib.pyplot as plt

# example histogram, data taken from bay area sample
data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,
        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,
        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,
         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,
         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]
plt.hist(data)
plt.title('Distribution of Trip Durations')
plt.xlabel('Duration (m)')
plt.show()

def plot_all(filename):
    """
    This function reads file and plots all trip times on histogram
    """
    get_ipython().run_line_magic('matplotlib', 'inline')
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        # initialize date collection vairable
        data = []    
        # convert to float and add to collection varable
        for row in reader:
                data.append(float(row['duration']))  
        # create histogram
        plt.hist(data)
        plt.title('Distribution of Trip Durations')
        plt.xlabel('Duration (m)')
        plt.show() 
        return    

city_file = {'Washington':('./data/Washington-2016-Summary.csv')}
        
for city, filename in city_file.items():
    plot_all(filename)

import numpy as np

def plot_all(filename):
    """
    This function reads file and plots all trip times on histogram
    """
    get_ipython().run_line_magic('matplotlib', 'inline')
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        # initialize date collection vairable
        data_sub = []
        data_cus = []  
        # convert to float and add to collection varable
        for row in reader:
            if row['user_type'] == 'Subscriber':
                if float(row['duration']) < 75:
                    data_sub.append(float(row['duration'])) 
            elif row['user_type'] == 'Customer': 
                if float(row['duration']) < 75:
                    data_cus.append(float(row['duration']))      
        # create histogram
        plt.hist(data_sub, rwidth=1)
        plt.title('Distribution of Trip Durations for Subscribers')
        plt.xlabel('Duration (m)')
        plt.show()
        plt.hist(data_cus, rwidth=1)
        plt.title('Distribution of Trip Durations for Customers')
        plt.xlabel('Duration (m)')
        plt.show()               
        return    

city_file = {'Washington':('./data/Washington-2016-Summary.csv')}
        
for city, filename in city_file.items():
    plot_all(filename)

# One question that was explored was how usage during rush hours (set as 07:00 to 09:00 and 17:00 to 20:00) changed during weekdays versus weekends for both subscribers and customers in NYC. 
# The aim of this was show how usage habits changed for both usertypes at different stages of the week.
# 
# The results are show below 
# Subscribers: *57.3%* of weekday trips and *50.7%* of weekend trips were during rush hours respectively 
# Customers: *29.59%* of weekday trips and *30.52%* of weekend trips were during rush hours respectively 
# It is highly likely that subscribers use bike sharing for commuting to work far more than customers who appear to use bikes more consistently through out the day. 
# Furthermore subscriber habits change more notably during weekends with a drop of usage during rushour of 6.6% compared to a slight rise of 0.93% for customers. 
# Considering that most users are subscribers, a potential action point from this analysis is to ensure increased availablity during rushhours on weekdays. 
# Also consider using a marketing strategy that emphasises *leisure* use for non-commuting activity to attract new customers while targeting exisitng customers with *commuting* advantages offered by bike sharing to convert them into subscribers.

import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def plot_analysis(filename):
    """
    This function plots the proportion of usgae in work hours vs non work hours for on weekdays and weekend for
    subscribers and customers
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        reader2 = csv.DictReader(f_in)
        # initialize date collection vairables
        sub_weekday_rush_count = 0
        sub_weekday_total_count = 0
        sub_weekend_rush_count = 0
        sub_weekend_total_count = 0
        cus_weekday_rush_count = 0
        cus_weekday_total_count = 0
        cus_weekend_rush_count = 0
        cus_weekend_total_count = 0        
        # convert to int and add to respective collection varables
        for row in reader:
            if (7 <= float(row['hour']) <= 9) or (17 <= float(row['hour']) <= 20):
                if str(row['day_of_week']) == ('Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'):
                    if str(row['user_type']) == 'Subscriber':
                        sub_weekday_rush_count += 1
                        sub_weekday_total_count += 1
                    elif str(row['user_type']) == 'Customer':
                        cus_weekday_rush_count += 1
                        cus_weekday_total_count += 1     
                else:
                    if str(row['user_type']) == 'Subscriber':
                        sub_weekend_rush_count += 1
                        sub_weekend_total_count += 1
                    elif str(row['user_type']) == 'Customer':
                        cus_weekend_rush_count += 1
                        cus_weekend_total_count += 1    
            else:
                if str(row['day_of_week']) == ('Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'):
                    if str(row['user_type']) == 'Subscriber':
                        sub_weekday_total_count += 1
                    elif str(row['user_type']) == 'Customer':
                        cus_weekday_total_count += 1     
                else:
                    if str(row['user_type']) == 'Subscriber':
                        sub_weekend_total_count += 1
                    elif str(row['user_type']) == 'Customer':
                        cus_weekend_total_count += 1 
        sub_weekday_output = (sub_weekday_rush_count / sub_weekday_total_count) * 100
        sub_weekend_output = (sub_weekend_rush_count / sub_weekend_total_count) * 100     
        cus_weekday_output = (cus_weekday_rush_count / cus_weekday_total_count) * 100
        cus_weekend_output = (cus_weekend_rush_count / cus_weekend_total_count) * 100    
        sub_weekday_output = round(sub_weekday_output, 2)
        sub_weekend_output = round(sub_weekend_output, 2)
        cus_weekday_output = round(cus_weekday_output, 2)
        cus_weekend_output = round(cus_weekend_output, 2)
        # data to plot
        n_groups = 2
        data_1 = []
        data_1.append(sub_weekday_output)
        data_1.append(cus_weekday_output)
        data_2 = []
        data_2.append(sub_weekend_output)
        data_2.append(cus_weekend_output)      
        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8
        rects1 = plt.bar(index, data_1, bar_width, alpha=opacity, color='b',label='% of rush hours trips on weekdays')
        rects2 = plt.bar(index + bar_width, data_2, bar_width, alpha=opacity, color='g', label='% of rush hours trips on weekends')
        plt.xlabel('User Type')
        plt.ylabel('% of trips in rush hours')
        plt.title('NYC Rush Hour Usage Weekday vs Weekends')
        plt.xticks(index + (0.5 * bar_width) , ('Subscribers', 'Customers')) #
        plt.legend()
        plt.tight_layout()
        plt.show()
        print('For subscribers, {}% of weekday trips and {}% of weekend trips were during rush hours respectively'.format(sub_weekday_output, sub_weekend_output))
        print('For customers, {}% of weekday trips and {}% of weekend trips were during rush hours respectively'.format(cus_weekday_output, cus_weekend_output))
        return

city_file = {'NYC':('./data/NYC-2016-Summary.csv')}
        
for city, filename in city_file.items():
    plot_analysis(filename)

#from subprocess import call
#call(['python', '-m', 'nbconvert', 'Bike_Share_Analysis.ipynb'])

