# CubeSat Data Pipeline Project

## Project Overview
This project demonstrates a low-cost system for retrieving, decoding, and visualizing data from CubeSats. Our system processes satellite recordings, decodes the signals, and visualizes the data alongside predicted satellite passes.

**Key Focus Areas:**
- Retrieving CubeSat recordings (from public databases or SDR hardware)
- Decoding signals into meaningful data (images or telemetry)
- Displaying results clearly for analysis
- Comparing results to CubeSat reference data (done by another teammate)

> Note: NOAA APT signals are no longer publicly available, so we are focusing on CubeSat data.


## Repository Structure

---

## Workflow Overview

1. **Retrieve Data**
   - Download CubeSat recordings from SatNOGS or capture with hardware (RTL-SDR + antenna).
   - Store recordings in `data/raw/`.

2. **Decode Data**
   - Convert recordings into images or telemetry using decoding tools or Python scripts.
   - Save outputs in `data/decoded/`.

3. **Analyze & Visualize**
   - Use Python scripts to plot:
     - Satellite elevation vs time
     - Signal strength
     - Decoded telemetry or reconstructed images
   - Organize plots and images for comparison.

4. **Compare**
   - Another teammate compares decoded data to CubeSat reference data.
   - Insights and summaries are generated from this comparison.

---

## Notes

- `.gitignore` ensures large files (raw recordings, decoded images) are **not pushed to GitHub**.
- All Python scripts are designed to work on local machines using VS Code.
- All satellite predictions use public TLEs from [CelesTrak](https://www.celestrak.com/NORAD/elements/).



