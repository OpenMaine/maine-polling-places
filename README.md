# p-polling
Polling place location map for Maine

Project is currently functional but incomplete. Polling locations through the towns of Abbott-Cranberry Isles are loaded as of 7 Oct 2018.

# How you can help

The output.txr file is an extracted JavaScript function across the State of Maine's database for each town. Extracted output looks like the following:

   function createMarker map.pl?show=poll&drop_select=Crawford:function addMarkers()
      {
              
              
                var latitude = '45.19845';
                var longitude = '-69.191895';
                var in_msg = 'Geographic location could not be found for: <br /><br /><strong>Crawford Town Hall</strong><br />3190 Airline Road<br />Crawford, ME 04694<br /><a href="javascript:closerLook(0)">Take a closer look</a><br />';
                var out_msg = 'Geographic location could not be found for: <br /><br /><strong>Crawford Town Hall</strong><br />3190 Airline Road<br />Crawford, ME 04694<br /><a href="javascript:widerLook(0)">Take a wider look</a><br />';
                var point = new google.maps.LatLng(latitude,longitude);
                var name = '3190 Airline Road, Crawford, ME 04694';
                var marker = createMarker(point,in_msg);
                gmarkers[0] = marker;
                gpoints[0] = point;
                in_msgs[0] = in_msg;
                in_msgs_dir[0] = in_msg + '<br /><br />Start address:<form action="javascript:getDirections()"><input type="text" SIZE=40 MAXLENGTH=40 name="saddr" id="saddr" value="" /><br ><INPUT value="Get Directions" TYPE="SUBMIT"><input type="hidden" id="daddr" name="daddr" value="'+name+"@"+ latitude + ',' + longitude + '"/>';
                out_msgs[0] = out_msg;
                out_msgs_dir[0] = out_msg + '<br /><br />Start address:<form action="javascript:getDirections()"><input type="text" SIZE=40 MAXLENGTH=40 name="saddr" id="saddr" value="" /><br ><INPUT value="Get Directions" TYPE="SUBMIT"><input type="hidden" id="daddr" name="daddr" value="'+name+"@"+ latitude + ',' + longitude + '"/>';
                gmarkers[0].setMap(map);
              
              
              
   }
   
The latitude and longitude are extracted from the same variable names that you see in the output above. The address is can be found in the name variable. The actually facility name is located in the in_msg or out_msg variable. It doesn't matter whcih in or out variable you use, it holds the same information. These four pieces of information then need to be entered into another file named polling.json . Let's take out some of the information from the extracted JavaScript above first though.

Latitude = 45.19845 
Longitude = -69.191895
Address = 3190 Airline Road, Crawford, ME 04694
Name = Crawford Town Hall

** WARNING: If the in_msg or out_msg states "Geographic location could not be found" then you will need to manually search for the latitude and longitude of the polling location. Generally this happens in towns that share polling locations. In this case Crawford doesn't have its town hall displayed in Google Maps so the location can't be found and the lat/lon are bogus. To fix it, use Google Maps to load the address and use the lat/lon in the address bar... https://www.google.com/maps/place/3190+Airline+Rd,+Crawford,+ME+04694/@45.0554612,-67.5524257,767m ... latitude = 45.0554612 and longitude = -67.5524257 .

So we want Crawford to actually look like this:

Latitude = 45.0554612 
Longitude = -67.5524257
Address = 3190 Airline Road, Crawford, ME 04694
Name = Crawford Town Hall

Next we want to plug this information into the polling.json file. Here is an extract of city with multiple locations:

	"augusta": {
      "proper": "Augusta",
      "locations": [
        {
          "latitude": "44.316584",
          "longitude": "-69.770559",
          "address": "16 Cony Street, Augusta, ME 04330",
          "name": "Augusta City Hall"
        },
		{
		  "latitude": "44.318905",
		  "longitude": "-69.7978526",
		  "address": "76 Community Drive, Augusta, ME 04330",
		  "name": "Augusta Civic Center"
		},
		{
		  "latitude": "44.3121892",
		  "longitude": "-69.7969601",
		  "address": "22 Armory Street, Augusta, ME 04330",
		  "name": "Buker Community Center"
		},
		{
		  "latitude": "44.3125354",
		  "longitude": "-69.7480711",
		  "address": "60 Pierce Drive, Augusta, ME 04330",
		  "name": "Cony High School"
		}
      ]
    },
	
In this case, you can see that we can plug what we extracted from the output.txt file into this file rather nicely. Let's show you what Crawford would look like:

	"crawford": {
      "proper": "Crawford",
      "locations": [
        {
          "latitude": "45.0554612",
          "longitude": "-67.5524257",
          "address": "3190 Airline Road, Crawford, ME 04694",
          "name": "Crawford Town Hall"
        }
      ]
    },

Notice the removal of the comma after one location. Too many commas in this case can be bad because the code is looking for another location if the comma remained and will break the map.

# About the map
The map uses tiles from Stamen Design and the underlying mapping library is leaflet. There is a search function located at the top-right of the map that can perform a limited polling location search. It is tied only to the polling location names themselves, while you can enter a town name not all towns will appear.

# Todo
1. Add a town selection section on the right or left of the map to reduce the number of marker icons required.
2. Modify the search results to poll against the town or city versus the polling location name.