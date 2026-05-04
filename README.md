# AEGIS — Autonomous Emergency Grid Intelligence Swarm

*A fully autonomous, zero-infrastructure disaster response robot swarm simulation.*  
No operator. No GPS. No cloud. No internet. Just deploy and let them work.
---

## The Problem

Every year, thousands of people die trapped in collapsed buildings, floods, and fires — not because rescue is impossible, but because it's too slow and too
dangerous for human responders.
The first *72 hours* after a disaster are the golden window. Most survivors are found — or lost — in this period.
Current rescue robots are costly, need skilled operators, fail in GPS-denied rubble environments, and can't be deployed in swarms. There is no affordable,
autonomous, zero-infrastructure solution.

*AEGIS is building that solution.*

---

## What AEGIS Does

AEGIS deploys a swarm of small, autonomous robots into disaster zones — collapsed buildings, fires, floods — and:

- *Maps* the entire disaster environment using Collaborative SLAM
- *Detects survivors* using thermal imaging and acoustic bio-signal processing
- *Coordinates* between units using a LoRa mesh network — no internet required
- *Self-manages* energy, roles, and tasks with zero human operators
- *Generates* a live Digital Twin of the disaster zone for rescue commanders

Zero operator. Zero GPS. Zero cloud. Zero internet.

---

## Architecture


┌─────────────────────────────────────────────────────────────┐
│                    AEGIS SWARM SYSTEM                        │
├─────────────────┬───────────────────┬───────────────────────┤
│   RAPTOR (MAV)  │  CRAWLER (Ground) │   HYDRA (Amphibious)  │
│   Aerial survey │  Rubble entry     │   Flood zones         │
│   Signal relay  │  Survivor detect  │   Water search        │
└────────┬────────┴────────┬──────────┴───────────┬───────────┘
         │                 │                       │
         └─────────────────┼───────────────────────┘
                           │
              ┌────────────▼────────────┐
              │    LoRa Mesh Network    │
              │   (Zero Internet)       │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │     Digital Twin        │
              │  Live 3D Disaster Map   │
              └─────────────────────────┘


---

## Key Capabilities

### Acoustic Bio-Signal Detection
Each Crawler carries a 4-microphone array and geophone. The system detects heartbeat signatures (0.8–2.5 Hz) buried in rubble noise — triangulating survivor 
positions to within half a meter.

### Emergent Role Assignment
No pre-programmed roles. The swarm self-assigns responsibilities based on environment — mesh relay, survivor anchor, passive beacon — inspired by ant colony
behavior. This is an open research problem in robotics.

### Federated On-Swarm Learning
When one unit detects a novel survivor signal pattern, it broadcasts only the model weight deltas to other units via LoRa mesh. The entire swarm gets smarter as 
the mission progresses — with zero raw data sharing and zero internet.

### Byzantine Fault-Tolerant Consensus
Damaged robots with corrupted sensors are automatically voted out of the network. Survivor detection requires agreement from at least 2 units — preventing false 
positives from hardware failures.

### Collaborative SLAM in Rubble
Individual robot maps are merged and reconciled in real time using distributed pose graph optimization — building a shared 3D model of the disaster zone that no
single robot could build alone.

### Autonomous Energy Economy
The swarm monitors battery levels collectively. Low-battery units reroute their tasks automatically and navigate back to the deployment point, entering beacon
mode to extend the mesh network.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Physics Simulation | Gazebo Harmonic |
| Robot Operating System | ROS 2 Jazzy |
| Swarm Logic | Python |
| Motor Control | C (deterministic real-time) |
| Survivor Detection AI | TensorFlow Lite |
| Mapping / SLAM | SLAM Toolbox + Nav2 |
| Visualization | RViz2 |
| Mesh Communication | Simulated LoRa via ROS 2 topics |
| Version Control | GitHub |

---

## Project Structure


aegis-swarm-sim/
│
├── worlds/
│   └── collapsed_building.world    # Gazebo disaster environment
│
├── robots/
│   └── crawler.urdf.xacro          # Crawler robot 3D model + physics
│
├── src/
│   └── aegis_core/
│       ├── heartbeat_monitor.py    # Acoustic bio-signal simulation
│       ├── signal_analyzer.py      # Heartbeat pattern detection
│       ├── motor_controller.c      # C-based autonomous navigation
│       ├── survivor_detector.py    # Thermal imaging detection
│       ├── swarm_coordinator.py    # Multi-robot coordination
│       └── mission_logger.py       # Mission data logging
│
├── ai_models/
│   └── survivor_model.tflite       # On-device survivor detection model
│
├── config/
│   └── aegis_phase1.launch.py      # Single command full system launch
│
└── docs/
    └── mission_logs/               # JSON mission reports


---

## Build Phases

### ✅ Phase 1 — Single Robot Core (Active)
- [x] ROS 2 workspace and package structure
- [x] Acoustic heartbeat simulation node
- [x] Signal analyzer with pattern detection
- [x] Crawler robot URDF model
- [x] Disaster world in Gazebo
- [x] C motor controller with state machine
- [x] Single command launch file

### 🔲 Phase 2 — Intelligence Layer
- [ ] SLAM Map Buliding 
- [ ] Thermal Survivor Detection 
- [ ] Acoustic heartbeat ML model (trained on real data)
- [ ] Survivor triangulation using multi-mic array
- [ ] Full autonomous navigation with Nav2
- [ ] Digital Twin generation

### 🔲 Phase 3 — Swarm
- [ ] 3-unit heterogeneous swarm (Raptor + Crawler + Hydra)
- [ ] Emergent role assignment algorithm
- [ ] LoRa mesh communication simulation
- [ ] Federated on-swarm learning
- [ ] Byzantine fault-tolerant consensus
- [ ] Full swarm demo video

---

## Open Research Problems This Project Tackles

| Problem | Status in Research |
|---|---|
| Acoustic heartbeat detection through rubble | Early-stage, few working implementations |
| Emergent role assignment in heterogeneous swarms | Active research, no standard solution |
| Federated learning on physical robot swarms | Mostly theoretical |
| Collaborative SLAM in rubble environments | Open problem, active DARPA funding |
| Byzantine-tolerant swarm consensus in robotics | Sparse robotic application |

---

## Getting Started

### Prerequisites
- Ubuntu 24.04 (or WSL2 on Windows 11)
- ROS 2 Jazzy
- Gazebo Harmonic
- Python 3.12

## Why This Matters

India faces frequent natural disasters — earthquakes, floods, building collapses — that kill thousands annually. Current rescue robots are priced out of reach
for most response teams.

AEGIS is designed to be:
- *Cheap* — built from commodity components
- *Autonomous* — zero operator training required
- *Resilient* — works without GPS, internet, or infrastructure
- *Scalable* — more units = better coverage, not more operators

A swarm of 10 AEGIS units could cover a 5-storey collapsed building in under 8 minutes and locate all survivors — faster than any human team can safely enter.

---

## Author
*Zafreen Jagir*:
   BE Computer Science Engineering;   
   Saveetha Engineering Of College, Chennai;    
   GitHub: [ZafreenJagir](https://github.com/ZafreenJagir).

*Mohammed Mubashir*: 
   BTech Robotics & AI Engineering;  
   Presidency University, Bengaluru; 
   GitHub: [@mubashir956](https://github.com/mubashir956).

---

## Acknowledgements

Built on the shoulders of:
- ROS 2 — Open Robotics
- Gazebo — Open Robotics  
- SLAM Toolbox — Steve Macenski
- Nav2 — Open Navigation LLC

---

AEGIS is a simulation-first open source project. Real hardware implementation is the long-term goal.  
If you're a researcher, student, or organization working on disaster robotics — let's connect!!
