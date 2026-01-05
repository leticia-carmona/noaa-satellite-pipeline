from skyfield.api import load, EarthSatellite, wgs84
from datetime import timedelta

# 1. Load time scale
ts = load.timescale()

# 2. Load NOAA 19 TLE (example)
line1 = "1 33591U 09005A   24001.12345678  .00000023  00000+0  34567-4 0  9991"
line2 = "2 33591  99.1945  12.3456 0012345 123.4567 234.5678 14.12456789123456"

satellite = EarthSatellite(line1, line2, "NOAA 19", ts)

# 3. Define your location (example: New York City)
observer = wgs84.latlon(40.7128, -74.0060)

# 4. Choose start time and duration
t0 = ts.now()
t1 = ts.now() + timedelta(hours=24)

# 5. Step through time and find passes
t, events = satellite.find_events(observer, t0, t1, altitude_degrees=0.0)

print("Upcoming passes:")
for ti, event in zip(t, events):
    if event == 0:
        print("Pass starts:", ti.utc_strftime())
    elif event == 1:
        print("Max elevation:", ti.utc_strftime())
    elif event == 2:
        print("Pass ends:", ti.utc_strftime())
