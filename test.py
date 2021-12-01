from geopy.distance import geodesic
from haversine import haversine

print(geodesic().nm)
dis = haversine((30.28708, 120.12802999999997), (28.7427, 115.86572000000001))
print(dis)
