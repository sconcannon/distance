#! python3
# lat_long.py adds latitude and longitude to origin point for all RMBS 2019 attendees

import csv
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import urllib.request
import json
import time
import urllib.parse
timestr = time.strftime("%Y%m%d-%H%M%S")

# open data and transform to list
travel_data_file = open('data/190526_rbms_full.csv')
travel_data_read = csv.reader(travel_data_file)
travel_data = list(travel_data_read)

# start geocoders
geolocator = Nominatim(user_agent='rbms_distance')

# settings
destination = 'Baltimore, MD'
destination_latitude = 39.2908816
destination_longitude = -76.610759
destination_coords = (destination_latitude, destination_longitude)

# results file
timestr = time.strftime("%Y%m%d-%H%M%S")
result_filename = 'data/190526_rbms_output' + timestr + '.csv'
resultFile = open(result_filename, 'w', newline='')
resultWriter = csv.writer(resultFile)

for line in travel_data:
    # if no destination, skip lookup
    if line[3] == '':
        new_line = line
    else:
        # get latlong
        # make origin for Nominatim
        origin = line[3] + ", " + line[4]
        origin_geocoded = geolocator.geocode(origin)

        # add lat & long miles to results
        new_line = line
        new_line.append(origin_geocoded.latitude)
        new_line.append(origin_geocoded.longitude)
        print(origin)

    resultWriter.writerow(new_line)

# save list as csv
resultFile.close()