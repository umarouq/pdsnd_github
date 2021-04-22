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
    print('Hello!!! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("Name of the city: (chicago, new york city, or washington)").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Not on the list of cities (chicago, new york city or washington)")
        else:
            break

        # get user input for month (all, january, february, ... , june)
        
    while True:
        month = input("Name of the month: (all, january to june)").lower()
        if month not in ('all', 'january', 'february','march', 'april', 'may','june'):
            print("Not on the list of months")
        else:
            break

        # get user input for day of week (all, monday to sunday)

    while True:
        day = input("Name of the week: (all, monday, tuesday, ... sunday)").lower()
        if day not in ('all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday'):
            print("Not on the list of weeks")
        else: 
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    

    # load data file into a dataframe
    #df = pd.read_csv(CITY_DATA[city])
    df = pd.read_csv(f'C:\\Users\\umar.ibrahim1971\\Downloads\\bikeshare-2\\{CITY_DATA[city]}')
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
 
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)
 
 
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common month:', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]

    print('Most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station (frenquently used)
    
    most_common_ss = df['Start Station'].mode()[0]
    print('Most common Start Station:', most_common_ss)

    # display most commonly used end station (frequently used)

    most_common_es = df['End Station'].mode()[0]
    print('Most common End Station:', most_common_es)


    # display most frequent combination of start station and end station trip

    #if 'Start Station' in df.columns and 'End Station' in df.columns:
    df['route'] = df['Start Station'] + ' -> ' + df['End Station']
    print('Most frequent route '.ljust(40, '.'), df['route'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    print('Total Travel Time '.ljust(40, '.'), df['Trip Duration'].sum())

    # display mean travel time
    print('Mean Travel Time '.ljust(40, '.'), df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)
    else: 
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # Display earliest, most recent, and most common year of birth
    print(' Age stats '.center(78, '-'))

    if 'Birth Year' in df:
        print('Earliest Birth Year '.ljust(40, '.'), int(df['Birth Year'].min()))
        print('Most recent Birth Year '.ljust(40, '.'), int(df['Birth Year'].max()))
        print('Most common Birth Year '.ljust(40, '.'), int(df['Birth Year'].mode()[0]))
    else:
        print('Birth Year stats cannot be calculated because Gender does not appear in the dataframe')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while True:
        if view_data != 'no':
            print(df.iloc[0:5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
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
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
