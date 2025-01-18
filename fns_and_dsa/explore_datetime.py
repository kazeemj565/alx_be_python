from datetime import datetime, timedelta
from datetime import date

# local_datetime = datetime.now()
# print(local_datetime)


# two_hurricanes_dates = [date(2020, 8, 27), date(2020, 9, 14)]
# print(two_hurricanes_dates)


def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)


display_current_datetime()

def calculate_future_date():
    future_date = datetime.now() + timedelta(days=40)
    future_date = future_date.strftime("%Y-%m-%d")


calculate_future_date()