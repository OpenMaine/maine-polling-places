# p-polling
Polling place location map for Maine

Project is currently functional but incomplete.

# Methodology
Polling locations were downloaded in batch using wget to the scrape the About Maine Maps service, https://www.maine.gov/cgi-bin/gmaps/map.pl?show=poll . Each request would include a JavaScript function that would create a Google Maps marker. Each function for every town was cut from each request and output into a central file. This file was then run against a python script to output a JSON file. 

Last pull from Maine's server was 20 September 2018.

# About the map
The map uses tiles from Stamen Design and the underlying mapping library is leaflet. There is a search function located at the top-right of the map that can perform a limited polling location search. It is tied only to the polling location names themselves, while you can enter a town name not all towns will appear.

# Todo
1. Add a town selection section on the right or left of the map to reduce the number of marker icons required.
2. Modify the search results to poll against the town or city versus the polling location name.
3. Explore using geocoding to point users to their polling location
