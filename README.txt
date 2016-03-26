
Language Used-python.
API Used- Google Geocoding.

Using the Google Geocoding API with a Database and Visualizing data on Google Map.
In this project, we are using the Google geocoding API to clean up some user-entered  geographic locations of 
university names and then placing the data on a Google Map.

The first problem to solve is that the Google geocoding API is rate limited to 2500 requests per day.  
So if you have a lot of data you might need to stop and restart the lookup process several times.  So we break the problem into two
phases.  

In the first phase we take our input data in the file (where.data) and read it one line at a time, and retreive the
geocoded response and store it in a database (geodata.sqlite).Before we use the geocoding API, we simply check to see 
if we already have the data for that particular line of input.You can re-start the process at any time by removing the file
geodata.sqlite.
Run the geoload.py program.This program will read the input lines in where.data and for each line check to see if it is already
in the database and if we don't have the data for the location,call the geocoding API to retrieve the data and store it in 
the database.
The geoload.py can be stopped at any time, and there is a counter that you can use to limit the number of calls to the geocoding
API for each run.
Once you have some data loaded into geodata.sqlite, you can visualize the data using the (geodump.py) program.  This
program reads the database and writes tile file (where.js) with the location, latitude, and longitude in the form of
executable JavaScript code.   

A run of the geodump.py program records written to where.js Open where.html to view the data in a browser
The file (where.html) consists of HTML and JavaScript to visualize a Google Map.  It reads the most recent data in where.js to get 
the data to be visualized.  

This is a JavaScript list of lists.  The syntax for JavaScript list constants is very similar to Python so the syntax should 
be familiar to you.

Simply open where.html in a browser to see the locations.  You can hover over each map pin to find the location that the 
gecoding API returned for the user-entered input.  If you cannot see any data when you open the where.html file, you might 
want to check the JavaScript or developer console for your browser.


