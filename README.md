# distance
## Summary
distance takes a list of UAS city/state and Canada city/province pairs and calculates the distance in miles from each location to a single destination. This data would help an organizer at the destination calculate the environmental impact of travel to the destination. This script was written to assist the organizers of a conference in 2018. 
* lat_long.py turns the city/state or city/province pairs into latitude/longitude pairs, using Mominatim from geopy.geocoders
* distance uses the latitude/longitude pairs to calculate distance using the Google Maps Distance Matrix api

