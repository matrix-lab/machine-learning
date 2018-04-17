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
    city = ''
    while city not in CITY_DATA.keys():
        print('which city? please select Chicago, New York City, or Washington?')
        city = input().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    print('would like to filter the date by month, Yes/No?')
    month = ''
    if input().lower() == 'yes':
        while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('which month? January, February, March, April, May, or June, and "all" for no time filter')
            month = input().lower()
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('would like to filter the date by day, Yes/No?')
    day = ''
    if input().lower() == 'yes':
        while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('which day? Monday, Tuesday, Wednesday, Thursday, Friday, Staturday, or Sunday, and "all" for no filter')
            day = input().lower()
    else:
        day = 'all'

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
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Frequent Month:', df['month'].mode()[0], ' counts:', df['month'].value_counts().max())

    # TO DO: display the most common day of week
    print('Most Frequent Day of Week:', df['day_of_week'].mode()[0], ' counts:', df['day_of_week'].value_counts().max())

    # TO DO: display the most common start hour
    print('Most Frequent Hour:', df['hour'].mode()[0], ' counts:', df['hour'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
    most_index = most_start_end['count'].argmax();
    most_start = most_start_end.loc[most_index]['Start Station']
    most_end = most_start_end.loc[most_index]['End Station']
    most_count = most_start_end.loc[most_index]['count']
    print('Most Frequent combination of start and end station trip:', most_start, ' and ', most_end, ' count:', most_count), 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
