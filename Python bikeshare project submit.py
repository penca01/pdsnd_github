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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city\'s data would you like to see (Chicago, New York City or Washington)? ').lower()
        if (city in ['chicago', 'new york city', 'washington']):
            break
        else:
            print('Please enter one of the following: Chicago, New York City, or Washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to see all the available data, or just the data for a month (January through June)? ').lower()
        if (month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
            break
        else:
            print('Please enter one of the following: January, February, March, April, May, June, or all.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to see all available data, or would you just like to see the data by day (Sunday through Saturday)? ').lower()
        if (day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']):
            break
        else:
            print('Please enter one of the following: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all.')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


    if day != 'all':
        df = df[df[day_of_week] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    hour = df['Start Time'].dt.hour
    popular_hour = hour.mode()[0]

    print('Most frequent start month:', popular_month)
    print('Most frequent start day:', popular_day)
    print('Most frequent start hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startst = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_endst = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df[['Start Station', 'End Station']].mode().loc[0]

    print('Most popular start station:', popular_startst)
    print('Most popular end station:', popular_endst)
    print('Most popular trip: {} to {}'.format(popular_trip[0], popular_trip[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = int(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    avg_trip = int(df['Trip Duration'].mean())

    print('Total trip time was:', total_trip)
    print('The average trip lasted:', avg_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest_user = df['Birth Year'].max()
    youngest_user = df['Birth Year'].min()
    popular_age = df['Birth Year'].mode()

    print(users)
    print(gender)
    print(oldest_user)
    print(youngest_user)
    print(popular_age)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Limits the output to 5 lines at a time for ease of readibility.
    After loading the data, it asks the user whether they would like to see
    the next 5 lines of data."""
    record = 0
    while True:
        print(df[0:5])
        raw = input('Would you like to see the next 5 lines of raw data (Enter yes or no)? ').lower()
        if raw == 'yes':
            print(df.iloc[record:record + 5])
            continue
        else:
            break



def main():
    """Defines the main set of operations.
    Loads all defined variables when a city month and day are input by a user.
    Asks the user whether they would like to restart the application and view other data."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart and view additional data? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
