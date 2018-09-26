
from __future__ import print_function
import requests
import json
import sys
import csv

# import urllib2 or urllib

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib



## input will be "python show_bus_locations.py <MTA_KEY> <BUS_LINE>"

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]


# user the json.loads to obtain a dictionary representation of the response string


#print (url)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Test if the route exist


    
#print (Num_buses)
def bus_locations_info():
    
    Num_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    print ("Bus Line :" + sys.argv[2])
    print ("Number of Active Buses : "+ str(Num_buses))
    for i in range(Num_buses):
        bus_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        bus_lon = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print ("Bus "+ str(i) +" is at" +" latitude " +str(bus_lat) +" and longitude "+str(bus_lon))

try:  
    test = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    bus_locations_info()
except KeyError:
    print('No such route')        


