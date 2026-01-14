# 📘 Isaac Sim & ROS 2 Handbook
**A Practical Guide to Sim-to-Real Workflows for Industrial Manipulation**

## 🚀 Overview
This repository contains:

1.  **A Generic Guide:** Step-by-step documentation of the **NVIDIA Isaac Sim** ecosystem, focusing on setting up the environment, bridging to **ROS 2**, and implementing GPU-accelerated motion planning using **CuRobo**.
2.  **Example using Yaskawa GP-180:** A specific, operational example applying these concepts to the **Yaskawa GP-180** robot, targeting the **"Scan & Polish"** industrial application.

## 🎯 Key Objectives
This handbook documents the process of:
* **Environment Setup:** Configuring a local workstation for high-fidelity simulation using Isaac Sim.
* **Robot Modeling:** Importing and configuring industrial manipulators (URDF/USD) with accurate physics boundaries.
* **Sensor Integration:** Simulating real-world perception data, specifically **Laser Scanners (LiDAR)** and **Load Cells** (Force/Torque sensors).
* **Motion Planning:** Utilizing **NVIDIA CuRobo** for collision-free, geometric path planning and obstacle avoidance.
* **Application Logic:** Porting "Scan-and-Polish" logic (based on ROS-Industrial/Godel) into a modern simulation context.

## 🛠️ Tech Stack
* **Simulation:** NVIDIA Isaac Sim 5.1.0
* **Middleware:** ROS 2 (Jazzy)
* **Motion Planning:** NVIDIA CuRobo (CUDA Robotics)
* **Hardware Target:** Yaskawa GP-180

---
*Created by Usama Jahangir*