# PUI2018 Homework 3

### Assignments:


#### Assignment_1. Peform the instruction in deleteData.md: delete data and its history from a GitHub rep
In terminal

![rm fromterminal](https://user-images.githubusercontent.com/31417181/46114484-de2a5d00-c1c0-11e8-9c78-e953dabfbca7.JPG)


GitHub

![repohistory](https://user-images.githubusercontent.com/31417181/46114855-7d038900-c1c2-11e8-9678-5226bf040b49.JPG)


#### Assignment_2. Choose a file in CSV format from NYC Open Data and use pandas to read the file and mangle the data within it.

I choose the data about [Incidents Responded to by Fire Companies](https://data.cityofnewyork.us/Public-Safety/Incidents-Responded-to-by-Fire-Companies/tm6d-hbzd/data)


please see notebook HW3_2_jl9200

#### Assignment_3.  tracking each vehicle for a line

type code as below in terminal:

python show_bus_locations_jl9200,py <MTA_KEY> <BUS_LINE>

For example if you choose M15, the code should be:

python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx M15


Output:

Bus Line :M15
Number of Active Buses : 16
Bus 0 is at latitude 40.781508 and longitude -73.949086
Bus 1 is at latitude 40.711049 and longitude -74.000432
Bus 2 is at latitude 40.764562 and longitude -73.958373
Bus 3 is at latitude 40.744846 and longitude -73.975851
Bus 4 is at latitude 40.75323 and longitude -73.96973
Bus 5 is at latitude 40.738454 and longitude -73.980496
Bus 6 is at latitude 40.764409 and longitude -73.961557
Bus 7 is at latitude 40.762501 and longitude -73.962955
Bus 8 is at latitude 40.744264 and longitude -73.973152
Bus 9 is at latitude 40.724063 and longitude -73.987875
Bus 10 is at latitude 40.735519 and longitude -73.98257
Bus 11 is at latitude 40.753674 and longitude -73.966287
Bus 12 is at latitude 40.800438 and longitude -73.935252
Bus 13 is at latitude 40.796793 and longitude -73.934824
Bus 14 is at latitude 40.711283 and longitude -73.992364
Bus 15 is at latitude 40.787552 and longitude -73.941576


#### Assignment_4.  next stop information

type code as below in terminal:

python get_bus_info_jl9200,py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv



For example if you choose M15, the code should be:

python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx M15

output to a csv file named <BUS_LINE>.csv as beloow:

Latitude,Longitude,Stop Name,Stop Status
40.803068,-73.93222,E 126 ST/2 AV,at stop
40.731078,-73.98586,2 AV/E 12 ST,approaching
40.705185,-74.00738,WATER ST/GOUVERNEUR LA,approaching
40.731269,-73.982632,1 AV/E 14 ST,approaching
40.799345,-73.932971,1 AV/PALADINO AV,approaching
40.738674,-73.980344,2 AV/E 23 ST,approaching
40.771444,-73.953321,1 AV/E 79 ST,< 1 stop away
40.731977,-73.9852,2 AV/E 12 ST,< 1 stop away
40.776256,-73.952912,2 AV/E 82 ST,< 1 stop away
40.758735,-73.965722,2 AV/E 54 ST,< 1 stop away
40.760018,-73.961664,1 AV/E 62 ST,< 1 stop away
40.794585,-73.939538,2 AV/E 110 ST,< 1 stop away
40.751893,-73.967494,1 AV/MITCHELL PL,< 1 stop away
40.75154,-73.970967,2 AV/E 42 ST,< 1 stop away
40.75685,-73.967089,2 AV/E 50 ST,< 1 stop away
40.729805,-73.983691,1 AV/E 14 ST,< 1 stop away

I also add the feature for error input, such as if you input M6, which it is not exist it will return like below:

![nosuchroute](https://user-images.githubusercontent.com/31417181/46114874-a3292900-c1c2-11e8-9a82-90eb61da859a.JPG)


Meanwhile, if the Json data 'OnwardCalls' is empty I output the "Stop Name", and "Stop Status" as "N/A" like below:

![na](https://user-images.githubusercontent.com/31417181/46114900-ba681680-c1c2-11e8-9235-8745ca2cfc2c.JPG)










