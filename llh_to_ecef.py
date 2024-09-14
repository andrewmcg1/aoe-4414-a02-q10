# llh_to_ecef.py
#
# Usage: python3 ecef_to_llh.py r_x_km r_y_km r_z_km
#  Converts ECEF vector components to LLH
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
#  lat_deg: Latitude component in degrees
#  lon_deg: Longitude component in degrees
#  hae_km: Height above the ellipsoid in km
# Output:
#  Prints 
#
# Written by Andrew McGrellis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions

## calculated denominator
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
lat_deg = float('nan') # Latitude component in degrees
lon_deg = float('nan') # Longitude component in degrees
hae_km = float('nan') # Height above the ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
   'Usage: '\
   'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
  exit()

# write script below this line

# convert degrees to radians
lat_rad = math.radians(lat_deg)
lon_rad = math.radians(lon_deg)

c_e = R_E_KM / calc_denom(E_E, lat_rad)
s_e = c_e * (1.0 - E_E**2)

r_x_km = (c_e + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y_km = (c_e + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z_km = (s_e + hae_km) * math.sin(lat_rad)

print(r_x_km)
print(r_y_km)
print(r_z_km)