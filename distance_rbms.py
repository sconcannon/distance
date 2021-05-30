#! python3
# distance_rbms.py calculates distances traveled for all RMBS 2019 attendees

import csv
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import urllib.request
import json
import time
import urllib.parse
timestr = time.strftime("%Y%m%d-%H%M%S")

# open data and transform to list
travel_data_file = open('data/190525_rbms_full.csv')
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
result_filename = 'data/190525_rbms_output' + timestr + '.csv'
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
        #  calculate distance from geopy.distance
        origin_coords = (origin_geocoded.latitude, origin_geocoded.longitude)
        distance_miles_air = vincenty(origin_coords, destination_coords).miles

        # add air miles to results
        new_line = line
        new_line.append(distance_miles_air)

        if line[6] in ('US','Canada'):
            # TODO if ground, get miles from Google Maps Distance Matrix API
            # make origin for Distance Matrix API
            origin = urllib.parse.quote(line[3] + "+" + line[4])
            distance_matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" \
                                  + origin +"&destinations=baltimore+md&key=" + [insert_api_key]
            res = urllib.request.urlopen(distance_matrix_url).read()
            data = json.loads(res.decode())
            distance_meters = data["rows"][0]["elements"][0]["distance"]["value"]
            distance_miles_ground = distance_meters * 0.00062137

            # add ground miles to results
            new_line.append(distance_miles_ground)

    resultWriter.writerow(new_line)

# save list as csv
resultFile.close()