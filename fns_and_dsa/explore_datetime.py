from datetime import datetime,timedelta
current_date = datetime.now()
def display_current_datetime():
  return f" Current date and time:{current_date.strftime("%Y-%m-%d %H:%M:%S")}"
display_current_datetime(current_date)
number_of_days=int(input("Enter the number of days to add to the current date:"))
future_date= current_date + timedelta(days=number_of_days)
def calculate_future_date():
  return f"Future date:{future_date.strftime("%Y-%m-%d %H:%M:%S")}"
calculate_future_date( future_date)
