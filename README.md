# 📡 SmartWiFi

AI-Based Wi-Fi Performance Prediction & Channel Optimization System

## Overview

SmartWiFi is a wireless network analytics platform that performs real-time Wi-Fi discovery, channel congestion analysis, interference scoring, and intelligent channel recommendation using live wireless environment data.

The system scans nearby Wi-Fi networks, analyzes channel utilization and signal strength, and recommends the optimal Wi-Fi channel to minimize interference and improve network performance.

---

## Features

- Real-time Wi-Fi network scanning
- SSID and BSSID discovery
- Signal strength (RSSI) analysis
- Channel occupancy analysis
- Interference score calculation
- Intelligent channel recommendation
- Network health assessment
- Interactive Flask dashboard

---

## Tech Stack

### Backend
- Python
- Flask

### Networking
- Windows WLAN (`netsh`)
- Wi-Fi Channel Analysis
- Wireless Signal Analytics

### Data Processing
- Pandas

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Machine Learning (Planned)
- Scikit-Learn
- Random Forest

---

## Project Architecture

```text
Wi-Fi Scanner
      ↓
Network Parser
      ↓
Channel Analyzer
      ↓
Interference Engine
      ↓
Recommendation Engine
      ↓
Analytics Dashboard
      ↓
AI Prediction Module
```

---

## Dashboard Features

### Nearby Networks
Displays:
- SSID
- Signal Strength
- Channel
- Radio Type

### Channel Analysis
Provides:
- Number of networks per channel
- Total signal strength
- Interference score

### Smart Recommendation
Recommends the optimal Wi-Fi channel based on:
- Congestion
- Signal interference
- Non-overlapping channel selection

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/SmartWiFi.git
cd SmartWiFi
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Current Status

### Completed
- Real-time Wi-Fi scanning
- Network parsing
- Channel analysis
- Interference scoring
- Recommendation engine
- Flask dashboard

### Upcoming
- Channel overlap analysis
- AI-based network quality prediction
- Historical analytics
- Performance forecasting
- PDF reporting

---

## Sample Output

Recommended Channel: 11

Reason:
Channel 11 has the lowest congestion and interference score among preferred non-overlapping Wi-Fi channels.

---

## Learning Outcomes

This project demonstrates practical knowledge of:

- Computer Networking
- Wireless Communications
- Wi-Fi Technologies
- Network Analytics
- Flask Development
- AI-driven Optimization

---

## Author

**Sri Chaitanya Varma**

Computer Science Engineer | AI & Networking Enthusiast
