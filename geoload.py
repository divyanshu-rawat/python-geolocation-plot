import urllib
import sqlite3
import json
import time
import ssl

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"                                    #base service url.

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

conn = sqlite3.connect('geodata.sqlite')                     # making an connection basically now going to make an connection to
                                                             # an sqlite3 database stored in a file named geodata.sqlite
cur = conn.cursor()                                         # cursor is basically a sub-conection inside that.

# calling a method inside of cur or cursor to execute a bit of sql
# we are basically saying hey ! just create a table if it doesn't EXISTS Name the table Loccations and put colous in it address,geodata!!
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")

count = 0
for line in fh:
    if count > 200 : break  #we are basically saying that we will take 200 at a time!!!
    address = line.strip()
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (buffer(address), ))
    #buffer is a way to force address onto the address coloumn.
    #what it does is that it searches for geodata coloumn database looks down where address ? first time we don't have it because we
    #just made a table.
    try:
        data = cur.fetchone()[0]
        # fetchone is the method that fetches one row row ends up being a list so we want fetch zero item i.e -geodata
        # get the first coloumn and bring it back in data.if that doesn't exist we are going to except which says pass!!!
        # basically data will store either NULL(if it doesn't exist) otherwise (geodata(value), )
        # if we are reading things that are in the database then the process is effeciently fast.
        print "Found in database ",address
        continue
    except:
        pass

    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)                                                     #opening the url
    data = uh.read()                                                             #reading the data in the url!!
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1
    try:
        js = json.loads(str(data))
        #print js  # We print in case unicode causes an error
    except:
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print '==== Failure To Retrieve ===='
        print data
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
          VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    conn.commit()
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can visualize it on a map."
