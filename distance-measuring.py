import math

def deg2rad(deg):
    return deg * ((math.pi) / 180)
def getDistance(lat1, lng1, lat2, lng2):
    earthRadius = 6371000 #as meter
    dLat = deg2rad(lat2 - lat1) #delta Lat
    dLng = deg2rad(lng2 - lng1) #delta Lng
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLng / 2) * math.sin(dLng / 2) # The main formule of distance of points
    c =  2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) # formule is continue.
    dist = earthRadius * c # main distance 
    return dist

lat1 = input("Latitude 1: ")
lng1 = input("Longitude 1: ")
lat2 = input("Latitude 2: ")
lng2 = input("Longitude 2: ")
distance = round(getDistance(lat1, lng1, lat2, lng2), 2) #39.901058, 32.796729, 39.902182, 32.797222
print str(distance) + " m"