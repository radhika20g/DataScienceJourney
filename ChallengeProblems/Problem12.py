'''
Problem Statement - Inbuilt Libraries
Write a Python program that calculates the remaining days, hours, and minutes until the event. Additionally, provide the percentage completion of the event based on the current time compared to the event's start time.
'''

from datetime import datetime, timedelta
import math

event_date = datetime(2024, 3, 20, 16, 45)  # March 20, 2024, 04:45 PM
current_datetime = datetime.now()

time_difference = event_date - current_datetime
remaining_days = time_difference.days
remaining_hours, remaining_seconds = divmod(time_difference.seconds, 3600)
remaining_minutes = remaining_seconds // 60

# Calculate percentage completion
total_seconds_in_event = (event_date - event_date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
elapsed_seconds = (current_datetime - event_date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
percentage_completion = (elapsed_seconds / total_seconds_in_event) * 100


print(f"Remaining time until the event: {remaining_days} days, {remaining_hours} hours, {remaining_minutes} minutes.")
print(f"Percentage completion of the event: {math.floor(percentage_completion)}%")