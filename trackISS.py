# Using Python requests and the Google Maps Geocoding API.
#
# References:
#
# * http://docs.python-requests.org/en/latest/
# * https://developers.google.com/maps/
from geopy.distance import geodesic
import requests, json, geocoder, time

def callStation():
    lat = (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude']
    long = (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude']
    gLocation = geocoder.osm([lat, long], method = 'reverse')
    print(("Target acquired, tracking active: the location of the ISS is {}, {}.".format(lat, long))), print("Landmarks the station is visible from: ", gLocation.country)
    print("See location: ", "http://www.google.com/maps/place/{},{}".format(lat, long))
    lastKnown = (lat, long)
    return lastKnown

def callDistance(lastKnown, currentKnown):
    print("ISS has traveled at approx ", geodesic(lastKnown, currentKnown).miles, "miles in 10 seconds.")
    return lastKnown

def calcDistance(firstKnown, currentKnown):
    print("The ISS is traveling at approx ", geodesic(firstKnown, currentKnown).miles, "miles per minute.")
    mile_hour = (int(geodesic(firstKnown, currentKnown).miles) * 60)
    print("The ISS is traveling at approx ", mile_hour, " miles per hour.\n>>>discontinuing tracking>>>")

data = (requests.get("http://api.open-notify.org/astros.json")).json();print("Data request : ", (data['message'])),print("Total humans in orbit: ", data['number'],"\nPrinting manifest: ")
for i in range(len(data['people'])):
    print(("%s is currently in space aboard the %s." % ((data['people'][i]['name']), (data['people'][i]['craft']))))
for i in range(6):
    if i < 1:
        lastKnown = callStation()
        firstKnown = lastKnown
        time.sleep(10)
    elif i < 5:
        currentKnown = callStation()
        lastKnown = callDistance(lastKnown, currentKnown)
        time.sleep(10)

    elif i == 5:
        print("FINAL ROUND: ")
        currentKnown = callStation()
        calcDistance(firstKnown, currentKnown)