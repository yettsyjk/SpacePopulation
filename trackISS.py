from geopy.distance import geodesic
import request, json, geocoder, time

def callStation():
    lat = (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude']
    long = (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude']
    gLocation = geocoder.osm([lat, long], method = 'reverse')
    print(("Target acquired, tracking active: the location of the ISS is {}, {}.".format(lat, long))), print("Landmarks the station is visible from: ", gLocation.country)
    print("See location: ", "http://www.google.com/maps/place/{},{}".format(lat, long))
    lastKnown = (lat, long)
    return lastKnown
def callDistance(lastKnown, currentKnown):
    print("ISS has traveled at approx ", geodesic(lastKnown, currentKnown).miles, "miles inm 10 seconds.")