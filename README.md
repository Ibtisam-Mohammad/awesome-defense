# Awesome Defence

> A curated list of open-source and public resources for physical defence, defence equipment, emergency-response, unmanned systems, sensing, field communications, geospatial intelligence, simulation, and command-and-control.


## Contents

- [Start Here](#start-here)
- [Curated Lists And Indexes](#curated-lists-and-indexes)
- [Government And Defence OSS Hubs](#government-and-defence-oss-hubs)
- [Defence Industrial Base, Manufacturing, And Field Repair](#defence-industrial-base-manufacturing-and-field-repair)
- [Drone And UxV Autopilots](#drone-and-uxv-autopilots)
- [Drone Hardware And FPV](#drone-hardware-and-fpv)
- [Open Hardware, Airframes, And Vehicle Design](#open-hardware-airframes-and-vehicle-design)
- [Power, Propulsion, And Endurance Modeling](#power-propulsion-and-endurance-modeling)
- [Drone Payloads And Payload Integration](#drone-payloads-and-payload-integration)
- [Drone Payload Delivery And Logistics](#drone-payload-delivery-and-logistics)
- [Ground Control And MAVLink](#ground-control-and-mavlink)
- [Flight Logs, Telemetry Analytics, And Incident Review](#flight-logs-telemetry-analytics-and-incident-review)
- [Mission Planning, Survey, And Photogrammetry Workflows](#mission-planning-survey-and-photogrammetry-workflows)
- [Autonomy, Robotics, And Simulation](#autonomy-robotics-and-simulation)
- [Guidance, Navigation, And Path Planning](#guidance-navigation-and-path-planning)
- [GPS-Denied Navigation, SLAM, And Terrain Mapping](#gps-denied-navigation-slam-and-terrain-mapping)
- [Autonomous Perception, Tracking, And Guidance](#autonomous-perception-tracking-and-guidance)
- [Onboard Edge AI And Embedded Perception](#onboard-edge-ai-and-embedded-perception)
- [Drone Coordination, Deconfliction, And Detect-And-Avoid](#drone-coordination-deconfliction-and-detect-and-avoid)
- [Defence Engagement Simulation And C2](#defence-engagement-simulation-and-c2)
- [Jamming Detection And RF Interference Monitoring](#jamming-detection-and-rf-interference-monitoring)
- [SDR And Signal Analysis](#sdr-and-signal-analysis)
- [Radar](#radar)
- [Remote ID](#remote-id)
- [UTM, U-Space, Geofencing, And Airspace Compliance](#utm-u-space-geofencing-and-airspace-compliance)
- [Contributing](#contributing)

## Legend

- `OSS` - Open-source software
- `HW` - Open hardware or hardware design files
- `Dataset` - Dataset, benchmark, or corpus
- `Paper` - Public paper, preprint, or academic publication
- `Standard` - Protocol, standard, or interoperability artifact
- `Index` - Curated list, directory, or source hub
- `Active` - Recently maintained or visibly active
- `Archive` - Inactive but historically useful
- `Dual-use` - Has both civilian and military/defence applications

## Start Here

- [ArduPilot](https://github.com/ArduPilot/ardupilot) - Full-featured open-source autopilot for multicopters, planes, rovers, boats, submarines, and related unmanned systems. `OSS` `Active`
- [PX4 Autopilot](https://github.com/PX4/PX4-Autopilot) - Open-source autopilot stack for drones and unmanned vehicles, with strong MAVLink and ROS2 ecosystem support. `OSS` `Active`
- [QGroundControl](https://github.com/mavlink/qgroundcontrol) - Cross-platform ground control station for MAVLink-compatible drones. `OSS` `Active`
- [OpenDroneMap](https://github.com/OpenDroneMap/ODM) - Toolkit for turning aerial imagery into maps, point clouds, 3D models, and DEMs. `OSS` `Active`
- [Meshtastic Firmware](https://github.com/meshtastic/firmware) - Open-source, off-grid LoRa mesh communications firmware. `OSS` `Active`
- [Open-DIS](https://github.com/open-dis) - Repository hub for open-source implementations of the Distributed Interactive Simulation protocol. `Index` `Standard`
- [FreeTAKServer](https://github.com/FreeTAKTeam/FreeTakServer) - Open-source TAK-compatible situational awareness server. `OSS`

## Curated Lists And Indexes

- [awesome-drones](https://github.com/janesmae/awesome-drones) - Broad index of drone software, libraries, services, hardware, platforms, and related projects. `Index`
- [awesome-flying-fpv](https://github.com/Matthias84/awesome-flying-fpv) - Curated index of software and hardware resources for building remote-controlled copters and planes. `Index`
- [awesome-adsb](https://github.com/rickstaa/awesome-adsb) - Curated index of ADS-B tools, receivers, decoders, maps, and learning resources. `Index`
- [awesome-sar](https://github.com/RadarCODE/awesome-sar) - Curated index of synthetic-aperture radar resources, tools, datasets, and papers. `Index`
- [geospatial-intelligence-library](https://github.com/neonpangolin/geospatial-intelligence-library) - Curated index of geospatial intelligence tools and resources. `Index`
- [openTAKpickList](https://github.com/FreeTAKTeam/openTAKpickList) - Curated index of TAK ecosystem software, plugins, hardware references, and related resources. `Index`

## Government And Defence OSS Hubs

- [Department of Defense](https://github.com/deptofdefense) - Archived official U.S. Department of Defense GitHub organization. `Index` `Archive`
- [mil-oss](https://github.com/mil-oss) - Military Open Source Software community repository hub. `Index`
- [dstl](https://github.com/dstl) - UK Defence Science and Technology Laboratory open-source repository hub. `Index`
- [National Geospatial-Intelligence Agency](https://github.com/ngageoint) - NGA repository hub for geospatial, imagery, and mission tools. `Index`
- [U.S. Naval Research Laboratory](https://github.com/USNavalResearchLaboratory) - NRL repository hub for tracking, networking, simulation, and related research. `Index`
- [AFRL RQ](https://github.com/afrl-rq) - AFRL Aerospace Systems Directorate research repository hub. `Index`

## Defence Industrial Base, Manufacturing, And Field Repair

- [FreeCAD](https://github.com/FreeCAD/FreeCAD) - Open-source parametric 3D CAD modeler for mechanical design, fixtures, parts, and engineering documentation. `OSS`
- [OpenSCAD](https://github.com/openscad/openscad) - Script-based solid modeling CAD tool useful for reproducible parametric parts and fixtures. `OSS`
- [KiCad](https://gitlab.com/kicad/code/kicad) - Open-source electronics design automation suite for schematics, PCB layout, and manufacturing outputs. `OSS`
- [LibrePCB](https://github.com/LibrePCB/LibrePCB) - Cross-platform electronics design automation suite for schematic and PCB design. `OSS`
- [Horizon EDA](https://github.com/horizon-eda/horizon) - Open-source EDA package for schematic capture and PCB layout. `OSS`
- [OpenPnP](https://github.com/openpnp/openpnp) - Open-source SMT pick-and-place machine control software. `OSS`
- [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer) - Open-source slicing software for fused-filament and resin additive manufacturing workflows. `OSS`
- [UltiMaker Cura](https://github.com/Ultimaker/Cura) - Open-source 3D printing preparation software. `OSS`
- [CuraEngine](https://github.com/Ultimaker/CuraEngine) - C++ slicing engine used by Cura for generating additive manufacturing toolpaths. `OSS`
- [Slic3r](https://github.com/slic3r/Slic3r) - Open-source slicer for 3D printing workflows and toolpath generation. `OSS`
- [OpenRadioss](https://github.com/OpenRadioss/OpenRadioss) - Open-source finite-element solver for dynamic event, impact, and structural simulation. `OSS`
- [CalculiX](https://github.com/Dhondtguido/CalculiX) - Open-source finite-element analysis suite for structural, thermal, and mechanical problems. `OSS`
- [OpenModelica](https://github.com/OpenModelica/OpenModelica) - Open-source Modelica-based modeling and simulation environment for multi-domain engineering systems. `OSS`
- [OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) - NASA-origin multidisciplinary design, analysis, and optimization framework. `OSS`
- [esptool](https://github.com/espressif/esptool) - Serial bootloader utility for Espressif chips used in embedded prototyping and field updates. `OSS`
- [ESP-IDF](https://github.com/espressif/esp-idf) - Espressif IoT development framework for ESP32-class embedded systems. `OSS`
- [PlatformIO Core](https://github.com/platformio/platformio-core) - Cross-platform embedded development environment and package ecosystem. `OSS`
- [Zephyr](https://github.com/zephyrproject-rtos/zephyr) - Open-source RTOS for connected embedded systems and hardware platforms. `OSS`

## Drone And UxV Autopilots

- [ArduPilot](https://github.com/ArduPilot/ardupilot) - Full-featured autopilot for aircraft, rovers, boats, submarines, and related vehicles. `OSS` `Active`
- [PX4 Autopilot](https://github.com/PX4/PX4-Autopilot) - Modular autopilot stack for multirotors, fixed wing, VTOL, rovers, and experimental platforms. `OSS` `Active`
- [Betaflight](https://github.com/betaflight/betaflight) - Flight-controller firmware focused on FPV multirotors and performance flying. `OSS` `Active`
- [INAV](https://github.com/iNavFlight/inav) - Navigation-enabled flight-control firmware for fixed-wing, multirotor, and RC aircraft. `OSS` `Active`
- [Paparazzi UAV](https://github.com/paparazzi/paparazzi) - Free and open-source hardware/software project for unmanned air vehicles. `OSS` `HW`
- [ROSflight Firmware](https://github.com/rosflight/rosflight_firmware) - Research-oriented firmware for UAV autopilots integrated with ROS. `OSS`
- [ROSflight ROS Packages](https://github.com/rosflight/rosflight_ros_pkgs) - ROS2 packages for interfacing companion computers with ROSflight autopilots. `OSS`
- [Crazyflie Firmware](https://github.com/bitcraze/crazyflie-firmware) - Firmware for Bitcraze Crazyflie nano quadcopters and related platforms. `OSS`
- [ESP-Drone](https://github.com/espressif/esp-drone) - ESP32-based mini drone/quadcopter firmware and reference design. `OSS` `HW`
- [dRehmFlight](https://github.com/nickrehm/dRehmFlight) - Teensy/Arduino flight controller and stabilization code for small-scale VTOL vehicles. `OSS` `HW`

## Drone Hardware And FPV

- [ExpressLRS](https://github.com/ExpressLRS/ExpressLRS) - High-performance open-source radio control link for RC and FPV systems. `OSS` `Active`
- [ExpressLRS Hardware](https://github.com/ExpressLRS/ExpressLRS-Hardware) - Open PCB designs, schematics, and printable cases for ExpressLRS modules and receivers. `HW`
- [OpenHD](https://github.com/OpenHD/OpenHD) - Open-source digital video link ecosystem for UAVs and remote vehicles. `OSS` `Active`
- [TBS Source One](https://github.com/tbs-trappy/source_one) - Open-source FPV freestyle drone frame. `HW`
- [Agilicious](https://github.com/uzh-rpg/agilicious) - Open-source and open-hardware agile quadrotor research platform. `OSS` `HW`

## Open Hardware, Airframes, And Vehicle Design

- [Pixhawk Hardware](https://github.com/pixhawk/Hardware) - Open hardware designs for autopilots, FMUs, ESCs, optical-flow sensors, and related unmanned-vehicle components. `HW` `Standard`
- [Pixhawk Standards](https://github.com/pixhawk/Pixhawk-Standards) - Connector, payload-bus, and flight-controller open standards for Pixhawk-compatible systems. `Standard` `HW`
- [OpenVSP](https://github.com/OpenVSP/OpenVSP) - NASA-origin parametric aircraft geometry and analysis tool for conceptual aircraft design. `OSS`
- [FAST-UAV](https://github.com/SizingLab/FAST-UAV) - OpenMDAO-based framework for optimal drone sizing across multirotor, fixed-wing, and hybrid VTOL configurations. `OSS`
- [AeroSandbox](https://github.com/peterdsharpe/AeroSandbox) - Differentiable aircraft design optimization tools for aerodynamics, propulsion, structures, and trajectory design. `OSS` `Active`
- [NASA Aviary](https://github.com/OpenMDAO/Aviary) - OpenMDAO-based aircraft analysis, sizing, and optimization tool using GASP/FLOPS-derived methods. `OSS` `Active`
- [SUAVE](https://github.com/suavecode/SUAVE) - Stanford conceptual aircraft-design toolbox for multi-fidelity vehicle optimization. `OSS`
- [RCAIDE-LEADS](https://github.com/leadsgroup/RCAIDE_LEADS) - Research community aircraft interdisciplinary design and analysis environment for UAVs and electric aircraft. `OSS`
- [OpenRacer](https://github.com/OpenRacer/OpenRacer) - Open-source FPV drone racing frame with CAD, DXF, and printable canopy files. `HW`
- [TBS Source One](https://github.com/tbs-trappy/source_one) - Open-source FPV freestyle frame with public design files. `HW`
- [Agilicious](https://github.com/uzh-rpg/agilicious) - Open software and hardware agile quadrotor research platform. `OSS` `HW`
- [FOS_UAV](https://github.com/rahulsarchive/FOS_UAV) - DIY open-source fixed-wing aerial mapping platform and workflow. `HW` `Archive`
- [OpenDrone](https://github.com/ljbotero/OpenDrone) - 3D-printable quadcopter frame project with STL files and parts documentation. `HW` `Archive`
- [eXploraVTOL](https://github.com/robustini/eXploraVTOL) - Open 3D-printable tailsitter VTOL project with STL, 3MF, and STEP design files. `HW`

## Power, Propulsion, And Endurance Modeling

- [FAST-UAV](https://github.com/SizingLab/FAST-UAV) - Multidisciplinary drone sizing framework with analytical models for multirotor, fixed-wing, and quad-plane UAVs. `OSS`
- [FAST-OAD](https://github.com/fast-aircraft-design/FAST-OAD) - Open framework for rapid overall aircraft design and multidisciplinary analysis using OpenMDAO. `OSS`
- [AeroSandbox](https://github.com/peterdsharpe/AeroSandbox) - Aircraft design optimization toolkit covering aerodynamics, propulsion, structures, and trajectory studies. `OSS` `Active`
- [NeuralFoil](https://github.com/peterdsharpe/NeuralFoil) - Physics-informed machine-learning airfoil analysis tool for fast design loops. `OSS` `Active`
- [RotorPy](https://github.com/spencerfolk/rotorpy) - Python multirotor simulator with aerodynamic effects, wind models, controls, and batched simulation. `OSS` `Active`
- [PteraSoftware](https://github.com/camUrban/PteraSoftware) - Open-source aerodynamics package for flapping-wing and micro air vehicle analysis. `OSS`
- [Gazebo ROS Battery](https://github.com/ctu-vras/gazebo_ros_battery) - Gazebo battery plugin with open-circuit model, power loads, state of charge, and thermal/internal-resistance options. `OSS`
- [CVaR Energy Risk Deep Model](https://github.com/castacks/cvar-energy-risk-deep-model) - Multirotor flight-energy prediction and battery-risk assessment research code. `OSS`
- [OpenAP](https://github.com/TUDelft-CNS-ATM/openap) - Open aircraft performance model and Python toolkit for performance, fuel, emissions, and trajectory studies. `OSS`

## Drone Payloads And Payload Integration

- [DJI Payload SDK](https://github.com/dji-sdk/Payload-SDK) - DJI SDK for developing drone-mounted payloads such as cameras, gimbals, mapping sensors, searchlights, and onboard analysis platforms. `OSS` `Dual-use`
- [ADAPT Multi-Mission Payload](https://gitlab.kitware.com/adapt/adapt) - Open-source sUAS payload documentation, CAD references, and simulation assets for real-time onboard AI missions. `OSS` `HW`
- [ADAPT ROS Workspace](https://gitlab.kitware.com/adapt/adapt_ros_ws) - Source workspace for Kitware's ADAPT payload software stack. `OSS`
- [Pixhawk Standards](https://github.com/pixhawk/Pixhawk-Standards) - Open drone hardware standards including the Pixhawk Payload Bus Standard. `Standard` `HW`
- [MAVLink](https://github.com/mavlink/mavlink) - Micro air vehicle communication protocol with camera, gimbal, payload, mission, and Remote ID message definitions. `OSS` `Standard`
- [asv-drones-sdr](https://github.com/asv-soft/asv-drones-sdr) - Drone SDR payload project for geolocation, spectrum analysis, and specialized equipment control. `OSS` `Dual-use`
- [STorM32 BGC](https://github.com/olliw42/storm32bgc) - Open-source 3-axis brushless gimbal controller for camera and sensor stabilization. `OSS` `HW`
- [OpenHD](https://github.com/OpenHD/OpenHD) - Open-source digital video link ecosystem for UAV payload video and telemetry. `OSS` `Active`

## Drone Payload Delivery And Logistics

- [autonomous-drone](https://github.com/szebedy/autonomous-drone) - PX4, MAVROS, Gazebo, SVO, WhyCon, and EWOK research stack for autonomous drone delivery and collision-aware trajectory planning. `OSS` `Archive`
- [UAV-EXPRESS](https://github.com/ISEC-AHU/UAV-EXPRESS) - Research code for energy-aware computation and resource scheduling in UAV delivery scenarios. `OSS`

## Ground Control And MAVLink

- [QGroundControl](https://github.com/mavlink/qgroundcontrol) - Cross-platform ground control station for drones. `OSS` `Active`
- [Mission Planner](https://github.com/ArduPilot/MissionPlanner) - Ground control station for ArduPilot. `OSS` `Active`
- [MAVSDK](https://github.com/mavlink/MAVSDK) - High-level API and libraries for MAVLink-compatible systems. `OSS` `Active`
- [MAVROS](https://github.com/mavlink/mavros) - MAVLink communication node and gateway for ROS. `OSS` `Active`
- [gomavlib](https://github.com/bluenviron/gomavlib) - MAVLink 1.0 and 2.0 library for Go. `OSS`
- [mavp2p](https://github.com/bluenviron/mavp2p) - Flexible MAVLink router for serial, UDP, TCP, broadcast, Docker, and OpenWrt-style deployments. `OSS`

## Flight Logs, Telemetry Analytics, And Incident Review

- [PX4 Flight Review](https://github.com/PX4/flight_review) - Web application for PX4 ULog flight-log upload, analysis, 3D review, and browser-based plotting. `OSS`
- [pyulog](https://github.com/PX4/pyulog) - Python package and command-line tools for parsing, converting, and inspecting PX4 ULog files. `OSS`
- [ulog_cpp](https://github.com/PX4/ulog_cpp) - C++17 ULog reader and writer library for streamed or immediate flight-log processing. `OSS`
- [PlotJuggler](https://github.com/PlotJuggler/PlotJuggler) - Time-series visualization tool with PX4 ULog, ROS, MQTT, WebSocket, UDP, and plugin support. `OSS` `Active`
- [ARK Logloader](https://github.com/ARK-Electronics/logloader) - Automatic PX4 flight-log upload and download tooling. `OSS`
- [DroneKit Log Analyzer](https://github.com/dronekit/dronekit-la) - Static analyzer for ArduPilot DataFlash logs and MAVLink telemetry logs. `OSS` `Archive`
- [pymavlog](https://github.com/rmargar/pymavlog) - Lightweight Python parser for ArduPilot MAVLink binary and telemetry logs. `OSS`
- [mavlog2csv](https://github.com/sashgorokhov/mavlog2csv) - Typed Python utility for converting ArduPilot telemetry and DataFlash logs to CSV. `OSS`
- [pymavlink](https://github.com/ArduPilot/pymavlink) - Python MAVLink interface and utilities, including log-dump and message tooling. `OSS` `Active`
- [px4tools](https://github.com/dronecrew/px4tools) - Python and notebook-based PX4 flight-data plotting, system identification, and control-analysis tools. `OSS` `Archive`
- [Open DroneLog](https://github.com/arpanghosh8453/open-dronelog) - Local-first DJI and Litchi flight-log analytics dashboard. `OSS`
- [UAV Insight Toolkit](https://github.com/Tartistbz/UAV-Insight-Toolkit) - Python telemetry-analysis dashboard for PX4 and ArduPilot logs with vibration, PID, optical-flow, and 3D trajectory review. `OSS`

## Mission Planning, Survey, And Photogrammetry Workflows

- [QGroundControl](https://github.com/mavlink/qgroundcontrol) - Cross-platform MAVLink ground control station with mission planning and vehicle configuration. `OSS` `Active`
- [Mission Planner](https://github.com/ArduPilot/MissionPlanner) - ArduPilot ground control station with mission planning, log review, configuration, and simulation support. `OSS` `Active`
- [DroneRoute](https://github.com/fcsonline/droneroute) - Open-source DJI mission planner with 3D map planning, obstacle-zone modeling, templates, sharing, and KMZ export. `OSS`
- [GeoFlight Planner](https://github.com/OpenGeoOne/qgis-drone-flight-planner) - QGIS plugin for terrain-following photogrammetry, vertical inspections, circular paths, and Litchi-compatible outputs. `OSS`
- [uavRmp](https://github.com/gisma/uavRmp) - R-based UAV mission-planning package for surveys, battery-aware chunking, and Pixhawk/Litchi workflows. `OSS`
- [tmplanner](https://github.com/ethz-asl/tmplanner) - Real-time informative motion-planning framework for UAV-based terrain monitoring. `OSS` `Archive`
- [Fields2Cover](https://github.com/Fields2Cover/Fields2Cover) - Coverage path-planning library for robotic survey, agriculture, and area-coverage missions. `OSS`
- [OpenDroneMap](https://github.com/OpenDroneMap/ODM) - Command-line toolkit for turning aerial images into maps, point clouds, 3D models, and DEMs. `OSS`
- [WebODM](https://github.com/WebODM/WebODM) - Web interface for commercial-grade drone image processing and photogrammetry workflows. `OSS` `Active`
- [NodeODM](https://github.com/OpenDroneMap/NodeODM) - Lightweight REST API for aerial image processing engines such as ODM and MicMac. `OSS`
- [OpenSfM](https://github.com/mapillary/OpenSfM) - Structure-from-motion pipeline for camera-pose recovery and 3D reconstruction from image sets. `OSS`
- [openMVG](https://github.com/openMVG/openMVG) - Multiple-view geometry and structure-from-motion library for reproducible photogrammetry pipelines. `OSS`
- [COLMAP](https://github.com/colmap/colmap) - General-purpose structure-from-motion and multi-view stereo photogrammetry system. `OSS`
- [Meshroom](https://github.com/alicevision/Meshroom) - Node-based photogrammetry application built on AliceVision. `OSS`
- [OpenAerialMap](https://github.com/hotosm/openaerialmap) - Open service and platform for sharing openly licensed aerial imagery and map layers. `OSS`

## Autonomy, Robotics, And Simulation

- [aerial-autonomy-stack](https://github.com/JacopoPan/aerial-autonomy-stack) - ROS2 stack for simulating and deploying perception-based PX4/ArduPilot drone swarms with YOLO, LiDAR, and Jetson support. `OSS` `Active`
- [gym-pybullet-drones](https://github.com/utiasDSL/gym-pybullet-drones) - PyBullet Gymnasium environments for single and multi-agent quadcopter control. `OSS`
- [DiffPhysDrone](https://github.com/HenryHuYu/DiffPhysDrone) - Research code for learning vision-based agile quadrotor flight with differentiable physics. `OSS`
- [DroneDetour](https://github.com/xumeng367/DroneDetour) - Java and Android UAV path-planning library for detours around polygonal no-fly zones. `OSS`
- [OpenAMASE](https://github.com/afrl-rq/OpenAMASE) - AFRL simulation environment for autonomous systems experimentation. `OSS`
- [OpenUxAS](https://github.com/afrl-rq/OpenUxAS) - Service-oriented autonomy framework for unmanned systems. `OSS`
- [Airspace Encounter Models](https://github.com/Airspace-Encounter-Models) - Repository hub for aircraft encounter simulation and safety-research models. `Index`

## Guidance, Navigation, And Path Planning

- [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) - Readable implementations of robotics algorithms for localization, mapping, SLAM, path planning, path tracking, and aerial navigation. `OSS`
- [Navigation2](https://github.com/ros-navigation/navigation2) - ROS2 navigation framework for localization, planning, control, behavior trees, and obstacle avoidance. `OSS` `Active`
- [NMPC PX4 ROS2](https://github.com/kousheekc/nmpc_px4_ros2) - ROS2 nonlinear model predictive control pipeline for PX4 aerial-vehicle trajectory tracking. `OSS`
- [ROS2 Offboard Drone Control](https://github.com/Marnonel6/ROS2_offboard_drone_control) - PX4 and ROS2 offboard control stack with high-level path planning on a companion computer. `OSS`
- [DroneDetour](https://github.com/xumeng367/DroneDetour) - Java and Android UAV path-planning library for detours around polygonal no-fly zones. `OSS`
- [Fields2Cover](https://github.com/Fields2Cover/Fields2Cover) - Coverage path-planning library for vehicles and robotic field operations. `OSS`
- [Aerial Autonomy Stack](https://github.com/JacopoPan/aerial-autonomy-stack) - ROS2 stack for simulating and deploying perception-based PX4/ArduPilot drone swarms. `OSS` `Active`

## GPS-Denied Navigation, SLAM, And Terrain Mapping

- [WildNav](https://github.com/TIERS/wildnav) - GNSS-free drone localization by matching onboard imagery against georeferenced satellite maps. `OSS`
- [GISNav](https://github.com/hmakelin/gisnav) - ROS2 map-based visual navigation for estimating drone position from camera imagery and onboard GIS maps. `OSS`
- [OpenREALM](https://github.com/laxnpander/OpenREALM) - Real-time aerial mapping pipeline using visual SLAM and 3D reconstruction for multirotor platforms. `OSS`
- [terrain-navigation](https://github.com/ethz-asl/terrain-navigation) - Safe low-altitude fixed-wing navigation in steep terrain using terrain-aware planning. `OSS`
- [terrain-navigation2](https://github.com/ethz-asl/terrain-navigation2) - ROS2 port of the ETH Zurich steep-terrain fixed-wing navigation stack. `OSS`
- [FAST_LIO](https://github.com/hku-mars/FAST_LIO) - Computationally efficient LiDAR-inertial odometry package for fast motion, noisy, and cluttered environments. `OSS`
- [FAST-LIVO2](https://github.com/hku-mars/FAST-LIVO2) - Fast direct LiDAR-inertial-visual odometry for localization and mapping in degraded environments. `OSS`
- [Point-LIO](https://github.com/hku-mars/Point-LIO) - High-bandwidth LiDAR-inertial odometry for aggressive motion and high-frequency odometry. `OSS`
- [Point-LIO ROS2](https://github.com/dfloreaa/point_lio_ros2) - ROS2 implementation of Point-LIO with support for common LiDAR models. `OSS`
- [Swarm-LIO2](https://github.com/hku-mars/Swarm-LIO2) - Decentralized LiDAR-inertial odometry for UAV swarms. `OSS`
- [Voxel-SLAM](https://github.com/hku-mars/Voxel-SLAM) - LiDAR-inertial SLAM system with odometry, local mapping, loop closure, and global mapping. `OSS`
- [Direct LiDAR-Inertial Odometry](https://github.com/vectr-ucla/direct_lidar_inertial_odometry) - Lightweight continuous-time LiDAR-inertial odometry implementation from ICRA 2023. `OSS`
- [LIO-SAM](https://github.com/TixiaoShan/LIO-SAM) - Real-time LiDAR-inertial odometry via smoothing and mapping. `OSS`
- [hdl_graph_slam](https://github.com/koide3/hdl_graph_slam) - 3D LiDAR graph SLAM with scan matching, loop detection, and IMU/GPS/floor-plane constraints. `OSS`
- [GLIM](https://github.com/koide3/glim) - Modern 3D LiDAR-based localization and mapping framework from the hdl_graph_slam author. `OSS`
- [MOLA](https://github.com/MOLAorg/mola) - Modular ROS2-capable framework for localization, SLAM, LiDAR odometry, and mapping pipelines. `OSS` `Active`
- [OpenVINS](https://github.com/rpng/open_vins) - Visual-inertial navigation research platform for camera-IMU localization. `OSS`
- [MINS](https://github.com/rpng/MINS) - Multi-sensor-aided inertial navigation system fusing IMU, camera, LiDAR, GPS/GNSS, and wheel sensors. `OSS`
- [VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) - Visual-inertial state-estimation framework with stereo, mono, GPS fusion, loop closure, and global pose graph. `OSS`
- [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) - Visual, visual-inertial, monocular, stereo, RGB-D, and multi-map SLAM library. `OSS`
- [Kimera-VIO](https://github.com/MIT-SPARK/Kimera-VIO) - Metric-semantic visual-inertial odometry library for real-time state estimation. `OSS`
- [AI-IMU Dead-Reckoning](https://github.com/mbrossar/ai-imu-dr) - Learning-based inertial dead-reckoning research code for navigation without external fixes. `OSS`
- [monocular-slam-drone](https://github.com/jonasctrl/monocular-slam-drone) - AirSim/ROS monocular depth, voxel mapping, and A* navigation framework for UAVs in unknown 3D environments. `OSS`

## Autonomous Perception, Tracking, And Guidance

- [VisDrone Dataset](https://github.com/VisDrone/VisDrone-Dataset) - Large drone-based image and video benchmark for object detection, tracking, and crowd-counting research. `Dataset`
- [Multi-Drone Multi-Object Detection And Tracking](https://github.com/VisDrone/Multi-Drone-Multi-Object-Detection-and-Tracking) - MDMT benchmark and code for cross-drone multi-object tracking and identity association under occlusion. `OSS` `Dataset`
- [trackers](https://github.com/roboflow/trackers) - Clean multi-object tracking implementations including SORT, ByteTrack, OC-SORT, and BoT-SORT. `OSS` `Active`
- [MCMOT](https://github.com/CaptainEven/MCMOT) - Real-time one-stage multi-class multi-object tracking implementation with VisDrone examples. `OSS`
- [Stone Soup](https://github.com/dstl/Stone-Soup) - DSTL framework for target tracking, state estimation, and sensor fusion research. `OSS`
- [Tracker Component Library](https://github.com/USNavalResearchLaboratory/TrackerComponentLibrary) - NRL tracking and estimation algorithms for multi-sensor fusion research. `OSS`
- [UAVros](https://github.com/shupx/UAVros) - PX4/Gazebo ROS simulation packages for visual landing, object tracking, formation, and multi-UAV gimbal-camera experiments. `OSS`
- [GISNav](https://github.com/hmakelin/gisnav) - ROS2 simulation package for map-based visual navigation that estimates drone position by matching camera imagery to onboard GIS maps. `OSS`
- [trochoids](https://github.com/castacks/trochoids) - C++ time-optimal UAV path-planning library for wind-aware Dubins and trochoidal trajectories. `OSS`
- [autonomous_landing_uav](https://github.com/MikeS96/autonomous_landing_uav) - ROS/Gazebo autonomous landing stack with visual marker tracking, Kalman filtering, and PX4 offboard control. `OSS`

## Onboard Edge AI And Embedded Perception

- [SenseCraft AI](https://github.com/Seeed-Studio/SenseCraft-AI) - Open-source inference server and web UI for deploying YOLO models on NVIDIA Jetson devices. `OSS`
- [SenseCraft Model Assistant](https://github.com/Seeed-Studio/ModelAssistant) - Embedded-AI toolkit for deploying YOLOv8, YOLOv8 Pose, and NVIDIA TAO models on MCUs and SBCs. `OSS`
- [Waggle AI@Edge](https://github.com/waggle-sensor) - Repository hub for the Waggle distributed edge-AI sensing platform and edge-application ecosystem. `Index`
- [NanoSAM](https://github.com/NVIDIA-AI-IOT/nanosam) - TensorRT-optimized Segment Anything variant for real-time segmentation on Jetson Orin platforms. `OSS`
- [NanoOWL](https://github.com/NVIDIA-AI-IOT/nanoowl) - TensorRT-optimized OWL-ViT open-vocabulary detector for Jetson Orin platforms. `OSS`
- [Jetson Multicamera Pipelines](https://github.com/NVIDIA-AI-IOT/jetson-multicamera-pipelines) - Real-time multi-camera CV and AI pipeline examples for NVIDIA Jetson. `OSS`
- [jetson-inference](https://github.com/dusty-nv/jetson-inference) - NVIDIA Jetson deep-learning inference tutorials and reference applications. `OSS`
- [EdgeYOLO](https://github.com/LSH9832/edgeyolo) - Edge-real-time object detector with source code, weights, and hyperparameters. `OSS`
- [LEAF-YOLO](https://github.com/highquanglity/LEAF-YOLO) - Lightweight edge-real-time small-object detector for aerial imagery. `OSS`
- [YOLOv8-lite UAV Detector](https://github.com/hawkinglai/uav_det) - Interpretable lightweight YOLOv8 detector for real-time UAV detection. `OSS`
- [TakuNet](https://github.com/DanielRossi1/TakuNet) - Energy-efficient CNN for real-time inference on embedded UAV systems in emergency-response scenarios. `OSS`
- [Depth Anything for Jetson Orin](https://github.com/IRCVLab/Depth-Anything-for-Jetson-Orin) - Real-time depth-estimation pipeline optimized for NVIDIA Jetson Orin. `OSS`
- [YoloV8 TensorRT Jetson Nano](https://github.com/Qengineering/YoloV8-TensorRT-Jetson_Nano) - Lightweight C++ YOLOv8 TensorRT implementation for Jetson Nano and Orin Nano. `OSS`
- [Event-Orin Drone](https://github.com/tudelft/event_orin_drone) - TU Delft overview repository for a PX4, ROS2, event-camera, and Jetson Orin NX drone platform. `OSS` `HW`
- [LiDAR-Visual-Inertial-SLAM](https://github.com/valentinomario/LiDAR-Visual-Inertial-SLAM) - ROS2 LiDAR-visual-inertial SLAM setup for Jetson Orin NX, Livox MID360, and Arducam sensors. `OSS`

## Drone Coordination, Deconfliction, And Detect-And-Avoid

- [Aerostack2](https://github.com/aerostack2/aerostack2) - ROS2 framework for autonomous multi-aerial-robot systems with modular swarming-oriented architecture. `OSS` `Active`
- [OpenUxAS](https://github.com/afrl-rq/OpenUxAS) - AFRL service-oriented autonomy framework for unmanned systems, route planning, task ordering, and multi-vehicle decision support. `OSS`
- [EGO-Swarm](https://github.com/ZJU-FAST-Lab/ego-planner-swarm) - Decentralized asynchronous multi-robot quadrotor navigation in unknown cluttered environments. `OSS`
- [RACER](https://github.com/SYSU-STAR/RACER) - Decentralized multi-UAV collaborative exploration framework with limited/asynchronous communication. `OSS`
- [Ardupilot Multiagent Simulation](https://github.com/aau-cns/Ardupilot_Multiagent_Simulation) - ArduPilot, ROS2, and Gazebo environment for spawning and controlling multiple simulated drones. `OSS`
- [ArduSim](https://github.com/GRCDEV/ArduSim) - Historical real-time multi-UAV simulator for flight coordination protocols, planned missions, and swarm behavior over MAVLink. `OSS` `Archive`
- [ws_uspace_control_room](https://github.com/manudelu/ws_uspace_control_room) - ROS2, PX4, MQTT, and AirSim/Unreal control room for coordinated UAV fleet management and digital twins. `OSS`
- [Project Starling](https://github.com/StarlingUAS/ProjectStarling) - Containerized UAV simulation-to-reality infrastructure for single and multi-UAV systems. `OSS`
- [Crazyswarm2](https://github.com/IMRCLab/crazyswarm2) - ROS2 stack for Crazyflie multirotor swarms. `OSS` `Active`
- [Swarm-LIO2](https://github.com/hku-mars/Swarm-LIO2) - Decentralized LiDAR-inertial odometry for UAV swarms. `OSS`
- [multi_agent_pkgs](https://github.com/lis-epfl/multi_agent_pkgs) - Multi-agent aerial motion-planning packages using the HDSM method. `OSS`
- [RVO2](https://github.com/snape/RVO2) - Optimal reciprocal collision-avoidance library for multi-agent motion planning. `OSS`
- [dyn_small_obs_avoidance](https://github.com/hku-mars/dyn_small_obs_avoidance) - LiDAR-based UAV dynamic small-obstacle avoidance system with FAST-LIO, mapping, and kinodynamic A* modules. `OSS`
- [onboard_detector](https://github.com/Zhefan-Xu/onboard_detector) - Dynamic obstacle detection and tracking for autonomous navigation on constrained onboard computers. `OSS`
- [trajectory_optimization](https://github.com/Zhefan-Xu/trajectory_optimization) - Historical DPMPC planner for real-time UAV trajectory planning in static environments with dynamic obstacles. `OSS` `Archive`
- [px4_fast_planner](https://github.com/mzahana/px4_fast_planner) - PX4 integration for real-time collision-free trajectory planning with Fast-Planner, MAVROS, and onboard sensing. `OSS`
- [PULP-Dronet](https://github.com/pulp-platform/pulp-dronet) - Open software, hardware, datasets, and trained networks for onboard visual navigation and collision avoidance on nano-drones. `OSS` `HW`

## Defence Engagement Simulation And C2

- [Boomslang C2 Simulator](https://github.com/kabartsjc/boomslang-c2-sim) - Open-source military C2 simulation tool for doctrine, exercises, forces, missions, effects, cost, impact, and risk analysis. `OSS`
- [Open-DIS](https://github.com/open-dis) - Repository hub for IEEE-1278.1 Distributed Interactive Simulation implementations in multiple languages. `Index` `Standard`
- [OpenC2SIM](https://github.com/OpenC2SIM) - Repository hub for Command-and-Control Systems to Simulation Systems Interoperation artifacts. `Index` `Standard`
- [OpenAMASE](https://github.com/afrl-rq/OpenAMASE) - AFRL Aerospace Multi-Agent Simulation Environment for multi-UAV mission-level simulation and C2 experiments. `OSS`
- [OpenUxAS](https://github.com/afrl-rq/OpenUxAS) - AFRL service-oriented autonomy framework for unmanned systems and mission-level autonomy. `OSS`
- [DISPluginForUnreal](https://github.com/AF-GRILL/DISPluginForUnreal) - Legacy Unreal Engine 4 plugin for Distributed Interactive Simulation. `OSS` `Archive`
- [DISPluginForUnity](https://github.com/AF-GRILL/DISPluginForUnity) - Unity plugin for Distributed Interactive Simulation. `OSS`

## Jamming Detection And RF Interference Monitoring

- [JamShield Dataset](https://github.com/panitsasi/JamShield-Dataset) - Dataset for research on machine-learning detection of over-the-air jamming attacks. `Dataset` `Dual-use`
- [GNSS-SDR](https://github.com/gnss-sdr/gnss-sdr) - Open-source software-defined GNSS receiver useful for GNSS signal monitoring and interference research. `OSS` `Dual-use`
- [gnss-sdr-1pps](https://github.com/oscimp/gnss-sdr-1pps) - GNSS-SDR fork focused on 1-PPS, spoofing detection, and jamming detection/cancellation research with coherent SDR inputs. `OSS` `Dual-use`
- [QSpectrumAnalyzer](https://github.com/xmikos/qspectrumanalyzer) - Historical spectrum analyzer GUI for SoapySDR, rtl_power, hackrf_sweep, rx_power, and related SDR backends. `OSS` `Archive`
- [RFAnalyzer](https://github.com/demantz/RFAnalyzer) - Android real-time spectrum analyzer for HackRF, RTL-SDR, Airspy, and HydraSDR. `OSS`
- [OpenWebRX+](https://github.com/0xAF/openwebrxplus) - Multi-user web SDR receiver with decoders, maps, scanning, and recording support. `OSS`

## SDR And Signal Analysis

- [GNU Radio](https://github.com/gnuradio/gnuradio) - Free and open-source signal-processing runtime and SDR toolkit. `OSS` `Active`
- [Gqrx](https://github.com/gqrx-sdr/gqrx) - SDR receiver powered by GNU Radio and Qt. `OSS`
- [SDR++](https://github.com/AlexandreRouma/SDRPlusPlus) - Cross-platform SDR receiver software. `OSS`
- [OpenWebRX+](https://github.com/0xAF/openwebrxplus) - Web-based, multi-user SDR receiver software. `OSS`
- [QSpectrumAnalyzer](https://github.com/xmikos/qspectrumanalyzer) - Historical SDR spectrum analyzer for rtl-sdr, HackRF, Airspy, LimeSDR, SDRplay, USRP, and SoapySDR backends. `OSS` `Archive`
- [RFAnalyzer](https://github.com/demantz/RFAnalyzer) - Android SDR spectrum analysis app. `OSS`
- [SigMF](https://github.com/sigmf/SigMF) - Metadata standard and tooling for recorded signal datasets. `OSS` `Standard`
- [sigint](https://github.com/arall/sigint) - Multi-protocol SDR signal detection and triangulation system that can output to ATAK. `OSS` `Dual-use`
- [iNTERCEPT](https://github.com/smittix/intercept) - Open-source SIGINT platform for SDR-backed signal monitoring and protocol decoding. `OSS` `Dual-use`

## Radar

- [AERIS-10 / PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) - Open-source 10.5 GHz phased-array radar research platform. `OSS` `HW` `Dual-use`
- [OpenRadar](https://github.com/PreSenseRadar/OpenRadar) - Open-source library for interacting with and processing MIMO mmWave radar data. `OSS`
- [RETINA Node](https://github.com/offworldlabs/retina-node) - Node orchestration repository for the RETINA passive radar network, including compose configuration and OTA artifact generation. `OSS` `HW` `Dual-use`
- [virtualradar](https://github.com/chstetco/virtualradar) - Historical millimeter-wave radar simulation framework for robotic applications. `OSS` `Archive`
- [FMCW-MIMO-Radar-Simulation](https://github.com/ekurtgl/FMCW-MIMO-Radar-Simulation) - MATLAB simulations for FMCW MIMO radar signal processing. `OSS`
- [software-radar](https://github.com/luigifcruz/software-radar) - Historical software-defined radar project using GNU Radio Companion and Python. `OSS` `Archive` `Dual-use`
- [USRP Software Defined Radar](https://github.com/jonasmc83/USRP_Software_defined_radar) - Historical USRP-based software-defined radar code with C++ and Qt visualization. `OSS` `Archive` `Dual-use`
- [GnuRadar](https://github.com/rseal/GnuRadar) - Older USRP-based open-source software-defined radar project. `Archive` `Dual-use`

## Remote ID

- [Open Drone ID Core C](https://github.com/opendroneid/opendroneid-core-c) - C library for encoding and decoding Open Drone ID messages for ASTM F3411 and ASD-STAN Direct Remote ID. `OSS` `Standard`
- [Open Drone ID Android Receiver](https://github.com/opendroneid/receiver-android) - Example Android receiver application for unmanned-aircraft Remote ID. `OSS`
- [Open Drone ID Wireshark Dissector](https://github.com/opendroneid/wireshark-dissector) - Wireshark dissector for the Open Drone ID broadcast protocol. `OSS`
- [Open Drone ID Linux Transmitter](https://github.com/opendroneid/transmitter-linux) - Example Linux transmitter for Open Drone ID over Bluetooth and Wi-Fi. `OSS`
- [ArduRemoteID](https://github.com/ArduPilot/ArduRemoteID) - ESP32-based Remote ID transmitter firmware for ArduPilot/Open Drone ID integration. `OSS`
- [Flight Blender](https://github.com/openutm/flight-blender) - Open-source UTM backend with Network Remote ID, flight authorization, geofencing, and traffic information services. `OSS`
- [InterUSS DSS](https://github.com/interuss/dss) - Discovery and Synchronization Service implementation for ASTM Remote ID and UTM interoperability standards. `OSS`
- [RemoteIDReceiver](https://github.com/cyber-defence-campus/RemoteIDReceiver) - Web application for monitoring drones using Remote ID technology, including DJI DroneID. `OSS`
- [drone-mesh-mapper](https://github.com/colonelpanichacks/drone-mesh-mapper) - Remote ID detection and mapping bridge that can forward detections over Meshtastic. `OSS`
- [Sky-Spy](https://github.com/colonelpanichacks/Sky-Spy) - Firmware for detecting and mapping drones broadcasting Remote ID over Wi-Fi and BLE. `OSS`

## UTM, U-Space, Geofencing, And Airspace Compliance

- [Flight Blender](https://github.com/openutm/flight-blender) - Standards-compliant Network Remote ID, flight authorization, geofence, traffic information, and U-Space/UTM backend. `OSS`
- [InterUSS DSS](https://github.com/interuss/dss) - Discovery and Synchronization Service implementation for ASTM Remote ID and UTM interoperability. `OSS` `Standard`
- [InterUSS Monitoring](https://github.com/interuss/monitoring) - USS monitoring and automated conformance-testing tools for Remote ID and UTM services. `OSS` `Standard`
- [UTM Implementation US Get Started](https://github.com/utmimplementationus/getstarted) - Public onboarding resources for UTM service operationalization, governance, and strategic conflict-detection pilots. `Standard`
- [Open Drone ID Specs](https://github.com/opendroneid/specs) - Historical Open Drone ID draft specification repository with references to related Remote ID components. `Archive`
- [UAS Tech Standards](https://github.com/uastech/standards) - Unofficial index of UAS-related API and standards references, including Network Remote ID material. `Index`
- [Open Drone ID Core C](https://github.com/opendroneid/opendroneid-core-c) - Encoding and decoding library for ASTM F3411 and ASD-STAN Direct Remote ID messages. `OSS` `Standard`
- [Open Drone ID Android Receiver](https://github.com/opendroneid/receiver-android) - Android reference receiver for Bluetooth and Wi-Fi Remote ID broadcasts. `OSS`
- [Open Drone ID Linux Transmitter](https://github.com/opendroneid/transmitter-linux) - Linux reference transmitter for Open Drone ID over Bluetooth and Wi-Fi. `OSS`
- [Open Drone ID Wireshark Dissector](https://github.com/opendroneid/wireshark-dissector) - Wireshark dissector for inspecting Open Drone ID broadcast protocol messages. `OSS`
- [ArduRemoteID](https://github.com/ArduPilot/ArduRemoteID) - ArduPilot/OpenDroneID transmitter firmware targeting FAA and EU Remote ID compliance. `OSS`
- [Drone Scanner](https://github.com/fennhelloworld/drone-scanner) - Multiplatform app for receiving and mapping Direct Remote ID broadcasts. `OSS`
- [RemoteIDReceiver](https://github.com/cyber-defence-campus/RemoteIDReceiver) - Offline-capable Remote ID monitoring and replay web application. `OSS`
- [OpenARIA](https://github.com/mitre-public/open-aria) - MITRE open-source Aviation Risk Identification and Assessment tooling for aircraft location data. `OSS`
- [DroneDetour](https://github.com/xumeng367/DroneDetour) - UAV path-planning library for detours around polygonal no-fly zones. `OSS`

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

Every entry should be useful, public, clearly described, and relevant to the repository scope.

## License

This list is released under [CC0-1.0](LICENSE). You may copy, remix, and reuse it freely.
