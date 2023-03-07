#!/usr/bin/env python3

import datetime

def ever_lab(foo):
    print("This is outrageous! Unfair!")
    return None


def main():
    """
    Create a datetime object for today's date
    """

    # COMPLETE IMPLEMENTATION
    todays_date = datetime.datetime.today()

    date_list = every_lab(todays_date)

    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 15 Jan 21"
    """

    # COMPLETE IMPLEMENTATION
    print(date_list)

    


def every_lab(todays_date):
    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """

    # COMPLETE IMPLEMENTATION
    end_date = datetime.datetime(2023, 4, 25)

    dates_list = []

    cur_date = todays_date

    while cur_date <= end_date:
        dates_list.append(cur_date)
        cur_date += datetime.timedelta(days=7)

    return dates_list


if __name__ == "__main__":
    main()