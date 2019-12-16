import requests
import csv

## Using Python 3.6
## Before using this script: 
##		pip install requests

## Before using the data, read the license here. https://climate.weather.gc.ca/prods_servs/attachment1_e.html
## Historical weather and climate change data can be found here: https://climate.weather.gc.ca/index_e.html

## How to find station numbers can be found here: 
## https://zhiqiangyu.wordpress.com/ecreader-environment-canada-climate-data-reader/

start_year 	= 1972
end_year 	= 2019
weather_station = "4816" 		## Make sure this is in quotes.

def download_data(start_year, end_year, weather_station):
	for year in range (start_year, end_year+1):
		#print (i)
		url = 'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='+weather_station+'&Year='+str(year)+'&Month=12&Day=14&timeframe=2&submit=Download+Data'
		print (url)
		# ~ url = 'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=4816&Year=2018&Month=12&Day=14&timeframe=2&submit=Download+Data'
		
		myfile = requests.get(url)
		save_file = str(year)+".csv"
		open(save_file, 'wb').write(myfile.content)

def clean_data(start_year, end_year):
	## With Thanks to Martijn Pieters https://stackoverflow.com/users/100297/martijn-pieters
	## https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
	
	flag = 1		## If the flag = 1 then headers are added, otherwise they are not.
	
	# for year in range
	# after the first year, set the flag to 0.	
	with open("2017.csv", "r") as infile, open("data.csv", "a", newline='\n') as outfile:
	   reader = csv.reader(infile)
	   if flag != 1: 
		   next(reader, None)  # skip the headers
	   writer = csv.writer(outfile)
	   for row in reader:
		   # process each row
		   writer.writerow(row)
       
#download_data(start_year, end_year)
clean_data(start_year, end_year)
