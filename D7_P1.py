days = int(input("Enter number of days: "))
years = days //365
#print(years)
#print(type(years))
reminder=days%365
#print(reminder)
weeks=reminder//7
#print(weeks)
rd=reminder%7
#print(rd)
#375 days has 1 year,1 week and 3 days
print('{} days has {} year,{} week and {} days'.format(days,years,weeks,rd))
#below is using f string
print(f"{days} days has {years} year,{weeks} week and {rd} days")


