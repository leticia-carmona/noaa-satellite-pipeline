# CubeSat Radio Signal Processing Pipeline

This project implements an end-to-end pipeline for retrieving, decoding, and analyzing radio signals transmitted by CubeSats. The system processes real satellite radio-frequency data obtained from publicly available ground-station recordings and converts it into interpretable visualizations tied to satellite orbital geometry.

The project is designed to operate without hardware initially, using recorded passes, while remaining fully compatible with future live reception using an SDR and antenna.

---

## Project Objectives

- Retrieve real CubeSat signal recordings from public ground stations
- Convert raw RF/audio data into a usable digital format
- Decode continuous-wave (CW) style transmissions
- Extract and analyze signal strength over time
- Relate signal behavior to satellite elevation and orbital position
- Visualize results in a clear, engineering-focused manner

---

## System Pipeline

Satellite Transmission  
↓  
Ground Station Recording (SatNOGS)  
↓  
Raw Audio File (.ogg)  
↓  
Audio Conversion (.wav)  
↓  
Signal Decoding (CW amplitude extraction)  
↓  
Event Detection & Time-Series Analysis  
↓  
Orbital Geometry Computation  
↓  
Visualization & Interpretation  

---

## Repository Structure
data/
├── raw/ # Original downloaded satellite recordings
├── processed/ # Converted WAV files used for decoding
decoding/
├── decode_cw.py # Extracts CW signal amplitude
├── cw_amplitude.csv # Time vs amplitude data
├── cw_peak_times.csv # Detected signal events
analysis/
├── plot_elevation_vs_time.py
├── plot_elevation_with_amplitude.py
docs/ # Figures, explanations, final report
README.md
---

## Current Capabilities
- ✔ Download CubeSat recordings from SatNOGS
- ✔ Convert recordings to WAV format
- ✔ Decode CW-style transmissions
- ✔ Detect signal pulses
- ✔ Compute satellite elevation vs time
- ✔ Overlay signal behavior with orbital geometry

---

## Tools & Libraries
- Python 3
- NumPy, SciPy
- Pandas
- Matplotlib
- Skyfield
- FFmpeg
- SatNOGS Open Data

---

## Project Status
**Active development**

Current focus:
- Improving signal-to-orbit alignment
- Refining decoding thresholds
- Preparing visual results for presentation

Planned extensions:
- Live SDR reception
- Hardware validation
- Automated pass scheduling

---

## Team Roles
- **Hardware**: Antenna, SDR setup, RF reception
- **Signal Processing & Visualization**: Decoding, plotting, interpretation
- **Data Comparison**: Cross-checking decoded data with CubeSat telemetry

---

## Disclaimer
This project only listens to publicly available satellite transmissions.  
No communication, control, or interference with spacecraft occurs.
