## TODO: import all necessary packages and functions
import csv
from datetime import datetime
import time


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new-york-city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    print('Hello! Let\'s explore some US bikeshare data!')
    # TODO: handle raw input and complete function
    city = ''
    while city not in ['chicago', 'new_york_city', 'washington']:
        print('which city do you like to see? please select Chicago, New_York_City, or Washington?')
        city = input().lower()
    return eval(city)


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function
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

    return month, day

def popular_month(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What month occurs most often in the start time?
    '''
    # TODO: complete function
    month_count = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        month_count[month] =  month_count.get(month, 0) + 1
    
    #popular_month_value, popular_month_count = max(zip(month_count.values(),month_count.keys()))
    #print(popular_month_value, popular_month_count)
    
    #print(month_count)
    sorted_month_count = sorted(month_count.items(), key=lambda x:x[1], reverse=True)
    #print(sorted_month_count)
    return sorted_month_count[0]

def popular_day(city_file, month_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    '''
    # TODO: complete function
    day_count = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        if month_period == 'all' or month == month_period:
            day = start_time.strftime('%A')
            day_count[day] = day_count.get(day, 0) + 1
    sorted_day_count = sorted(day_count.items(), key=lambda x:x[1], reverse=True)
    return sorted_day_count[0]

def is_filter_work(month_period, day_period, month, day):
    if month_period != 'all' and day_period != 'all':
        if month == month_period and day == day_period:
           return True;
    elif month_period != 'all' and day_period == 'all':
        if month == month_period:
            return True;
    elif month_period == 'all' and day_period != 'all':
        if day == day_period:
            return True
    elif month_period == 'all' and day_period == 'all':
        return True
    else:
        return False

def popular_hour(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What hour of the day (0, 2, ... 22, 23) occurs most often in the start time?
    '''
    # TODO: complete function
    hour_count = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        hour = start_time.time().hour
        if is_filter_work(month_period, day_period, month, day):
            hour_count[hour] = hour_count.get(hour, 0) + 1
    sorted_hour_count = sorted(hour_count.items(), key=lambda x:x[1], reverse=True)
    popular_hour_result = sorted_hour_count[0]
    print('most often hour is:', popular_hour_result[0], ', count is:', popular_hour_result[1])


def trip_duration(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    total_trip_duration = 0
    total_count = 0
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        if is_filter_work(month_period, day_period, month, day):
            total_trip_duration += int(item['Trip Duration'])
            total_count += 1
        
    print('Total trip duration is:', total_trip_duration)
    print('Average trip duration is:', round(total_trip_duration/total_count, 2))


def popular_stations(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    '''
    # TODO: complete function
    popular_start_stations = {}
    popular_end_stations = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        if is_filter_work(month_period, day_period, month, day):
            popular_start_stations[item['Start Station']] = popular_start_stations.get(item['Start Station'], 0) + 1
            popular_end_stations[item['End Station']] = popular_end_stations.get(item['End Station'], 0) + 1
    
    popular_start_station_count, popular_start_station = max(zip(popular_start_stations.values(), popular_start_stations.keys()))
    popular_end_station_count, popular_end_station = max(zip(popular_end_stations.values(), popular_end_stations.keys()))
    print('most frequently used start station is:', popular_start_station, ',count is:', popular_start_station_count)
    print('most frequently used end station is:', popular_end_station, ',count is:', popular_end_station_count)

def popular_trip(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
    '''
    # TODO: complete function
    popular_start_end_trip = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        item['Start End Trip'] = item['Start Station'] + ' ' + item['End Station']
        if is_filter_work(month_period, day_period, month, day):
            popular_start_end_trip[item['Start End Trip']] = popular_start_end_trip.get(item['Start End Trip'], 0) + 1
    
    popular_start_end_station_count, popular_start_end_station = max(zip(popular_start_end_trip.values(), popular_start_end_trip.keys()))
    print('most frequently used start station is:', popular_start_end_station, ',count is:', popular_start_end_station_count)

def users(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    use_type = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        if is_filter_work(month_period, day_period, month, day):
            use_type[item['User Type']] = use_type.get(item['User Type'], 0) + 1
    print(use_type)
    

def gender(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    gender_count = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        if is_filter_work(month_period, day_period, month, day):
            gender_count[item['Gender']] = gender_count.get(item['Gender'], 0) + 1
    print(gender_count)


def birth_years(city_file, month_period, day_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    '''
    # TODO: complete function
    birth_year_count = {}
    for item in city_file:
        start_time = datetime.strptime(item['Start Time'], '%Y-%m-%d %H:%M:%S')
        month = start_time.date().month
        day = start_time.strftime('%A')
        if item['Birth Year'] and is_filter_work(month_period, day_period, month, day):
            birth_year_count[item['Birth Year']] = birth_year_count.get(item['Birth Year'], 0) + 1

    earliest_birth_year, earliest_birth_year_count = min(zip(birth_year_count.keys(), birth_year_count.values()))
    recent_birth_year, recent_birth_year_count = max(zip(birth_year_count.keys(), birth_year_count.values()))
    common_birth_year_count, common_birth_year = max(zip(birth_year_count.values(), birth_year_count.keys()))
    print('oldest person born year:', earliest_birth_year, ',count is:', earliest_birth_year_count)
    print('most recent birth year:', recent_birth_year, ',count is:', recent_birth_year_count)
    print('most common birth year:', common_birth_year, ', count is :', common_birth_year_count)

def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    count = 0 
    while display.lower() == 'yes':
        print(city_file[count * 5: (count + 1) * 5])
        count += 1

        display = input('\nWould you like to continuing...?'
                    'Type \'yes\' or \'no\'.\n')



def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    #print('city filename is:', city)

    with open(city) as f:
        city_file = [
            {k: v for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)
        ]
    print(type(city_file))

    # Filter by time period (month, day, none)
    month, day = get_time_period()
    #print(month, day)

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if month == 'all':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        most_popular_month = popular_month(city_file)
        print('Most popular month is:', most_popular_month[0], ' number is:', most_popular_month[1])

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if day == 'all':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        most_popular_day = popular_day(city_file, month)
        print('Most popular day is:', most_popular_day[0], ', number is:', most_popular_day[1])

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(city_file, month, day)
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
