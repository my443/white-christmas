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
## weather_station = "48569"	## Kitchener/ Waterloo Station that starts in 2010

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

	## Reset the data file.
	f = open("data.csv", "w")
	f.close()
		
	flag = 1					## If the flag = 1 then headers are added, otherwise they are not.

	for data_file in range(start_year, end_year + 1):
		fn = str(data_file) + ".csv"	
		with open(fn, "r") as infile, open("data.csv", "a", newline='\n') as outfile:
		   reader = csv.reader(infile)
		   
		   if flag == 0: 
			   next(reader, None)  	## skip the headers
			
		   flag = 0					## Set the flag to 0. You only need one header.
			   
		   writer = csv.writer(outfile)
		   for row in reader:
			   # process each row
			   writer.writerow(row)
		
		print ("Processing File . . ."+fn)
	
	print ("\nData saved to  . . . data.csv")
	infile.close()
		

	 
def get_christmas_row(start_year, end_year):
	## Reset the data file.
	f = open("christmas-data.csv", "w")
	f.close()
	
	with open("data.csv", "r") as infile, open("christmas-data.csv", "w", newline = "\n") as outfile: 
		reader = csv.reader(infile)
		writer = csv.writer(outfile)
		
		## Add the header to the new file.
		header = next(reader)
		writer.writerow(header)
		
		## Add all of the other rows.
		for row in reader:
			if row[6] == "12" and row[7] == "24":
				writer.writerow(row)
       
	print ("\nData saved to  . . . christmas-data.csv")
	

## Download the data	
download_data(start_year, end_year)

## Clean it and put it into one spreadsheet.
clean_data(start_year, end_year)

## Filter the consolidated sheet by December 24th.
get_christmas_row(start_year, end_year)

