import numpy as np

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"
raw = np.loadtxt(URL, delimiter=",", usecols=[6, 7, 8], skiprows=1) 

week_one_tmax = raw[0:7, 0]
week_one_tmin = raw[0:7, 1]
week_one_prcp = raw[0:7, 2]
week_two_tmax = raw[7:14, 0]

print("Week 1 TMAX: ", week_one_tmax)
print("Week 1 TMIN: ", week_one_tmin)
print("Week 1 PRCP: ", week_one_prcp)

print("Size of Week 1 TMAX: ", len(week_one_tmax))
print("Alt Size of Week 1 TMAX: ", week_one_tmax.shape)

print("TMAX / 0: ", week_one_tmax/0)