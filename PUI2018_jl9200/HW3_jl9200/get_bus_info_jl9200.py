
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



## input will be "get_bus_info.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv"

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]


# user the json.loads to obtain a dictionary representation of the response string


#print (url)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)



# filename will be sys.argv[3]

def bus_status_info_csv():          
    with open(sys.argv[3],'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
        # Number of bus
        Num_bus = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
        if Num_bus == 0:
            row = str('No Data')
            writer.writerow([row])
        else:
            for i in range(Num_bus):        
                bus_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
                bus_lon = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
                checkEmpty = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']
                if len(checkEmpty) == 0:
                    Stop_Name = "N/A"
                    Stop_Status = "N/A"
                else:  
                    Stop_Name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                    Stop_Status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

                # need to convert as str
                row = str(bus_lat),str(bus_lon),str(Stop_Name),str(Stop_Status)
                writer.writerow(row)



# Test if the route exist

# test incase the bus route didn't exist
try:  
    test = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    bus_status_info_csv()
except KeyError:
    print('No such route')  

