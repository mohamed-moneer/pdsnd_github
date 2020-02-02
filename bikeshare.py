import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Paris': 'Paris.csv',
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
    # TO DO: get user input for city (paris, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city=input('\nWhich city would you like to filter by? New York City, Chicago or Washington?\n')
            lowered_c = city.lower()
            if  lowered_c not in ('new york city', 'paris', 'washington'):
                print('Sorry, I couldn\'t catch that. Try Again')
                continue
            else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
        lowered_m = month.lower()
        if lowered_m not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Sorry, I couldn\'t catch that. Try Again')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
        lowered_d = day.lower()
        if lowered_d not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("Sorry, I didn't catch that. Try again.")
            continue
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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        months=['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index+1
        df = df[df['month']== month]
   # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('Most Common day:', popular_month)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Common hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station=df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station=df.groupby(['Start Station','End_Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time=sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")
    # TO DO: display mean travel time
    Mean_Travel_Time=df['Travel Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Type=df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_types=df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
        print('\nGender Types:\nNo data available for this month.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year=df['Birth Year'].min()
        print('\nEarliest Year:',Earliest_Year)
    except KeyError:
        print('\nEarlist Year:\nNo data available for this month.')

    try:
        Most_Recent_Year=df['Birth Year'].max()
        print('\nMost Recent Year:',Most_Recent_Year)
    except KeyError:
        print('\nMost Recent Year:\nNo data available for this month.')
    try:
        Popular_Year=df['Birth Year'].value_counts().idxmax
        print('\nPopular Year:',Most_Common_Year)
    except KeyError:
        print('\nPopular Year:\nNo data available for this month.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows

    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        raw_data=('yes or no')
        if raw_data.lower()=='yes':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n Displaying rows {} to {}:'.format(row_start+1,row_end+1))
            print('\n', df.iloc[row_start : row_end+1])
            row_start+=show_rows
            row_end+=show_rows

            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
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
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()