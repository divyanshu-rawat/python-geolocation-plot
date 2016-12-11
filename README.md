> Build :innocent: using  Google Geocoding :joy: API for Visualizing data on Google Map. :mag:

### Description 

* In this project, we are using the Google geocoding API to clean up some user-entered  geographic locations of 
  university names and then placing the data on a Google Map. (Where.data contains user-entered Data !).
 
### Installation Instructions :grey_exclamation:

* clone or download the repo. into any fresh temporary folder.

* cd into that root folder you just cloned locally.

* if you want to enter user defined data then please enter it in where.data file just add the name of the place,institution     you want to visualize on the map.

* Run geoload.py to  Query Data written in where.data using Google API !.

* Run geodump.py to read the data from the database so you can visualize it on a map.

* Open where.html to view the data in a browser.

### How it Works !

* In the first phase we take our input data in the file (where.data) and read it one line at a time, and retreive the
  geocoded response and store it in a database (geodata.sqlite).Before we use the geocoding API, we simply check to see 
  if we already have the data for that particular line of input.You can re-start the process at any time by removing the file
  geodata.sqlite.
  
* Run the geoload.py program.This program will read the input lines in where.data and for each line check to see if it is       already in the database and if we don't have the data for the location,call the geocoding API to retrieve the data and       store it in the database.

* The geoload.py can be stopped at any time, and there is a counter that you can use to limit the number of calls to the       geocoding API for each run.Once you have some data loaded into geodata.sqlite, you can visualize the data using the           (geodump.py) program.  This program reads the database and writes tile file (where.js) with the location, latitude, and       longitude in the form of executable JavaScript code. 

* A run of the geodump.py program records written to where.js Open where.html to view the data in a browser The file           (where.html) consists of HTML and JavaScript to visualize a Google Map.  It reads the most recent data in where.js to get 
  the data to be visualize.
  
* This is a JavaScript list of lists.  The syntax for JavaScript list constants is very similar to Python so the syntax         should be familiar to you. 

* Simply open where.html in a browser to see the locations.  You can hover over each map pin to find the location that the     gecoding API returned for the user-entered input.  If you cannot see any data when you open the where.html file, you might 
  want to check the JavaScript or developer console for your browser.


* I have attached screenshots below depicting various features of  applicationIn the first phase we take our input data in the file (where.data) and read it one line at a time, and retreive the



### Examples !

![alt tag](https://github.com/divyanshu-rawat/Retrieving_Processing_and_Visualizing_Data_with_Python./blob/master/screenshot/map.png)


