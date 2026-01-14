import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skyfield.api import load, EarthSatellite, wgs84, utc
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# -------------------------------
# Observation start (UTC)
# -------------------------------
observation_start = datetime(2026, 1, 12, 15, 9, 7, tzinfo=utc)

# -------------------------------
# Load CW peak times (seconds from start)
# -------------------------------
pulse_times = np.loadtxt(
    "decoding/cw_peak_times.csv",
    skiprows=1
)

# Convert CW pulses to UTC datetimes
pulse_datetimes = [
    observation_start + timedelta(seconds=t)
    for t in pulse_times
]

# -------------------------------
# Load CW amplitude CSV
# -------------------------------
amp_df = pd.read_csv("decoding/cw_amplitude.csv")

# Convert time offsets to UTC datetimes
amp_times = [observation_start + timedelta(seconds=t) for t in amp_df['time']]
amplitudes = amp_df['amplitude']

# -------------------------------
# Satellite TLE (placeholder)
# -------------------------------
tle_line1 = "1 27848U 03031E   26012.42300000  .00000023  00000-0  12345-4 0  9991"
tle_line2 = "2 27848 098.1234 045.6789 0012345 123.4567 234.5678 14.23456789123456"
satellite = EarthSatellite(tle_line1, tle_line2, "XI-IV", load.timescale())

# -------------------------------
# Ground station (placeholder)
# -------------------------------
ground_station = wgs84.latlon(latitude_degrees=0.0, longitude_degrees=0.0)

# -------------------------------
# Time grid for elevation
# -------------------------------
times = [observation_start + timedelta(seconds=i) for i in range(0, 600)]  # 10-min window
ts = load.timescale()
sf_times = ts.from_datetimes(times)

# Compute satellite elevation
difference = satellite - ground_station
topocentric = difference.at(sf_times)
elevation = topocentric.altaz()[0].degrees

# -------------------------------
# Plotting
# -------------------------------
fig, ax1 = plt.subplots(figsize=(12,5))

# Elevation curve (left y-axis)
ax1.plot(times, elevation, color='blue', linewidth=2, label='Elevation (deg)')
ax1.set_xlabel('Time (UTC)', fontsize=12)
ax1.set_ylabel('Elevation (deg)', color='blue', fontsize=12)
ax1.set_ylim(-90, 90)
ax1.tick_params(axis='y', labelcolor='blue')

# CW pulses as red X’s
pulse_elevations = np.interp(
    [t.timestamp() for t in pulse_datetimes],
    [t.timestamp() for t in times],
    elevation
)
ax1.scatter(
    pulse_datetimes,
    pulse_elevations,
    color='red',
    s=80,
    marker='x',
    label='CW Pulses',
    zorder=5
)

# Amplitude curve (right y-axis)
ax2 = ax1.twinx()
ax2.plot(amp_times, amplitudes, color='green', linewidth=1.5, label='Amplitude')
ax2.set_ylabel('Amplitude', color='green', fontsize=12)
ax2.tick_params(axis='y', labelcolor='green')

# Format x-axis nicely
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
fig.autofmt_xdate()

# Grid, title, legend
ax1.grid(True)
plt.title('CubeSat Elevation vs Time with CW Pulses and Amplitude', fontsize=14)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

plt.tight_layout()
plt.show()

