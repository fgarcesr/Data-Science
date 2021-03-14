#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

df_chicago = pd.read_csv("chicago.csv")
df_new_york_city = pd.read_csv("new_york_city.csv")
df_washington = pd.read_csv("washington.csv")

CITY_DATA = { 'chicago': df_chicago,
              'new york city': df_new_york_city,
              'washington': df_washington }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please write the city you would like to analyze from chicago, new york city and washington: ")
        city = city.lower()
        if city not in CITY_DATA.keys():
            print("Please try again")
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please write to select a month from january to june, or just write all: ")
        month = month.lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Please try again")
        else:
            break    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("please write to select a weekday from monday to sunday, or just write all: ")
        day = day.lower()
        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):
            print("Please try again")
        else:
            break


    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    df = CITY_DATA[city]
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.day_name()
    df["Start-End-Station"] = "[" + df["Start Station"] + "]-[" + df["End Station"] + "]"
    
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        df = df[df["month"] == month]
    
    if day != "all":
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df["month"].mode()
    months = {1:"january",2:"february",3:"march",4:"april",5:"may",6:"june"}
    print("The most common month to travel is: {}".format(months[month_mode[0]]))

    # TO DO: display the most common day of week
    day_mode = df["day_of_week"].mode()
    print("The most common day to travel is: {}".format(day_mode[0]))

    # TO DO: display the most common start hour
    hour_mode = df["Start Time"].dt.hour.mode()
    print("The most common start hour to travel is: {}{}".format(hour_mode[0]," hrs"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode = df["Start Station"].mode()
    print("The most common Start Station for users is: {}".format(start_station_mode[0]))
    # TO DO: display most commonly used end station
    end_station_mode = df["End Station"].mode()
    print("The most common End Station for users is: {}".format(end_station_mode[0]))

    # TO DO: display most frequent combination of start station and end station trip

    combi_station_mode = df["Start-End-Station"].mode().iloc[:df["Start-End-Station"].mode().shape[0]]
    print("The most common Station Combine is: {}".format(combi_station_mode[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    total_time_min = total_time//60
    total_time_seg = total_time%60
    print("The total travel time whitin your selection is: {}{}{}{}".format(total_time_min," min ",round(total_time_seg, 2)," seg"))

    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    mean_time_min = mean_time//60
    mean_time_seg = mean_time%60
    print("The average travel time within your selection is: {}{}{}{}".format(mean_time_min," min ",round(mean_time_seg, 2)," seg"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df["User Type"].value_counts(dropna=False)
    print("The count per user type is: \n{}".format(user_count))

    # TO DO: Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("The count per gender is: \n{}".format(gender_count))
    except KeyError:
        print("There are no information about Gender to display")    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yearbirth = df["Birth Year"].min()
        recent_yearbirth = df["Birth Year"].max()
        mode_yearbirth = df["Birth Year"].mode()
        print("The earliest year of birth is: {}".format(earliest_yearbirth))
        print("The most recent year of birth is: {}".format(recent_yearbirth))
        print("The most common year of birth is: {}".format(mode_yearbirth))
    except KeyError:
        print("There are no information about Birth Year to display")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    count = 0
    while True:
        answer = input("Would you like to see 5 lines of raw data? Enter yes or no: ")
        if answer.lower() == "yes":
            print(df.iloc[count:count+5])
            count += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()