# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:06:43 2021

@author: Mahmoud Abbas Makhlouf
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
   
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    Cities =['chicago','new york city','washington']
    while True:
        city = (input('Which City would you need to analyze (Chicago , New York City , Washington) ?\n')).lower()
        if city in Cities:
            break
    print( "ANALYZING "+city.upper() +" ......................")
    
    while True:
        Filter =(input('Do you want to filter data by month , day or both (if you don\'t like to filter enter None)?\n')).lower()
        if Filter.lower() == 'month' or Filter.lower() == 'day' or Filter.lower() == 'both' or Filter.lower() == 'none':
            break
        
        
    if Filter.lower() == 'month':
        day =''
        # get user input for month (all, january, february, ... , june)
        Months =['january','february','march','april','may','june']
        while True:
            month = (input('Enter name of the month (january , february , march , april , may , june) to filter by : \n')).lower()
            if month in Months:
                break
    elif Filter.lower()== 'day': 
        month = ''
        # get user input for day of week (all, monday, tuesday, ... sunday)
        Days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        while True:
            day = (input('Enter name of the day of week (monday , tuesday , wednesday , thursday , friday , saturday , sunday) to filter by : \n')).lower()
            if day in Days:
                break
    
    elif Filter.lower() == 'both':
         # get user input for month (all, january, february, ... , june)
        Months =['january','february','march','april','may','june']
        while True:
            month = (input('Enter name of the month (january , february , march , april , may , june) to filter by : \n')).lower()
            if month in Months:
                break   
        # get user input for day of week (all, monday, tuesday, ... sunday)
        Days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        while True:
            day = (input('Enter name of the day of week (monday , tuesday , wednesday , thursday , friday , saturday , sunday) to filter by : \n')).lower()
            if day in Days:
                break
    
    elif Filter.lower()=='none':
        month =''
        day =''
        
    print('-'*40)
    return city, month,day,Filter


def load_data(city, month, day,Filter):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if Filter == 'month':
        Months ={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
        df = df[df['Start Time'].dt.month == Months[month]]
    elif Filter == 'day':
        Days = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
        df = df[df['Start Time'].dt.dayofweek == Days[day]]
        
    elif Filter == 'both':
        Months ={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
        df = df[df['Start Time'].dt.month == Months[month]]
        Days = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
        df = df[df['Start Time'].dt.dayofweek == Days[day]]
        
    elif Filter =='none':
        pass
        
    return df


def time_stats(df,Filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    Days = {0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
    Months ={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june'}
  
    if Filter == 'month':
        # display the most common day of week
        df['Day'] = df['Start Time'].dt.dayofweek
        print('Most frequent day : ',Days[df['Day'].mode()[0]].title())

        # display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        print('Most frequent start hour ',(df['Hour'].mode()[0]).astype(str)+':00')
       
    elif Filter == 'day':
        # display the most common month
        df['Month'] = df['Start Time'].dt.month
        print('Most frequent month : ' , Months[df['Month'].mode()[0]].title())  
    
        # display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        print('Most frequent start hour ',(df['Hour'].mode()[0]).astype(str)+':00')     
        
    elif Filter == 'both':
        # display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        print('Most frequent start hour ',(df['Hour'].mode()[0]).astype(str)+':00')
    
    elif Filter =='none':
        # display the most common month
        df['Month'] = df['Start Time'].dt.month
        print('Most frequent month : ' ,Months[df['Month'].mode()[0]].title())
    
        # display the most common day of week
        df['Day'] = df['Start Time'].dt.dayofweek
        print('Most frequent day : ',Days[df['Day'].mode()[0]].title())
    
        # display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        print('Most frequent start hour ',(df['Hour'].mode()[0]).astype(str)+':00')
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station : ',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most commonly used end station : ',df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].astype(str)+' -> '+df['End Station'].astype(str)
    print('Most frequent trip : ',df['Trip'].mode()[0])
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time : %s Hours' %(int((df['Trip Duration'].sum())/3600)))

    # display mean travel time
    print('Average trip duration : %s Minutes' %(int((df['Trip Duration'].mean())/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types :\n',df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('Counts of gender :\n',df['Gender'].value_counts())
    except:
        #print('Error, Gender coulmn not existed in this data !!')
        pass

    # Display earliest, most recent, and most common year of birth
    try:
        print('Most earliest year of birth : ',int(df['Birth Year'].min()))
        print('Most recent year of birth: ',int(df['Birth Year'].max()))
        print('Most common year of birth : ',int(df['Birth Year'].mode()[0]))
    except:
        #print('Error, Birth Year coulmn not existed in this data !!')
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raws(df,i):
    # init a counter to get i raws every time
    count = 0
    
    # this while loop for first i raws and return a flag that determine 
    # if i need to ask the user again for next i raws .. etc
    while True:
        c = (input("Do you want to display The first "+str(i)+" raws of data ? (yes/no) : ")).lower()
        if c == 'yes':
            display_iraws_flag = True
            # print a specific raws with all coulmns
            print(df.iloc[count:count+i,:])
            break
        elif c == 'no':
            display_iraws_flag = False
            break
        else:
            continue
    
    # we will check if the flag is true to ask the user again
    if display_iraws_flag == True:
        # while yes , display the the next i raws
        while (input("Next "+str(i)+" Raws ? (yes or no) ")).lower() == 'yes':
            # increament the counter by i
            count=count+i
            # print a specific raws with all coulmns
            print(df.iloc[count:count+i,:])
        
        
    
def main():
    while True:
        city, month, day ,Filter = get_filters()
        df = load_data(city, month, day,Filter)
        time_stats(df,Filter)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raws(df,3)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()