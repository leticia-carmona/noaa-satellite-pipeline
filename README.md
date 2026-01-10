# NOAA Satellite Data Processing & Visualization Pipeline

## Project Overview

This project builds a complete software pipeline for working with Earth observation data from NOAA weather satellites. The focus is on:

- **Predicting satellite passes**
- **Decoding publicly available NOAA APT recordings**
- **Analyzing and visualizing the decoded data**
- **Connecting image data to satellite geometry**

This project *does not* require any hardware to begin — all work uses publicly archived satellite recordings and open data sources.

## Motivation

NOAA weather satellites broadcast images of Earth using the Automatic Picture Transmission (APT) protocol. These signals are publicly accessible, and with the right tools we can decode, analyze, and visualize Earth imagery — all with software. This project demonstrates how to build that pipeline end-to-end.

## System Architecture

## What’s Included

- `pass_prediction/`: Scripts that compute satellite passes and elevation vs. time.
- `decoding/`: Scripts and tools to decode audio files into NOAA images.
- `analysis/`: Tools to analyze decoded images and link them to orbital data.
- `visualization/`: Plots and maps tying passes to image data.
- `data/`: Public recordings and decoded image outputs.

## Current Status

- Hardware integration (RTL-SDR) is optional and *not required* for this project phase.
- Sample NOAA APT recordings will be stored in `data/raw/`.
- Decoded images will be stored in `data/decoded/`.

## Tools & Dependencies

- Python (Skyfield, NumPy, Matplotlib)
- NOAA APT decoding tools (e.g., `noaa-apt`, Python decoders like `apt-decoder`) :contentReference[oaicite:0]{index=0}
- Example WAV audio recordings from public sources

## How to Decode NOAA APT Recordings

1. Place a `.wav` file containing an APT satellite audio recording in `data/raw/`
2. Use a decoder (Python script or tool) to convert it into an image
3. Store output in `data/decoded/`
4. Analyze images with scripts in `analysis/`

## Next Steps

- Download a NOAA APT sample recording
- Decode it using the tools in `decoding/`
- Annotate the decoded images with predicted pass geometry

## What This Project Is *Not*

- Not transmitting to satellites
- Not controlling satellites
- Not requiring real hardware for initial progress



