# plot_elevation.py
from skyfield.api import load, EarthSatellite, wgs84
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ---------------------------
# 1 Load satellite TLE and observer
# ---------------------------
ts = load.timescale()

# Example NOAA 19 TLE (replace with real TLEs from CelesTrak later)
line1 = "1 33591U 09005A   24001.12345678  .00000023  00000+0  34567-4 0  9991"
line2 = "2 33591  99.1945  12.3456 0012345 123.4567 234.5678 14.12456789123456"

sat = EarthSatellite(line1, line2, "NOAA 19", ts)

# Observer location (example: New York City)
observer = wgs84.latlon(40.7128, -74.0060)

# ---------------------------
# 2 Predict all passes in the next 24 hours
# ---------------------------
t0 = ts.now()
t1 = ts.now() + timedelta(hours=24)

t_events, events = sat.find_events(observer, t0, t1, altitude_degrees=0.0)

# Extract all complete passes
passes = []
rise_time = None
for t, event in zip(t_events, events):
    if event == 0:  # rise
        rise_time = t
    elif event == 2 and rise_time is not None:  # set
        set_time = t
        passes.append((rise_time, set_time))
        rise_time = None

if not passes:
    raise RuntimeError("No complete passes found in the next 24 hours.")

# ---------------------------
# 3 Plot each pass with elevation & signal strength
# ---------------------------
plt.figure(figsize=(10,5))

for i, (rise, set_) in enumerate(passes, start=1):
    # Sample times every 10 seconds
    duration_seconds = int((set_.utc_datetime() - rise.utc_datetime()).total_seconds())
    times_pass = ts.utc(
        rise.utc_datetime() + np.array([timedelta(seconds=s) for s in range(0, duration_seconds, 10)])
    )
    
    # Compute elevation
    elevation_pass = (sat.at(times_pass) - observer.at(times_pass)).altaz()[0].degrees
    
    # Compute approximate signal strength (sin of elevation, scaled to y-axis)
    signal_strength = np.sin(np.radians(elevation_pass)) * 90
    
    # UTC times for x-axis
    utc_times_pass = [t.utc_datetime() for t in times_pass]
    
    # Plot elevation curve
    plt.plot(utc_times_pass, elevation_pass, label=f'Pass {i} Start {rise.utc_strftime("%H:%M")}')
    
    # Plot signal strength overlay (dashed)
    plt.plot(utc_times_pass, signal_strength, '--', label=f'Signal (Pass {i})')
    
    # Annotate max elevation
    max_idx = np.argmax(elevation_pass)
    plt.text(utc_times_pass[max_idx], elevation_pass[max_idx]+5, f'Max {int(elevation_pass[max_idx])}°',
             ha='center', color='blue')

# ---------------------------
# 4 Format plot
# ---------------------------
plt.xlabel("UTC Time")
plt.ylabel("Elevation Angle (degrees)")
plt.title("NOAA Satellite Passes and Predicted Signal Strength")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

