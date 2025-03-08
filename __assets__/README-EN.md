<!-- video -->
<p align="center">
  <video src="Demo.mp4" controls></video>
</p>

<!-- tag line -->
<h1 align='center'>Dynamic Traffic Signal Control System</h1>

<!-- primary badges -------------------------------------->
<p align="center">
  <img src='https://img.shields.io/badge/license-MIT-blue.svg' />
  <img src='https://img.shields.io/badge/Python-3.x-blue' />
  <img src='https://img.shields.io/badge/Pygame-2.x-green' />
  <img src='https://img.shields.io/badge/WebSocket-Server-yellow' />
</p>

<p align="center">
    <a href="../README.md">繁體中文版本</a>
</p>

## Project Overview
This project is the intersection simulation subsystem of the "Dynamic Traffic Signal Control System," developed as a project for the "System Analysis and Design" course at National Yunlin University of Science and Technology.

The simulator uses Pygame to create a virtual intersection environment and communicates in real-time with a Java core via WebSocket. The project aims to address the limitations of existing traffic signal control systems by developing a smarter, dynamic traffic control solution.

> [!NOTE]
> Interested in the Java core? Check out [this project](https://github.com/liwayne58/SA_DynamicSmartTrfficSignalCS)! <br>
> Interested in System Analysis and Design documents? Check out [Documents](/__assets__/Documents/)!

### Background
- Most current traffic signal systems rely on fixed timers.
- They cannot adapt to real-time traffic flow changes.
- This leads to traffic congestion, delays, and environmental pollution.

### Solution
This system adopts an innovative approach:
- A dynamic traffic controller based on computer vision.
- Calculates traffic density using CCTV or government database imagery.
- Detects vehicle numbers and types (cars, motorcycles, ambulances, etc.) in real-time.
- Dynamically adjusts green light durations.
- Prioritizes emergency vehicles and congested directions.

> [!Important]
> To demonstrate the project, Pygame is used to simulate traffic road congestion, with Python directly sending road traffic data to the Java core.

## Feature List
1. **Traffic Simulation**
   - Simulates road traffic flow using Pygame.
   - Supports multiple vehicle types.
   - Displays real-time traffic signal status.

2. **Real-Time Communication**
   - WebSocket server.
   - Real-time data exchange with the Java core.

3. **Simulation Control**
   - Multi-lane management.
   - Vehicle generation control.
   - Traffic signal timing control.
   - Traffic flow statistical analysis.

## Installation Guide

### Requirements
- Python 3.x
- Pygame
- WebSocket-server

### Installation Steps
1. Clone the repository
```bash
git clone https://github.com/liwayne58/SA_IntersectionSimulation.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Start the simulator
```bash
python main.py
```

### Configuration Notes
- Default WebSocket connection address: `127.0.0.1:5587`
- Connection settings can be modified in `Model/WebSocket.py`

## System Architecture
- Frontend: Python Pygame simulation interface
- Communication: WebSocket service
- Backend: Java server
- Algorithm: Weighted calculation system

## License
This project is licensed under the MIT License.

## Original Project
This project is based on [Basic-Traffic-Intersection-Simulation](https://github.com/mihir-m-gandhi/Basic-Traffic-Intersection-Simulation) By [Mihir Gandhi](https://github.com/mihir-m-gandhi), which has been modified and extended. The original project is also licensed under the MIT License.

You can also refer to this [video information](https://www.youtube.com/watch?v=ZzKuR2kSqM4).

## Contact
- Email: wayneli058@gmail.com