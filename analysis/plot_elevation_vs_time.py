import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skyfield.api import load, EarthSatellite, wgs84, utc
from datetime import datetime, timedelta



# -------------------------------
# Load CW pulse times
# -------------------------------
pulse_times = np.loadtxt(
    "decoding/cw_peak_times.csv",
    skiprows=1
)

# -------------------------------
# Define observation start time
# (from SatNOGS observation page)
# -------------------------------
observation_start = datetime(2026, 1, 12, 15, 9, 7, tzinfo=utc)



# Convert pulse offsets → UTC datetimes
pulse_datetimes = [
    observation_start + timedelta(seconds=t)
    for t in pulse_times
]

# -------------------------------
# Load satellite TLE
# (example — replace later if needed)
# -------------------------------
tle_line1 = "1 27848U 03031E   26012.42300000  .00000023  00000-0  12345-4 0  9991"
tle_line2 = "2 27848 098.1234 045.6789 0012345 123.4567 234.5678 14.23456789123456"

satellite = EarthSatellite(
    tle_line1,
    tle_line2,
    "XI-IV",
    load.timescale()
)

# -------------------------------
# Ground station location
# (use SatNOGS station later)
# -------------------------------
ground_station = wgs84.latlon(
    latitude_degrees=0.0,
    longitude_degrees=0.0
)

# -------------------------------
# Time grid for pass
# -------------------------------
times = [
    observation_start + timedelta(seconds=i)
    for i in range(0, 600)
]

ts = load.timescale()
sf_times = ts.from_datetimes(times)

# -------------------------------
# Compute elevation
# -------------------------------
difference = satellite - ground_station
topocentric = difference.at(sf_times)
elevation = topocentric.altaz()[0].degrees

# -------------------------------
# Plot
# -------------------------------
plt.figure(figsize=(10, 4))
plt.plot(times, elevation, label="Satellite Elevation")

# Overlay pulse times
pulse_elevations = np.interp(
    [t.timestamp() for t in pulse_datetimes],
    [t.timestamp() for t in times],
    elevation
)

plt.scatter(
    pulse_datetimes,
    pulse_elevations,
    color="red",
    label="CW Pulses",
    zorder=5
)

plt.xlabel("Time (UTC)")
plt.ylabel("Elevation (degrees)")
plt.title("Satellite Elevation vs Time with CW Pulses")
plt.legend()
plt.tight_layout()
plt.show()
