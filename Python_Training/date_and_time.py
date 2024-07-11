import datetime
from datetime import time, timedelta
import time
#import pendulum


# now = datetime.datetime.now()
# now.strftime("%Y-%m-%d %H:%M%S")
# print(f"Current date and time : {now}")

today = datetime.date.today()
new_year = datetime.date(2024, 5, 13)
#print(today)
#print(new_year)

day_delta = datetime.timedelta(days=1)

# start_date = datetime.date.today()
# end_date =  start_date - 5*day_delta
# print(end_date)
# for i in range((end_date - start_date).days):
#     print(start_date + i*day_delta)

# start_date = datetime.date.today()
# for x in range(0,6):
#     print(start_date - datetime.timedelta(days=x))


# for i in range(0,5):
#     print(start_date + datetime.timedelta(days=i))   

#unix timestamp: identifies date and time of an occurance, data can be accurate to milli-seconds (number of seconds in a digital form)

#convert a unix timestamp string to a readable date

time_stamp = datetime.datetime.fromtimestamp(int("1614983421"))
time_stamp.strftime("%Y-%m-%d %H:%M%S")
print(f"The date and time is : {time_stamp}")  

#current time rounded to the nearest milli-second
milli_sec = int(round(time.time() * 1000))
print(milli_sec)


#Code to find a date of the 1st Monday of a given week (2024)
#struct_time converts given time to seconds, type of time in 

time.struct_time

#asc converts a time tuple to a string
#strptime: parse a string to a time tuple according to a format specification
print(time.asctime(time.strptime("2024 10 1", "%Y %W %w")))  #Y = year, W = week, w = week day

#Code to select all the Sundays in a specified year

def all_sundays(year):
    day_time = datetime.date(year,1,1)
    day_time +=timedelta(days = 6-day_time.weekday())
    

    #iterateb through all Sundays of the given year
    while day_time.year == year:
        #yield current date as a result, produces value, retains it and continues
        yield day_time
        #add 7 days to move to next Sunday
        day_time += timedelta(days=7)

        
year = 2023    
all_sundays(year)
for i in all_sundays(year):
    print(i)

def add_years(d,years):
    #return day of current year with year adjusted 
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d + (datetime.date(d.year+years, 1,1)-datetime.date(d.year,1,1))
    
#adding -1 years to Jan 1st    
print(add_years(datetime.date(2020,1,1),-1))
#adding 0 years to Jan 1st
print(add_years(datetime.date(2020,1,1),0))
#adding 2 years to Jan 1st
print(add_years(datetime.date(2020,1,1),2))
#Adding 1 year to Feb 29th
print(add_years(datetime.date(2020,2,29),1))


#display previous 4 years

#Calculate the number of days between 2 days
# Create function which Calculate the difference in days between 2 days

def diff_days(date_1, date_2):
    a =date_1
    b = date_2
    return (a-b).days

print()
print(diff_days((datetime.date(2023,12,5)), datetime.date(2024,2,4)))
print()

date_d = ((datetime.date(2023,12,5)) - (datetime.date(2024,2,4)))
print(date_d)

print()
print((time.ctime()))
print() 

# pendulum: provides a cleaner and more concise interface then the standard date and time module
#get current date and time

# current_datetime = pendulum.now()
# print(current_datetime)

# formattde_datetime = current_datetime.format("YYYY-MM-DD HH:mm:ss")


#Write a code to add 5 seconds to current time
x = datetime.datetime.now()
# add the timedelt of 5 seconds to current date and time
y = x + datetime.timedelta(0.5)
print(x.time())
print(y.time())
