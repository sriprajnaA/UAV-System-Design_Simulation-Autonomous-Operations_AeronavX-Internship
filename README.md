# AeroNavX
### Autonomous Drone Design, Navigation & AI Vision System

> **Unlox Drone Engineering Program — Major Project**
> Built and simulated on Linux Mint 22 using ArduPilot SITL, DroneKit-Python, and OpenCV.

---

## Project Overview

AeroNavX is a fully autonomous quadcopter simulation system covering the complete UAV engineering stack — from mechanical frame design and power system engineering to Python-based autonomous flight programming and AI-driven computer vision.

The project replicates the workflow of a modern UAV R&D team and was developed as part of the **Unlox Drone Engineering Program (April 2026)**.

---

## What It Does

-  **Autonomous takeoff, waypoint navigation, and landing** via DroneKit-Python
-  **Real-time obstacle detection and avoidance** using OpenCV
-  **Vision-based precision landing** using color pad detection
-  **Complete SITL simulation** with ArduPilot on Linux
-  **Flight logs captured** from every simulation session
-  **DGCA/FAA compliant** with geo-fence and failsafe configuration

---

## Demo

> Add your screenshots to a `screenshots/` folder in this repo after uploading.

| Mission Flight | Obstacle Detection | Vision Landing |
|---|---|---|
| ![Mission](![alt text](image-2.png)) | ![Obstacle](![alt text](image.png)) | ![Landing](![alt text](image-1.png)) |

---

## Tech Stack

| Category | Tools |
|---|---|
| Simulation | ArduPilot SITL, MAVProxy |
| Autonomous Programming | DroneKit-Python, pymavlink |
| Computer Vision | OpenCV (cv2), NumPy |
| Flight Controller | Pixhawk 2.4.8 + ArduCopter firmware |
| CAD Design | Fusion 360 |
| OS / Platform | Linux Mint 22 (Ubuntu 24.04 base) |
| Language | Python 3.12 |

---

## Setup & Installation

### Prerequisites

- Linux (Ubuntu 20.04 / 22.04 / 24.04 or Linux Mint equivalent)
- Python 3.x
- Git

### 1. Clone ArduPilot & Install SITL

```bash
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
git submodule update --init --recursive
Tools/environment_install/install-prereqs-ubuntu.sh -y
. ~/.profile
```

### 2. Set Up Python Environment

```bash
python3 -m venv droneenv
source ~/droneenv/bin/activate
pip install dronekit pymavlink opencv-python numpy matplotlib future
```

### 3. Patch DroneKit for Python 3.12

```bash
sed -i 's/collections.MutableMapping/collections.abc.MutableMapping/g' \
  ~/droneenv/lib/python3.12/site-packages/dronekit/__init__.py
```

### 4. Clone This Repo

```bash
git clone https://github.com/YOUR_USERNAME/AeroNavX.git
cd AeroNavX
```

---

## Running the Simulation

### Step 1 — Start SITL (Terminal 1)

```bash
cd ~/ardupilot
. ~/.profile
sim_vehicle.py -v ArduCopter --console
```

Wait for `pre-arm good` in the MAVProxy console.

### Step 2 — Run Autonomous Mission (Terminal 2)

```bash
source ~/droneenv/bin/activate
cd AeroNavX/code
python3 mission.py
```

**Expected output:**
```
Connecting to drone...
Arming motors...
Taking off...
Altitude: 0.0m → 19.5m
Target altitude reached!
Navigating waypoints...
Going to waypoint 1... 2... 3... 4...
Returning to launch...
Mission complete!
```

### Step 3 — Run Obstacle Detection

```bash
python3 obstacle_avoidance.py
```

Detects red obstacles via webcam or test image. Press `Q` to quit.

### Step 4 — Run Vision Landing

```bash
python3 vision_landing.py
```

Detects green landing pad, calculates alignment error, and issues correction commands.

---

## Module Summary

| # | Module | Status |
|---|---|---|
| 1 | Drone Frame Design (Fusion 360 CAD) |  Complete |
| 2 | Power & Propulsion Engineering |  Complete |
| 3 | Flight Controller Setup & Calibration |  Complete |
| 4 | Autonomous Flight Programming (DroneKit) |  Complete |
| 5 | Obstacle Detection & Avoidance (OpenCV) |  Complete |
| 6 | Vision-Based Landing System |  Complete |
| 7 | Airspace Compliance & Geo-Fencing |  Complete |
| 8 | Final Integrated Simulation Flight | Complete |

---

## Drone Specifications

| Parameter | Value |
|---|---|
| Frame | X-Quadcopter, 450mm motor-to-motor |
| Motors | EMAX 2216 KV880 (×4) |
| ESCs | Hobbywing XRotor 30A OPTO (×4) |
| Propellers | APC 10×4.5 GFN (2× CW + 2× CCW) |
| Battery | Tattu 4S 5200mAh 45C LiPo |
| Flight Controller | Pixhawk 2.4.8 + ArduCopter |
| Total Thrust | 3400g |
| All-Up Weight | ~1450g |
| Thrust-to-Weight Ratio | **2.34 : 1** |
| Estimated Flight Time | ~14 minutes |

---

## Safety & Compliance

- DGCA (India) regulations followed — max 120m AGL, VLOS, 5km airport exclusion
- ArduPilot geo-fence: 100m altitude max, 150m radius, RTL on breach
- Battery failsafe at 3.5V/cell (RTL) and 3.3V/cell (immediate land)
- RC loss, GPS loss, and GCS loss failsafes configured

---

## Known Issues & Fixes

| Issue | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'past'` | `pip install future` |
| `AttributeError: collections has no attribute MutableMapping` | Patch dronekit with `sed` command (see setup above) |
| `sim_vehicle.py: command not found` | Run `. ~/.profile` to reload PATH |

---

## License

This project was built for educational purposes as part of the Unlox Drone Engineering Program.

---

*Built from scratch. Flown autonomously. Documented completely.*
