# Low-Cost NOAA Satellite Reception Pipeline

## Overview
This project designs and validates a low-cost system to receive, decode,
and visualize NOAA weather satellite transmissions using software-defined
radio (SDR). The system integrates orbital prediction, signal decoding,
data analysis, and visualization into a single end-to-end pipeline.

At the current stage, the project focuses on software, orbital mechanics,
and data processing using publicly available NOAA APT recordings.
Live RF reception will be integrated once hardware is available.

## Motivation
Weather satellites continuously broadcast valuable Earth observation data.
This project explores whether such data can be accessed and interpreted
using low-cost, commercially available hardware and open-source software.

The goal is not satellite communication, but passive reception and
interpretation of real satellite signals.

## Project Goals
- Predict NOAA satellite passes using publicly available TLE data
- Decode APT (Automatic Picture Transmission) signals into Earth images
- Analyze signal and image quality relative to satellite geometry
- Visualize satellite orbits and ground tracks
- Integrate all components into a clear, reproducible pipeline

## System Architecture
Satellite Orbit  
→ Pass Prediction  
→ Signal Capture (future hardware)  
→ Signal Decoding  
→ Data Analysis  
→ Visualization  

## Current Status
- Hardware: Not yet integrated
- Signal Source: Public NOAA APT recordings
- Orbit Prediction: In progress
- Decoding Pipeline: In progress
- Visualization: Planned

## Tools & Technologies
- Python
  - skyfield / sgp4 (orbit prediction)
  - numpy, pandas (analysis)
  - matplotlib, folium / plotly (visualization)
- SatDump / noaa-apt (signal decoding)
- Public NOAA satellite data
- Planned hardware: RTL-SDR + V-dipole antenna

## What This Project Is NOT
- Not transmitting to satellites
- Not controlling satellites
- Not collecting classified data
- Not implementing DSP algorithms from scratch

## Next Steps
- Implement satellite pass prediction for a fixed ground location
- Decode sample NOAA APT recordings into images
- Plot satellite elevation vs time during passes
- Visualize satellite ground tracks corresponding to decoded data

## Future Work
- Integrate RTL-SDR hardware
- Record live NOAA satellite passes
- Compare predicted vs actual reception windows
- Evaluate antenna orientation and signal quality
