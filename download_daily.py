#!usr/bin/python

#we are using openexchangerates.org to get daily data
#App ID: b16fd2804c9743458a08a0f89d740c44

import urllib2
import json
from datetime import date, timedelta as td
import time


start_date = date(1999,01,01)
current_date = time.strftime('%x')
current_month, current_date, current_year = current_date.split('/')
current_year = '20' + current_year
end_date = date(int(current_year), int(current_month), int(current_date))

base_url = 'http://openexchangerates.org/api/historical/'
app_id = 'app_id=b16fd2804c9743458a08a0f89d740c44'

date_list = []
delta = end_date - start_date
for i in range(delta.days + 1):
    temp_date = start_date + td(days=i)
    date_list.append(str(temp_date))
    
#write data to file
f = open('daily_data', 'w')
for date in date_list:
    url = base_url + date + '.json?' + app_id
    response = urllib2.urlopen(url)
    data = json.load(response)
    required_value = data['rates']['JPY']
    f.write(date + ' ')
    f.write(str(required_value))
    f.write('\r\n')
f.close()