#!/usr/bin/env python3

import re

import json

place_name_re = re.compile("drop_select=([^:]+):")
lat_long_re = re.compile(r"([0-9-.]+)")
in_single_quotes_re = re.compile("'([^']+)'")

polling = {}

current_place = {}

current_location = {}

f = open('output.txt', 'r')

for line in f:
    line = line.strip()
    if line.startswith('function createMarker'):
        name = place_name_re.search(line).group(1)
        current_place = {'proper': name, 'locations': []}
        polling[name.lower()] = current_place
    if line.startswith('var latitude ='):
        current_location['latitude'] = lat_long_re.search(line).group(1)
    if line.startswith('var longitude = '):
        current_location['longitude'] = lat_long_re.search(line).group(1)
    if line.startswith('var name ='):
        current_location['address'] = in_single_quotes_re.search(line).group(1)
    if line.startswith('var in_msg ='):
        in_html = in_single_quotes_re.search(line).group(1)
        end_pos = in_html.find('</strong>')
        start_pos = in_html.find('<strong>') + 8
        current_location['name'] = in_html[start_pos:end_pos]
    if line.startswith('gmarkers[') and line.endswith('].setMap(map);'):
        current_place['locations'].append(current_location)
        current_location = {}

root = { 'polling' : polling }
print(json.dumps(root, indent = 4))
