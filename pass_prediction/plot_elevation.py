from skyfield.api import load, EarthSatellite, wgs84
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt

# 1. Load time scale
ts = load.timescale()

# 2. NOAA 19 TLE (example — will update later)
line1 = "1 33591U 09005A   24001.12345678  .00000023  00000+0  34567-4 0  9991"
line2 = "2 33591  99.1945  12.3456 0012345 123.4567 234.5678 14.12456789123456"

sat = EarthSatellite(line1, line2, "NOAA 19", ts)

# 3. Observer location (change to your city later)
observer = wgs84.latlon(40.7128, -74.0060)

# 4. Find the next pass
t0 = ts.now()
t1 = ts.now() + timedelta(hours=24)

t_events, events = sat.find_events(observer, t0, t1, altitude_degrees=0.0)

# Find the first complete pass
rise_time = None
set_time = None

for t, event in zip(t_events, events):
    if event == 0 and rise_time is None:
        rise_time = t
    elif event == 2 and rise_time is not None:
        set_time = t
        break

if rise_time is None or set_time is None:
    raise RuntimeError("No complete pass found.")

# 5. Sample times during the pass (every 10 seconds)
duration_seconds = int((set_time.utc_datetime() - rise_time.utc_datetime()).total_seconds())
times = ts.utc(
    rise_time.utc_datetime() + np.array([timedelta(seconds=s) for s in range(0, duration_seconds, 10)])
)

# 6. Compute elevation angles
difference = sat.at(times) - observer.at(times)
topocentric = difference.altaz()
elevation = topocentric[0].degrees

# 7. Plot
plt.figure()
plt.plot(range(len(elevation)), elevation)
plt.xlabel("Time steps (10 s each)")
plt.ylabel("Elevation angle (degrees)")
plt.title("NOAA Satellite Elevation vs Time")
plt.grid(True)
plt.show()
