import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ["chicago","new york city","washington"]
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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

    while True:
        city = input("Please choose a city (chicago, new york city or washington)\n:-")
        if city in cities:
            break
        else:
          print("**invalid city or capital letters used**")


    # get user input for month (all, january, february, ... , june)

    while True:
        month=input("Please choose a month (january,february,march,april,may,june) or all\n:-")
        if month in months:
            break
        elif month == 'all':
            break
        else:
            print("**invalid month or capital letters used**")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Please choose a day (saturday,sunday,monday,tuesday,wednesday,thursday,friday) or all\n:-")
        if day in days:
            break
        elif day == 'all':
            break
        else:
            print("**invalid month or capital letters used**")

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
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    # filter by month to create the new dataframe
    df["month"]=df["Start Time"].dt.month
    # filter by day of week to create the new dataframe
    df["day_of_week"]=df["Start Time"].dt.day_name()

    if month !="all":
        months=["january","february","march","april","may","june"]
        month=months.index(month)+1
        df=df[df["month"]== month]

    if day !="all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is :\n{}".format(df["month"].mode()))


    # display the most common day of week
    print("Tho most common day of week is :\n{}".format(df["day_of_week"].mode()))

    # extract hour from the Start Time column to create an hour column
    df["start hour"] = df["Start Time"].dt.hour

    # display the most common start hour
    print("The most common start hour is:\n{}".format(df["start hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most start station used is:\n{}".format(df["Start Station"].mode()))


    # display most commonly used end station
    print("The most end station used is:\n{}".format(df["End Station"].mode()))


    # display most frequent combination of start station and end station trip
    df["frequent"]=df["Start Station"]+df["End Station"]
    print("The most frequent combination is:\n{}".format(df["frequent"].mode()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is:\n",df["Trip Duration"].sum())


    # display mean travel time
    print("The average travel time is:\n",df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts())


    # Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("No Data for this city")

    # Display earliest, most recent, and most common year of birth
    if  'Gender' in df.columns:
        print("The earliest year of birth is: \n",df["Birth Year"].min())
        print("The most recent year of birth is:\n ", df["Birth Year"].max())
        print("The common year of birth is: \n", df["Birth Year"].mode())

    else:
        print("No Data fot this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    iteration = 0
    row = 'first'
    loc = 0
    while True:
        data = input('\nWould you like to see the {} five rows of the data? Enter yes or no.\n'.format(row))
        if data.lower() != 'yes':
            break
        else:
            print('\nLoading Data')
            start_time = time.time()

            data = df.iloc[loc: loc+5]
            print('\nThe five rows are:\n{}'.format(data))
            loc += 5
            iteration += 1
            if iteration >= 1:
                row = 'next'
                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-' * 40)


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
