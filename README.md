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
- [Counter-UAS Detection And Tracking](#counter-uas-detection-and-tracking)
- [Counter-UAS Detection Infrastructure](#counter-uas-detection-infrastructure)
- [AI-Assisted Drone Detection And Sensor Fusion](#ai-assisted-drone-detection-and-sensor-fusion)
- [Air Picture, C2, And Sensor Analysis](#air-picture-c2-and-sensor-analysis)
- [Electromagnetic, RF, Optical, And Multiphysics Simulation](#electromagnetic-rf-optical-and-multiphysics-simulation)
- [Camouflage Detection And Remote-Sensing Tooling](#camouflage-detection-and-remote-sensing-tooling)
- [TAK, C2, And Situational Awareness](#tak-c2-and-situational-awareness)
- [Battlefield C2, Drone Tasking, And Shared Air Picture](#battlefield-c2-drone-tasking-and-shared-air-picture)
- [Field Communications And Mesh](#field-communications-and-mesh)
- [Resilient Links, Mesh, And GNSS-Denied Navigation](#resilient-links-mesh-and-gnss-denied-navigation)
- [Space, Satellite Communications, And ISR](#space-satellite-communications-and-isr)
- [Video, Telemetry Links, And Payload Streaming](#video-telemetry-links-and-payload-streaming)
- [Geospatial Intelligence, Mapping, And Imagery](#geospatial-intelligence-mapping-and-imagery)
- [Critical Infrastructure Protection And Damage Assessment](#critical-infrastructure-protection-and-damage-assessment)
- [Emergency Response, Search And Rescue, And Disaster Mapping](#emergency-response-search-and-rescue-and-disaster-mapping)
- [ADS-B And Air Tracking](#ads-b-and-air-tracking)
- [Training And Simulation Interoperability](#training-and-simulation-interoperability)
- [High-Fidelity Simulation, Digital Twins, And Synthetic Data](#high-fidelity-simulation-digital-twins-and-synthetic-data)
- [Ground, Surface, And Underwater Robotics](#ground-surface-and-underwater-robotics)
- [UGV Logistics, CASEVAC, And Ground Robotics](#ugv-logistics-casevac-and-ground-robotics)
- [Maritime USVs And Naval Drone Operations](#maritime-usvs-and-naval-drone-operations)
- [Mine Action, EOD, And Humanitarian Demining](#mine-action-eod-and-humanitarian-demining)
- [Research Datasets](#research-datasets)
- [Related Topics To Watch](#related-topics-to-watch)
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

## Counter-UAS Detection And Tracking

- [Batear](https://github.com/batear-io/batear) - ESP32-S3 acoustic drone detector with encrypted LoRa or wired Ethernet/PoE alerting. `OSS` `HW` `Dual-use`
- [Sky-Spy](https://github.com/colonelpanichacks/Sky-Spy) - Firmware for detecting and mapping drones broadcasting Remote ID over Wi-Fi and BLE. `OSS` `Dual-use`
- [drone-mesh-mapper](https://github.com/colonelpanichacks/drone-mesh-mapper) - ESP32 and Meshtastic bridge for mapping Remote ID detections. `OSS`
- [sigint](https://github.com/arall/sigint) - Distributed SDR signal detection and triangulation system with ATAK integration. `OSS` `Dual-use`
- [Anti-UAV](https://github.com/ucas-vg/Anti-UAV) - Large-scale multi-modal benchmark for UAV detection and tracking. `Dataset`
- [Anti-UAV](https://github.com/ZhaoJ9014/Anti-UAV) - Anti-UAV detection and tracking benchmark resources. `OSS` `Dataset`
- [MMAUD](https://github.com/ntu-aris/MMAUD) - Multi-modal anti-UAV dataset for miniature drone threats. `Dataset`
- [DUT-Anti-UAV](https://github.com/wangdongdut/DUT-Anti-UAV) - Anti-UAV detection and tracking resources with visible, thermal, and acoustic references. `OSS` `Dataset`
- [UAVDetectionTrackingBenchmark](https://github.com/KostadinovShalon/UAVDetectionTrackingBenchmark) - Code, configuration, and statistics for UAV detection and tracking benchmark experiments. `OSS` `Dataset`
- [UAVDETR](https://github.com/wd-sir/UAVDETR) - DETR-based anti-drone target detection research code. `OSS`
- [YOLOv12-BoT-SORT-ReID](https://github.com/wish44165/YOLOv12-BoT-SORT-ReID) - CVPR Anti-UAV Challenge tracking code using YOLOv12, BoT-SORT, and ReID. `OSS`
- [Drone Detection Dataset](https://github.com/DroneDetectionThesis/Drone-detection-dataset) - IR, visible, and audio data for drone detection systems. `Dataset`
- [SudarshanChakra Acoustic UAV Threat Detection](https://github.com/kbhujbal/SudarshanChakra-acoustic_uav_threat_detection_CNN) - Acoustic UAV detection model repository using CNN classifiers. `OSS`

## Counter-UAS Detection Infrastructure

- [Batear](https://github.com/batear-io/batear) - Low-cost ESP32-S3 acoustic drone detector with LoRa and Ethernet alerting paths. `OSS` `HW` `Dual-use`
- [Sky-Spy](https://github.com/colonelpanichacks/Sky-Spy) - Remote ID detection and mapping firmware for low-cost Wi-Fi/BLE monitoring nodes. `OSS` `Dual-use`
- [drone-mesh-mapper](https://github.com/colonelpanichacks/drone-mesh-mapper) - ESP32/Meshtastic bridge for forwarding Remote ID detections into a mesh map. `OSS`
- [TRIDENT](https://github.com/TRIDENT-2025/TRIDENT) - Tri-modal audio, visual, and RF drone-detection framework for edge-class hardware. `OSS` `Dataset`
- [RFClassification](https://github.com/IQTLabs/RFClassification) - IQT Labs RF signal-classification project for detecting and classifying drone communications using external RF datasets. `OSS`
- [Drone Detection Dataset](https://github.com/DroneDetectionThesis/Drone-detection-dataset) - IR, visible, and audio dataset for evaluating drone-detection sensor combinations. `Dataset`
- [UETT4K Anti-UAV](https://github.com/mugheessarwarawan/UETT4k-Anti-UAV) - 4K visual drone-detection dataset with annotated high-resolution imagery. `Dataset`
- [Anti-UAV410](https://github.com/HwangBo94/Anti-UAV410) - Thermal infrared anti-UAV single-object tracking benchmark. `Dataset`
- [MMAUD](https://github.com/ntu-aris/MMAUD) - Multi-modal anti-UAV dataset combining multiple sensing modalities for miniature drone detection. `Dataset`
- [SAPIENT Proto Files](https://github.com/dstl/SAPIENT-Proto-Files) - DSTL protocol buffer definitions for interoperable sensor, detection, and fusion-node messaging. `OSS` `Standard`
- [Apex SAPIENT Middleware](https://github.com/dstl/Apex-SAPIENT-Middleware) - Middleware implementation for routing, validating, filtering, archiving, and replaying SAPIENT messages. `OSS` `Standard`
- [SAPIENT Middleware And Test Harness](https://github.com/dstl/SAPIENT-Middleware-and-Test-Harness) - Legacy SAPIENT middleware and test harness retained for historical interoperability context; prefer Apex SAPIENT Middleware for current experiments. `OSS` `Archive`
- [Stone Soup](https://github.com/dstl/Stone-Soup) - Target tracking, state-estimation, data-association, and sensor-fusion framework. `OSS`
- [Tracker Component Library](https://github.com/USNavalResearchLaboratory/TrackerComponentLibrary) - U.S. NRL tracking, estimation, and sensor-fusion algorithm library. `OSS`

## AI-Assisted Drone Detection And Sensor Fusion

- [Stone Soup](https://github.com/dstl/Stone-Soup) - Framework for target tracking, state estimation, sensor management, and multi-target data association. `OSS`
- [Tracker Component Library](https://github.com/USNavalResearchLaboratory/TrackerComponentLibrary) - Tracking, estimation, gating, and assignment algorithms for multi-sensor fusion research. `OSS`
- [SAPIENT Proto Files](https://github.com/dstl/SAPIENT-Proto-Files) - Sensor and fusion-node message schema for machine-to-machine detection interoperability. `OSS` `Standard`
- [Apex SAPIENT Middleware](https://github.com/dstl/Apex-SAPIENT-Middleware) - SAPIENT middleware with validation, confidence filtering, message routing, archiving, and replay support. `OSS` `Standard`
- [TRIDENT](https://github.com/TRIDENT-2025/TRIDENT) - Multi-sensor audio, video, and RF fusion framework for real-time drone detection. `OSS` `Dataset`
- [MMDetection](https://github.com/open-mmlab/mmdetection) - OpenMMLab object-detection toolbox used for training and benchmarking modern detector architectures. `OSS`
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) - 3D object-detection toolbox for LiDAR, camera, radar-style, and multi-modal perception research. `OSS`
- [OpenPCDet](https://github.com/open-mmlab/OpenPCDet) - LiDAR-based 3D object detection framework with common point-cloud detection baselines. `OSS`
- [BEVFusion](https://github.com/mit-han-lab/bevfusion) - Bird's-eye-view multi-sensor fusion research code for camera and LiDAR perception. `OSS`
- [DeepStream Python Apps](https://github.com/NVIDIA-AI-IOT/deepstream_python_apps) - NVIDIA DeepStream Python examples for edge video analytics and multi-stream inference. `OSS`
- [DepthAI](https://github.com/luxonis/depthai) - OAK stereo-depth and edge-AI SDK for embedded perception pipelines. `OSS` `HW`
- [trackers](https://github.com/roboflow/trackers) - Clean implementations of SORT, ByteTrack, OC-SORT, BoT-SORT, and related multi-object trackers. `OSS` `Active`
- [ByteTrack](https://github.com/ifzhang/ByteTrack) - Historical multi-object tracking framework focused on associating nearly every detection box. `OSS` `Archive`
- [OC-SORT](https://github.com/noahcao/OC_SORT) - Observation-centric SORT tracker for robust motion association. `OSS`
- [BoT-SORT](https://github.com/NirAharon/BoT-SORT) - Historical multi-object tracking baseline combining motion and appearance cues. `OSS` `Archive`
- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLO training, inference, export, and deployment toolkit used across many edge-detection workflows. `OSS` `Active`
- [YOLOv12-BoT-SORT-ReID](https://github.com/wish44165/YOLOv12-BoT-SORT-ReID) - Anti-UAV Challenge tracking code combining detector, tracker, and ReID components. `OSS`

## Air Picture, C2, And Sensor Analysis

- [Open-DIS](https://github.com/open-dis) - Repository hub for Distributed Interactive Simulation implementations used in training and mission simulation. `Index` `Standard`
- [OpenC2SIM](https://github.com/OpenC2SIM) - Repository hub for Command-and-Control Systems to Simulation Systems interoperation artifacts. `Index` `Standard`
- [Boomslang C2 Simulator](https://github.com/kabartsjc/boomslang-c2-sim) - Military C2 simulation tool for doctrine, exercises, effects, cost, impact, and risk modeling. `OSS`
- [OpenAMASE](https://github.com/afrl-rq/OpenAMASE) - AFRL simulation environment for multi-UAV mission and command-and-control experimentation. `OSS`
- [OpenUxAS](https://github.com/afrl-rq/OpenUxAS) - AFRL service-oriented autonomy framework for mission-level unmanned-system coordination. `OSS`
- [ODINv2](https://github.com/syncpoint/ODINv2) - Open-source tactical mapping and C2IS with offline operation, Matrix collaboration, and military symbology. `OSS`
- [milsymbol](https://github.com/spatialillusions/milsymbol) - JavaScript MIL-STD-2525 and APP-6 military symbol generator. `OSS`
- [mil-sym-ts](https://github.com/missioncommand/mil-sym-ts) - TypeScript MIL-STD-2525D military symbol renderer. `OSS`
- [Stone Soup](https://github.com/dstl/Stone-Soup) - Tracking and state-estimation framework for fusing observations into air-picture tracks. `OSS`
- [Tracker Component Library](https://github.com/USNavalResearchLaboratory/TrackerComponentLibrary) - Estimation, assignment, and fusion algorithms useful for track management and sensor correlation. `OSS`
- [RadarSimPy](https://github.com/radarsimx/radarsimpy) - Python/C++ radar simulator for waveform, target, RCS, range-Doppler, DoA, and detection analysis. `OSS`
- [SimRadar](https://github.com/OURadar/SimRadar) - Polarimetric radar time-series emulator using motion and radar cross-section models. `OSS`
- [Airspace Encounter Models](https://github.com/Airspace-Encounter-Models) - Repository hub for tools that model encounter geometry and airspace conflict scenarios. `Index`
- [OpenARIA](https://github.com/mitre-public/open-aria) - Aviation risk-assessment tools for aircraft location data and operational safety analysis. `OSS`

## Electromagnetic, RF, Optical, And Multiphysics Simulation

- [openEMS](https://github.com/thliebig/openEMS) - Open-source finite-difference time-domain electromagnetic field solver for RF, microwave, and antenna simulation. `OSS`
- [Meep](https://github.com/NanoComp/meep) - Free FDTD electromagnetic simulation package for wave propagation, scattering, and photonics research. `OSS`
- [gprMax](https://github.com/gprMax/gprMax) - Open-source electromagnetic wave propagation simulator based on FDTD methods. `OSS`
- [SCUFF-EM](https://github.com/HomerReid/scuff-em) - Boundary-element-method suite for computational electromagnetism. `OSS`
- [LightPipes for Python](https://github.com/opticspy/lightpipes) - Optical propagation and diffraction simulation toolkit. `OSS`
- [POPPY](https://github.com/spacetelescope/poppy) - Physical optics propagation package from STScI for diffraction and wavefront simulation. `OSS`
- [PROPER](https://sourceforge.net/projects/proper-library/) - IDL, Matlab, and Python optical propagation library for modeling diffraction and wavefront propagation. `OSS`
- [Lightwave Explorer](https://github.com/NickKarpowicz/LightwaveExplorer) - Open-source nonlinear optics simulator for light-matter interaction and ultrashort pulse modeling. `OSS`
- [RadarSimPy](https://github.com/radarsimx/radarsimpy) - Radar simulator for waveform, target, RCS, and signal-processing studies that complement sensor-cued effect modeling. `OSS`

## Camouflage Detection And Remote-Sensing Tooling

- [Awesome Camouflage Vision](https://github.com/visionxiang/awesome-camouflaged-object-detection) - Curated index of camouflaged and concealed object detection, segmentation, tracking, and dataset resources. `Index`
- [Awesome COD](https://github.com/Awesome-COD/awesome-cod) - Curated index of camouflaged object detection papers, datasets, and code. `Index`
- [ZoomNeXt](https://github.com/lartpang/ZoomNeXt) - Unified image/video camouflaged object detection model and benchmark code. `OSS`
- [DCNet](https://github.com/USTCL/DCNet) - Camouflaged instance segmentation research code. `OSS`
- [MMRotate](https://github.com/open-mmlab/mmrotate) - OpenMMLab toolbox for rotated object detection in aerial and remote-sensing imagery. `OSS`
- [DOTA Devkit](https://github.com/CAPTAIN-WHU/DOTA_devkit) - Development kit for the DOTA aerial-image object detection benchmark. `OSS` `Dataset`
- [xView2 Baseline](https://github.com/DIUx-xView/xView2_baseline) - Historical baseline localization and classification models for the xView2 challenge. `OSS` `Archive`
- [JDet](https://github.com/Jittor/JDet) - Remote-sensing object detection framework with oriented bounding-box support. `OSS`
- [rschange](https://github.com/xwmaxwma/rschange) - Remote-sensing change-detection toolbox for developing and reproducing modern methods. `OSS`
- [OSSOD](https://github.com/Lans1ng/OSSOD) - Semi-supervised object detection with uncurated unlabeled data for remote-sensing images. `OSS`

## TAK, C2, And Situational Awareness

- [TAK Server](https://github.com/TAK-Product-Center/Server) - Official TAK Server development repository. `OSS`
- [FreeTAKServer](https://github.com/FreeTAKTeam/FreeTakServer) - TAK-compatible situational awareness server. `OSS`
- [OpenTAKServer](https://github.com/brian7704/OpenTAKServer) - Open-source TAK server for ATAK, iTAK, and WinTAK clients. `OSS`
- [CloudTAK](https://github.com/dfpc-coe/CloudTAK) - Open-source browser-based geospatial tools for the TAK ecosystem. `OSS`
- [Cloud-RF TAK Server](https://github.com/Cloud-RF/tak-server) - Docker setup for TAK Server. `OSS`
- [TAK Product Center](https://github.com/TAK-Product-Center) - Official TAK-related repository hub. `Index`
- [Meshtastic ATAK Plugin](https://github.com/meshtastic/ATAK-Plugin) - ATAK plugin for sending Cursor-on-Target events through Meshtastic mesh devices. `OSS`
- [takproto](https://github.com/snstac/takproto) - Python tools for sending and receiving TAK packets. `OSS`
- [pytak](https://github.com/snstac/pytak) - Python Cursor-on-Target and TAK client library. `OSS`
- [aircot](https://github.com/snstac/aircot) - Aircraft classifiers for TAK. `OSS`
- [node-CoT](https://github.com/dfpc-coe/node-CoT) - Cursor-on-Target tooling for Node.js. `OSS`
- [cotlib](https://github.com/NERVsystems/cotlib) - Go library for parsing, validating, and generating Cursor-on-Target XML messages. `OSS`
- [ODINv2](https://github.com/syncpoint/ODINv2) - Open-source C2IS with tactical mapping, MIL-STD-2525 symbology, Matrix, and offline-first design. `OSS`
- [mil-sym-ts](https://github.com/missioncommand/mil-sym-ts) - TypeScript MIL-STD-2525 D+ military symbol renderer. `OSS`
- [OmniTAK iOS](https://github.com/engindearing-projects/OmniTAK-iOS) - Open-source TAK-compatible mobile client for iOS. `OSS`
- [OmniTAK Android](https://github.com/engindearing-projects/OmniTAK-Android) - Open-source TAK-compatible mobile client for Android. `OSS`

## Battlefield C2, Drone Tasking, And Shared Air Picture

- [TAK Server](https://github.com/TAK-Product-Center/Server) - Official TAK Server repository for shared situational awareness and team data services. `OSS`
- [FreeTAKServer](https://github.com/FreeTAKTeam/FreeTakServer) - Open TAK-compatible server with federation, data packages, REST API, CoT recording, and integrations. `OSS`
- [OpenTAKServer](https://github.com/brian7704/OpenTAKServer) - Python TAK server for ATAK, iTAK, WinTAK, and web clients. `OSS`
- [CloudTAK](https://github.com/dfpc-coe/CloudTAK) - Browser-based TAK-compatible common operating picture and situational-awareness tool. `OSS`
- [FreeTAKUAS](https://github.com/FreeTAKTeam/FreeTAKUAS) - DJI drone app integrating PPLI, field of view, sensor point reporting, video streaming, and object detection with FreeTAKServer. `OSS`
- [FreeTAKHub](https://github.com/FreeTAKTeam/FreeTAKHub) - Node-RED based integration component for connecting FreeTAKServer with external systems and drone feeds. `OSS`
- [Meshtastic ATAK Plugin](https://github.com/meshtastic/ATAK-Plugin) - ATAK plugin for moving CoT events, PLI, chat, and mission data across Meshtastic meshes. `OSS`
- [takproto](https://github.com/snstac/takproto) - Python protobuf/XML tools for sending and receiving TAK packets. `OSS`
- [pytak](https://github.com/snstac/pytak) - Python Cursor-on-Target and TAK client library for rapid integration. `OSS`
- [adsbcot](https://github.com/snstac/adsbcot) - ADS-B to TAK gateway for adding aircraft tracks to a shared air picture. `OSS`
- [aiscot](https://github.com/snstac/aiscot) - AIS to TAK gateway for adding maritime vessel tracks to TAK. `OSS`
- [inrcot](https://github.com/snstac/inrcot) - Garmin inReach to Cursor-on-Target gateway for TAK products. `OSS`
- [DragonSync](https://github.com/alphafox02/DragonSync) - Gateway for publishing drone detections and ADS-B/UAT aircraft data into TAK/ATAK and MQTT. `OSS`
- [node-CoT](https://github.com/dfpc-coe/node-CoT) - TypeScript Cursor-on-Target library for TAK-related integrations. `OSS`
- [node-tak](https://github.com/dfpc-coe/node-tak) - TAK Server SDK for Node.js and TypeScript applications. `OSS`
- [py-cot](https://github.com/wcrum/py-cot) - Python Cursor-on-Target library intended for data science and machine-learning friendly workflows. `OSS`
- [OpenTAKRouter](https://github.com/darkplusplus/opentakrouter) - Open-source Cursor-on-Target router with ATAK support. `OSS`
- [OpenAMASE](https://github.com/afrl-rq/OpenAMASE) - AFRL multi-UAV simulation environment for mission-level C2 experimentation. `OSS`
- [OpenUxAS](https://github.com/afrl-rq/OpenUxAS) - AFRL autonomy framework for route planning, task ordering, and multi-vehicle coordination. `OSS`
- [ws_uspace_control_room](https://github.com/manudelu/ws_uspace_control_room) - ROS2, PX4, MQTT, and AirSim/Unreal control room for coordinated UAV fleet management. `OSS`
- [Project Starling](https://github.com/StarlingUAS/ProjectStarling) - Containerized UAV simulation-to-reality infrastructure for single and multi-UAV systems. `OSS`
- [ODINv2](https://github.com/syncpoint/ODINv2) - Offline-capable open-source tactical C2IS with mapping, Matrix collaboration, and military symbology. `OSS`
- [MAGE Server](https://github.com/ngageoint/mage-server) - NGA Mobile Awareness GEOINT Environment server for field observation collection and situational awareness. `OSS`
- [milsymbol](https://github.com/spatialillusions/milsymbol) - Military symbol renderer for operational graphics in shared pictures. `OSS`

## Field Communications And Mesh

- [Meshtastic Firmware](https://github.com/meshtastic/firmware) - LoRa-based off-grid mesh communication firmware. `OSS` `Active`
- [Meshtastic Android](https://github.com/meshtastic/Meshtastic-Android) - Android client for Meshtastic devices. `OSS`
- [Meshtastic Apple](https://github.com/meshtastic/Meshtastic-Apple) - Apple client for Meshtastic devices. `OSS`
- [Reticulum](https://github.com/markqvist/Reticulum) - Cryptography-based networking stack for building resilient local and wide-area networks. `OSS`
- [RNode Firmware](https://github.com/markqvist/RNode_Firmware) - Firmware for Reticulum-compatible LoRa radio nodes. `OSS` `HW`
- [LoRaMesher](https://github.com/LoRaMesher/LoRaMesher) - Distributed mesh communication library for LoRa devices. `OSS`

## Resilient Links, Mesh, And GNSS-Denied Navigation

- [OpenHD](https://github.com/OpenHD/OpenHD) - Open-source UAV digital video, telemetry, audio, and RC-control link ecosystem. `OSS` `Active`
- [OpenHD wifibroadcast](https://github.com/OpenHD/wifibroadcast) - Raw Wi-Fi broadcast video and telemetry library with FEC and packet validation. `OSS`
- [WFB-NG](https://github.com/svpcom/wfb-ng) - Long-range packet radio link for FPV video, telemetry, PX4, MAVLink, and RTP workflows. `OSS`
- [OpenIPC wfb-ng-openwrt](https://github.com/OpenIPC/wfb-ng-openwrt) - WFB-NG packaging for OpenWrt-based FPV and ground-station workflows. `OSS`
- [RubyFPV](https://github.com/RubyFPV/RubyFPV) - Open digital FPV radio system for video, telemetry, control, auxiliary, and custom data channels. `OSS`
- [ExpressLRS](https://github.com/ExpressLRS/ExpressLRS) - Open-source RC link with telemetry, MAVLink, PWM, SBUS, and CRSF support. `OSS` `Active`
- [MAVLink](https://github.com/mavlink/mavlink) - Lightweight drone communication protocol and message-definition repository. `OSS` `Standard`
- [MAVLink Router](https://github.com/mavlink-router/mavlink-router) - MAVLink router for serial, TCP, UDP, logging, and multi-endpoint telemetry distribution. `OSS`
- [MAVProxy](https://github.com/ArduPilot/MAVProxy) - Command-line MAVLink ground station, telemetry proxy, and routing tool. `OSS`
- [MAVROS](https://github.com/mavlink/mavros) - ROS gateway for MAVLink-enabled vehicles, payloads, and companion computers. `OSS`
- [gomavlib](https://github.com/bluenviron/gomavlib) - Go MAVLink library powering routers, monitors, and custom telemetry applications. `OSS`
- [Meshtastic Firmware](https://github.com/meshtastic/firmware) - Low-power LoRa mesh firmware for off-grid team and sensor communications. `OSS` `Active`
- [Reticulum](https://github.com/markqvist/Reticulum) - Cryptography-based networking stack for resilient local and wide-area networks over heterogeneous links. `OSS`
- [RNode Firmware](https://github.com/markqvist/RNode_Firmware) - Firmware for Reticulum-compatible LoRa radio nodes. `OSS` `HW`
- [LoRaMesher](https://github.com/LoRaMesher/LoRaMesher) - Distributed LoRa mesh communication library. `OSS`
- [FlyNetSim](https://github.com/saburhb/FlyNetSim) - Historical synchronized UAV-network simulator combining ns-3 and ArduPilot. `OSS` `Archive`
- [ADOS Mission Control](https://github.com/altnautica/ADOSMissionControl) - Browser-based ground control station for ArduPilot, PX4, Betaflight, and INAV drones. `OSS`
- [ADOS Drone Agent](https://github.com/altnautica/ADOSDroneAgent) - Companion-computer agent for MAVLink proxying, video pipeline, telemetry relay, cloud connectivity, and ground-station mode. `OSS`
- [srsRAN Project](https://github.com/srsran/srsRAN_Project) - Historical open-source 4G/5G RAN stack for private-network and cellular-link experimentation. `OSS` `Archive`
- [OpenAirInterface 5G](https://github.com/OPENAIRINTERFACE/openairinterface5g) - Open-source 5G RAN and core components for SDR-backed cellular-network research. `OSS`
- [Open5GS](https://github.com/open5gs/open5gs) - Open-source 4G/5G core network implementation for private cellular testbeds. `OSS`
- [openwifi](https://github.com/open-sdr/openwifi) - Open-source IEEE 802.11 Wi-Fi baseband FPGA design, driver, and software stack. `OSS` `HW`
- [GNSS-SDR](https://github.com/gnss-sdr/gnss-sdr) - Software-defined GNSS receiver for GNSS monitoring, analysis, and receiver research. `OSS`
- [gnss-sdr-1pps](https://github.com/oscimp/gnss-sdr-1pps) - GNSS-SDR fork focused on 1-PPS, spoofing detection, and jamming-detection research. `OSS`
- [WildNav](https://github.com/TIERS/wildnav) - GNSS-free drone localization by matching onboard imagery against satellite maps. `OSS`
- [GISNav](https://github.com/hmakelin/gisnav) - ROS2 map-based visual navigation for estimating drone position from camera imagery and GIS maps. `OSS`
- [OpenVINS](https://github.com/rpng/open_vins) - Visual-inertial navigation research platform for camera-IMU localization. `OSS`
- [MINS](https://github.com/rpng/MINS) - Multi-sensor-aided inertial navigation system combining IMU, camera, LiDAR, GNSS, and wheel data. `OSS`

## Space, Satellite Communications, And ISR

- [SatDump](https://github.com/SatDump/SatDump) - Generic satellite data processing, decoding, and live reception software. `OSS`
- [SatNOGS Client](https://gitlab.com/librespacefoundation/satnogs/satnogs-client) - Libre Space Foundation open-source satellite ground-station client. `OSS`
- [SatNOGS Network](https://gitlab.com/librespacefoundation/satnogs/satnogs-network) - Open network for scheduling and sharing satellite ground-station observations. `OSS`
- [gr-satellites](https://github.com/daniestevez/gr-satellites) - GNU Radio out-of-tree module for decoding telemetry from many satellites. `OSS`
- [Skyfield](https://github.com/skyfielders/python-skyfield) - Python astronomy library for satellite positions, passes, and ephemeris calculations. `OSS`
- [python-sgp4](https://github.com/brandon-rhodes/python-sgp4) - Python implementation of SGP4 satellite orbit propagation. `OSS`
- [Orekit](https://gitlab.orekit.org/orekit/orekit) - Open-source space-dynamics library for orbit propagation, estimation, and mission analysis. `OSS`
- [poliastro](https://github.com/poliastro/poliastro) - Historical Python astrodynamics and orbital mechanics library. `OSS` `Archive`
- [Hypatia](https://github.com/snkas/hypatia) - Historical LEO satellite network simulator and visualizer. `OSS` `Archive`
- [Orbit Predictor](https://github.com/satellogic/orbit-predictor) - Python satellite pass and orbit prediction library. `OSS`
- [CelesTrak](https://celestrak.org/) - Public orbital element data, satellite catalog resources, and spaceflight dynamics references. `Dataset` `Dual-use`
- [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) - Fire Information for Resource Management System with near-real-time thermal anomaly data. `Dataset`
- [Cesium](https://github.com/CesiumGS/cesium) - Open-source 3D geospatial visualization engine for time-dynamic tracks and globe visualization. `OSS`
- [OpenSpace](https://github.com/OpenSpace/OpenSpace) - Open-source interactive data visualization software for space and Earth science. `OSS`
- [WorldWind Java](https://github.com/NASAWorldWind/WorldWindJava) - NASA virtual globe SDK for geospatial visualization. `OSS` `Archive`

## Video, Telemetry Links, And Payload Streaming

- [OpenHD](https://github.com/OpenHD/OpenHD) - Open-source digital video link ecosystem for HD video, two-way telemetry, audio, and RC control over one channel. `OSS` `Active`
- [OpenHD wifibroadcast](https://github.com/OpenHD/wifibroadcast) - C++ library for Wi-Fi broadcast video and telemetry streaming with FEC and packet validation. `OSS`
- [QOpenHD](https://github.com/OpenHD/QOpenHD) - OpenHD companion application for video display, OSD, MAVLink settings, and ground-station control. `OSS`
- [WFB-NG](https://github.com/svpcom/wfb-ng) - Long-range packet radio link based on raw Wi-Fi for FPV video, telemetry, PX4, MAVLink, and RTP workflows. `OSS`
- [RubyFPV](https://github.com/RubyFPV/RubyFPV) - Open digital FPV radio system for video, telemetry, control, auxiliary, and custom data streams. `OSS`
- [ExpressLRS](https://github.com/ExpressLRS/ExpressLRS) - High-performance open-source RC radio link with telemetry, MAVLink, PWM, SBUS, and CRSF support. `OSS` `Active`
- [OpenVTx](https://github.com/OpenVTx/OpenVTx) - Open-source FPV video-transmitter firmware supporting MSP, SmartAudio, and Tramp protocols. `OSS`
- [MAVLink Router](https://github.com/mavlink-router/mavlink-router) - MAVLink packet router for UART, UDP, TCP, logging, and multi-endpoint telemetry routing. `OSS`
- [mavp2p](https://github.com/bluenviron/mavp2p) - Flexible MAVLink proxy, bridge, and router for serial, UDP, TCP, broadcast, Docker, and OpenWrt-style deployments. `OSS`
- [MAVProxy](https://github.com/ArduPilot/MAVProxy) - Command-line MAVLink ground station, router, and telemetry proxy for ArduPilot-oriented workflows. `OSS`
- [MAVROS](https://github.com/mavlink/mavros) - MAVLink communication node and gateway for ROS-based companion-computer and payload integrations. `OSS` `Active`
- [OpenIPC Firmware](https://github.com/OpenIPC/firmware) - Alternative open firmware for IP camera hardware used in FPV and embedded video systems. `OSS`
- [OpenIPC Waybeam VENC](https://github.com/OpenIPC/waybeam_venc) - Standalone H.265/H.264 video encoder and RTP streamer for low-latency FPV and IP camera applications. `OSS`
- [OpenIPC Aviateur](https://github.com/OpenIPC/aviateur) - Cross-platform OpenIPC FPV ground station for Linux, Windows, and macOS. `OSS`

## Geospatial Intelligence, Mapping, And Imagery

- [OpenDroneMap](https://github.com/OpenDroneMap/ODM) - Command-line toolkit for drone imagery processing and reconstruction. `OSS`
- [WebODM](https://github.com/OpenDroneMap/WebODM) - Web interface for processing aerial imagery. `OSS`
- [DroneDB](https://github.com/DroneDB/DroneDB) - Open-source platform for geospatial data storage, visualization, and sharing. `OSS`
- [GeoQ](https://github.com/ngageoint/geoq) - Historical NGA tasking and workflow platform for geographic event response. `OSS` `Archive`
- [Hootenanny](https://github.com/ngageoint/hootenanny) - Geospatial conflation and data translation tools. `OSS`
- [GeoPackage JS](https://github.com/ngageoint/geopackage-js) - JavaScript GeoPackage library. `OSS`
- [MAGE Server](https://github.com/ngageoint/mage-server) - Mobile Awareness GEOINT Environment server. `OSS`
- [sarpy](https://github.com/ngageoint/sarpy) - Python tools for reading, writing, and processing SAR data. `OSS`
- [MATLAB SAR](https://github.com/ngageoint/MATLAB_SAR) - MATLAB tools for synthetic aperture radar data. `OSS`
- [QGIS](https://github.com/qgis/QGIS) - Free and open-source geographic information system for viewing, editing, analysis, and cartography. `OSS`
- [TorchGeo](https://github.com/microsoft/torchgeo) - PyTorch datasets, samplers, transforms, and pretrained models for geospatial data. `OSS`
- [Raster Vision](https://github.com/azavea/raster-vision) - Deep-learning framework for satellite, aerial, and drone imagery. `OSS`
- [segment-geospatial](https://github.com/opengeos/segment-geospatial) - Geospatial image segmentation using Segment Anything-style models. `OSS`
- [Prithvi-EO-2.0](https://github.com/NASA-IMPACT/Prithvi-EO-2.0) - NASA IMPACT repository for the Prithvi-EO-2.0 geospatial foundation model release. `OSS`
- [TerraTorch](https://github.com/IBM/terratorch) - Framework for fine-tuning geospatial foundation models. `OSS`
- [RADAR](https://github.com/Syntax-Error-1337/radar) - Open-source real-time geospatial intelligence dashboard. `OSS` `Dual-use`
- [Crucix](https://github.com/calesthio/Crucix) - Personal intelligence dashboard aggregating satellite fire detection, flight tracking, radiation monitoring, sanctions, conflict, and other open feeds. `OSS`
- [SkyIntel](https://github.com/0xchamin/skyintel) - Open sky intelligence app and MCP server for flight and satellite tracking from public data. `OSS`

## Critical Infrastructure Protection And Damage Assessment

- [Ukraine Damage Mapping Tool](https://github.com/prs-eth/ukraine-damage-mapping-tool) - Open-source tool for mapping war destruction in Ukraine using Sentinel-1 time series. `OSS`
- [Open Access Damage Detection Using Sentinel-1](https://oballinger.github.io/PWTT/) - Open-access Sentinel-1 damage-detection platform and Battle Damage Dashboard resources. `Dataset`
- [SKAI](https://github.com/google-research/skai) - Google Research tool for automatic building damage assessment from aerial imagery. `OSS`
- [Microsoft Building Damage Assessment](https://github.com/microsoft/building-damage-assessment) - Toolkit for building damage assessments from satellite, aerial, and SAR imagery. `OSS`
- [xView2 Baseline](https://github.com/DIUx-xView/xView2_baseline) - Historical baseline models for post-disaster building localization and damage classification in the xView2 challenge. `OSS` `Archive`
- [xBD Road Damage Assessment](https://github.com/seunghyeokleeme/xBD_road_damage_assessment) - Deep-learning road-damage detection and assessment with satellite imagery. `OSS`
- [rschange](https://github.com/xwmaxwma/rschange) - Change-detection toolbox for remote-sensing imagery. `OSS`
- [xarray-sentinel](https://github.com/bopen/xarray-sentinel) - Xarray backend for accessing and exploring Copernicus Sentinel-1 data products. `OSS`
- [TorchGeo](https://github.com/microsoft/torchgeo) - PyTorch geospatial datasets, samplers, transforms, and pretrained models. `OSS`
- [Raster Vision](https://github.com/azavea/raster-vision) - Deep-learning framework for satellite, aerial, and drone imagery. `OSS`
- [OpenInfraMap](https://github.com/openinframap/openinframap) - OpenStreetMap-based infrastructure map for power, telecom, petroleum, water, and other networks. `OSS`
- [OpenDSSDirect.py](https://github.com/dss-extensions/OpenDSSDirect.py) - Python interface to OpenDSS for electric power distribution system studies. `OSS`
- [pandapower](https://github.com/e2nIEE/pandapower) - Python power-system analysis tool for grid modeling, power flow, and optimal power flow. `OSS`
- [PyPSA](https://github.com/PyPSA/PyPSA) - Python for Power System Analysis, covering generation, storage, networks, and optimization. `OSS`
- [GridCal](https://github.com/SanPen/GridCal) - Power systems simulation and optimization tool. `OSS`
- [GridLAB-D](https://github.com/gridlab-d/gridlab-d) - Distribution-grid simulation platform. `OSS`
- [WNTR](https://github.com/USEPA/WNTR) - EPA water network tool for resilience modeling and disruption analysis. `OSS`
- [EPANET](https://github.com/OpenWaterAnalytics/EPANET) - Open-source hydraulic and water-quality modeling toolkit. `OSS`
- [OpenQuake Engine](https://github.com/gem/oq-engine) - Open-source hazard and risk calculation engine for infrastructure and regional risk analysis. `OSS`

## Emergency Response, Search And Rescue, And Disaster Mapping

- [SAREnv](https://github.com/namurproject/SAREnv) - Dataset and evaluation framework for UAV-based search-and-rescue algorithms, scenarios, metrics, and planners. `OSS` `Dataset`
- [SeaDronesSee](https://github.com/Ben93kie/SeaDronesSee) - Maritime search-and-rescue UAV vision benchmark with object detection, single-object tracking, and multi-object tracking tracks. `OSS` `Dataset`
- [AIR](https://github.com/Accenture/AIR) - Aerial Inspection RetinaNet framework for detecting visual clues in drone imagery during land search-and-rescue missions. `OSS`
- [Drone Swarm Search Environment](https://github.com/pfeinsper/drone-swarm-search) - PettingZoo-based simulation environment for drone-swarm search strategies in maritime SAR scenarios. `OSS`
- [UAV-SaR-Tracking](https://github.com/spsingh37/UAV-SaR-Tracking) - ROS package for UAV search-and-rescue navigation experiments with reinforcement learning and PID control. `OSS`
- [Search Management Map](https://github.com/canterbury-air-patrol/search-management-map) - Django, Leaflet, and PostGIS application for planning and managing search-and-rescue missions. `OSS`
- [Resgrid Core](https://github.com/Resgrid/Core) - Open-source dispatch, personnel, AVL, and emergency-management platform for first-response organizations. `OSS`
- [OpenAerialMap](https://github.com/hotosm/openaerialmap) - Open platform for sharing openly licensed aerial imagery useful for disaster mapping and humanitarian response. `OSS`
- [HOT fAIr](https://github.com/hotosm/fAIr) - Humanitarian OpenStreetMap AI-assisted mapping service for detecting map features from satellite and UAV imagery. `OSS`
- [Pyronear Pyro Engine](https://github.com/pyronear/pyro-engine) - Wildfire detection engine for edge devices and low-cost early-warning deployments. `OSS`
- [Pyronear Pyro Vision](https://github.com/pyronear/pyro-vision) - Computer-vision library for wildfire detection models in PyTorch, ONNX, and edge inference workflows. `OSS`
- [ForeFire](https://github.com/forefireAPI/forefire) - Open-source wildfire spread simulation engine for research and operational forecasting. `OSS`
- [SimFire](https://github.com/mitrefireline/simfire) - Python wildfire simulator for reinforcement-learning and emergency-response research. `OSS`
- [fire-rs-saop](https://github.com/laas/fire-rs-saop) - Historical situation assessment and observation-planning tools for wildfire monitoring with UAV fleets. `OSS` `Archive`
- [OpenDrift Leeway WebGUI](https://github.com/digitalfabrik/opendrift-leeway-webgui) - Experimental web interface for OpenDrift leeway simulations in search-and-rescue operations. `OSS`

## ADS-B And Air Tracking

- [dump1090](https://github.com/antirez/dump1090) - Mode S / ADS-B decoder for RTL-SDR devices. `OSS`
- [readsb](https://github.com/wiedehopf/readsb) - ADS-B decoder derived from dump1090-fa. `OSS`
- [tar1090](https://github.com/wiedehopf/tar1090) - Web interface for aircraft tracking with readsb/dump1090-style backends. `OSS`
- [Stratux](https://github.com/b3nn0/stratux) - Open-source DIY ADS-B and flight-data system for aviation situational awareness. `OSS` `HW`
- [pyModeS](https://github.com/junzis/pyModeS) - Python decoder for Mode-S and ADS-B messages. `OSS`
- [adsb_deku](https://github.com/rsadsb/adsb_deku) - Rust ADS-B decoder and terminal radar application. `OSS`
- [dump1090_rs](https://github.com/rsadsb/dump1090_rs) - Multi-SDR Rust translation of dump1090 for ADS-B demodulation. `OSS`
- [Tracker Component Library](https://github.com/USNavalResearchLaboratory/TrackerComponentLibrary) - NRL tracking and estimation algorithms. `OSS`

## Training And Simulation Interoperability

- [Open-DIS](https://github.com/open-dis) - Repository hub for Distributed Interactive Simulation implementations. `Index` `Standard`
- [OpenC2SIM](https://github.com/OpenC2SIM) - Repository hub for Command-and-Control Simulation Interoperation artifacts and reference implementations. `Index` `Standard`
- [DISPluginForUnreal](https://github.com/AF-GRILL/DISPluginForUnreal) - Legacy Unreal Engine 4 plugin for Distributed Interactive Simulation. `OSS` `Archive`
- [DISPluginForUnity](https://github.com/AF-GRILL/DISPluginForUnity) - Unity plugin for Distributed Interactive Simulation. `OSS`
- [IVCT Framework](https://github.com/IVCTool/IVCT_Framework) - Interoperability verification and certification framework for HLA federates. `OSS`
- [NETN-FOM](https://github.com/AMSP-04/NETN-FOM) - NATO Education and Training Network Federation Object Model artifacts. `Standard`
- [Stone Soup](https://github.com/dstl/Stone-Soup) - DSTL framework for target tracking and state estimation research. `OSS`
- [SAPIENT Proto Files](https://github.com/dstl/SAPIENT-Proto-Files) - DSTL protocol buffer definitions for SAPIENT sensor interoperability. `OSS` `Standard`
- [SAPIENT Middleware And Test Harness](https://github.com/dstl/SAPIENT-Middleware-and-Test-Harness) - Legacy SAPIENT middleware and test harness retained for historical interoperability context; prefer Apex SAPIENT Middleware for current experiments. `OSS` `Archive`

## High-Fidelity Simulation, Digital Twins, And Synthetic Data

- [Project AirSim](https://github.com/iamaisim/ProjectAirSim) - Open-source evolution of AirSim for high-fidelity drone, robot, and autonomous-system simulation in Unreal Engine. `OSS` `Active`
- [AirSim](https://github.com/microsoft/AirSim) - Unreal/Unity simulator for drones, cars, autonomy research, PX4, ArduPilot, and synthetic-data generation. `OSS` `Archive`
- [Drone Colosseum](https://github.com/gist-ailab/drone-colosseum) - AirSim-derived open-source simulator for autonomous robotics on Unreal Engine 5 with PX4 and ArduPilot support. `OSS`
- [Pegasus Simulator](https://github.com/PegasusSimulator/PegasusSimulator) - NVIDIA Isaac Sim framework for multirotor simulation with PX4 and ArduPilot integration. `OSS` `Active`
- [Gazebo Sim](https://github.com/gazebosim/gz-sim) - Open-source robotics simulator with high-fidelity physics, rendering, sensors, GUI, plugins, and transport APIs. `OSS` `Active`
- [PX4 Gazebo Models](https://github.com/PX4/PX4-gazebo-models) - PX4-maintained Gazebo models, worlds, and helper script for local GZ simulation. `OSS`
- [ArduPilot Gazebo](https://github.com/ArduPilot/ardupilot_gazebo) - Official ArduPilot Gazebo plugin and models for SITL simulation with current Gazebo releases. `OSS` `Active`
- [PX4 Simulation with ROS2](https://github.com/ParsaKhaledi/px4_sim_ros2) - Dockerized PX4, ROS2, Gazebo, Nav2, and QGroundControl simulation environment. `OSS`
- [XTDrone](https://github.com/robin-shaun/XTDrone) - PX4, ROS, and Gazebo UAV simulation platform for multi-rotor, fixed-wing, VTOL, and swarm experiments. `OSS`
- [MRS UAV Gazebo Simulation](https://github.com/ctu-mrs/mrs_uav_gazebo_simulation) - CTU MRS metapackage for Gazebo and PX4 SITL UAV simulation. `OSS`
- [ArduPilot Multiagent Simulation](https://github.com/aau-cns/Ardupilot_Multiagent_Simulation) - ArduPilot, ROS2, and Gazebo simulation environment for spawning and controlling multiple drones. `OSS`
- [ws_uspace_control_room](https://github.com/manudelu/ws_uspace_control_room) - ROS2, PX4, MQTT, and AirSim/Unreal control room for coordinated UAV fleet management and digital twins. `OSS`
- [FlyAwareV2](https://github.com/LTTM/FlyAwareV2) - Code and tooling for a multimodal cross-domain UAV urban-scene dataset combining CARLA-generated and real UAV imagery. `OSS` `Dataset`
- [Syndrone](https://github.com/LTTM/Syndrone) - Code and tools for building and simulating the SynDrone multimodal UAV dataset. `OSS` `Dataset`
- [Griffin](https://github.com/wang-jh18-SVM/Griffin) - Aerial-ground cooperative 3D perception benchmark using CARLA-AirSim co-simulation. `OSS` `Dataset`
- [Baseball Avoidance Multirotor](https://github.com/nasa/Baseball-Avoidance-Multirotor-BAM) - NASA simulation for autonomous multirotor collision-avoidance research with Simulink, ROS2, Unreal, AirSim, and Colosseum interfaces. `OSS`

## Ground, Surface, And Underwater Robotics

- [ugv_nav4d_ros2](https://github.com/dfki-ric/ugv_nav4d_ros2) - ROS2 wrapper for 4D path planning for autonomous ground vehicles. `OSS`
- [NASA Open Source Rover](https://github.com/nasa-jpl/open-source-rover) - Build-it-yourself six-wheel rover inspired by Mars rovers. `OSS` `HW`
- [ArduPilot Rover And Sub](https://github.com/ArduPilot/ardupilot) - ArduPilot vehicle code for ground rovers, boats, ROVs, and submarines. `OSS` `Active`
- [m2020-urdf-models](https://github.com/nasa-jpl/m2020-urdf-models) - Perseverance and Ingenuity URDF models for visualization. `OSS`

## UGV Logistics, CASEVAC, And Ground Robotics

- [Open Source Rover](https://github.com/nasa-jpl/open-source-rover) - NASA JPL open rover hardware and software project for ground robotics education and experimentation. `OSS` `HW`
- [Linorobot](https://github.com/linorobot/linorobot) - Legacy ROS1 ground robot platform supporting 2WD, 4WD, Ackermann, and mecanum bases. `OSS` `HW` `Archive`
- [Linorobot2](https://github.com/linorobot/linorobot2) - ROS2 version of the Linorobot autonomous ground robot stack. `OSS` `HW`
- [Navigation2](https://github.com/ros-navigation/navigation2) - ROS2 navigation stack for localization, planning, control, behavior trees, and obstacle avoidance. `OSS` `Active`
- [Clearpath Simulator](https://github.com/clearpathrobotics/clearpath_simulator) - ROS2/Gazebo simulator packages for Clearpath UGVs. `OSS`
- [Husky](https://github.com/husky/husky) - Common ROS packages for the Clearpath Husky UGV platform. `OSS`
- [Rover Robotics ROS2](https://github.com/RoverRobotics/roverrobotics_ros2) - ROS2 packages, URDFs, simulation, SLAM, and navigation support for Rover Robotics platforms. `OSS`
- [AgileX UGV SDK](https://github.com/agilexrobotics/ugv_sdk) - SDK for AgileX UGV chassis control and integration. `OSS`
- [AgileX Hunter ROS2](https://github.com/agilexrobotics/hunter_ros2) - ROS2 driver package for the AgileX Hunter UGV platform. `OSS`
- [AgileX Gazebo Simulation](https://github.com/agilexrobotics/ugv_gazebo_sim) - Gazebo simulation packages and URDF models for AgileX UGV chassis. `OSS`
- [OpenPodCar V2](https://github.com/Rak-r/OpenPodCar_V2) - Open hardware and software ROS2 platform for Ackermann autonomous ground-vehicle research. `OSS` `HW`
- [Autoware](https://github.com/autowarefoundation/autoware) - ROS2-based autonomous driving stack and metapackage for ground-vehicle autonomy. `OSS`
- [RELLIS-3D](https://github.com/unmannedlab/RELLIS-3D) - Multi-modal off-road robotics dataset with camera, LiDAR, GPS, IMU, and ROS bag data. `Dataset`
- [WarNav](https://arxiv.org/abs/2511.15429) - Conflict-scene navigable-zone segmentation benchmark for autonomous ground vehicle research. `Paper` `Dataset`
- [marsupial_simulator_ros2](https://github.com/robotics-upo/marsupial_simulator_ros2) - ROS2/Gazebo simulator for tethered UAV-UGV marsupial systems. `OSS`
- [ROS2swarm](https://github.com/ROS2swarm/ROS2swarm) - Historical ROS2 framework and library for swarm behaviors across robot platforms. `OSS` `Archive`

## Maritime USVs And Naval Drone Operations

- [MOOS-IvP](https://github.com/moos-ivp/moos-ivp) - Open-source autonomy modules for robotic platforms, especially autonomous marine vehicles. `OSS`
- [Virtual RobotX](https://github.com/osrf/vrx) - Gazebo and ROS2 simulation environment for uncrewed surface vehicle autonomy and RobotX-style tasks. `OSS` `Active`
- [BlueOS](https://github.com/bluerobotics/BlueOS) - Open-source onboard platform for ROV, USV, and robotic-system operation, development, and expansion. `OSS`
- [BlueOS Cockpit](https://github.com/bluerobotics/cockpit) - Cross-platform ground control station for remote vehicles, including ROVs and boats. `OSS`
- [ArduPilot Rover And Sub](https://github.com/ArduPilot/ardupilot) - ArduPilot vehicle code for boats, surface rovers, ROVs, and submarines. `OSS` `Active`
- [QGroundControl](https://github.com/mavlink/qgroundcontrol) - MAVLink ground control station used across aerial, surface, and underwater unmanned systems. `OSS` `Active`
- [MAVLink](https://github.com/mavlink/mavlink) - Common messaging protocol for unmanned vehicles, payloads, GCS, and marine autopilot integrations. `OSS` `Standard`
- [OtterROS](https://github.com/offroad-robotics/otter_ros) - ROS2 packages for research with the Maritime Robotics Otter USV. `OSS`
- [MultiVessel Simulation](https://github.com/FieldRoboticsLab/MultiVessel_Simulation) - Virtual RobotX-based multi-vessel simulation with configurable routes and AIS-derived scenarios. `OSS`
- [PyQuaticus](https://github.com/mit-ll-trusted-autonomy/pyquaticus) - PettingZoo multi-agent maritime environment with USV dynamics and OpenStreetMap-based aquatic regions. `OSS`
- [Plankton](https://github.com/Liquid-ai/Plankton) - Historical ROS2/Gazebo maritime robotics simulator built from UUV Simulator components. `OSS` `Archive`
- [UUV Simulator](https://github.com/uuvsimulator/uuv_simulator) - Gazebo and ROS packages for underwater unmanned vehicle simulation. `OSS` `Archive`
- [Stonefish](https://github.com/patrykcieslak/stonefish) - C++ simulation library for marine robots with underwater rendering, sensors, and hydrodynamics. `OSS`
- [Orca4](https://github.com/clydemcqueen/orca4) - ROS2 AUV project based on BlueROV2, ArduSub, Gazebo, and Navigation2. `OSS`
- [UNav-Sim](https://github.com/open-airlab/UNav-Sim) - Unreal Engine and AirSim-based underwater robotics simulator with ROS support. `OSS`
- [SeaDronesSee](https://github.com/Ben93kie/SeaDronesSee) - Maritime search-and-rescue UAV vision benchmark for object detection and tracking. `OSS` `Dataset`
- [Drone Swarm Search Environment](https://github.com/pfeinsper/drone-swarm-search) - PettingZoo simulation environment for drone-swarm maritime search strategies. `OSS`
- [aiscot](https://github.com/snstac/aiscot) - AIS to TAK gateway for integrating ship tracks into a shared operational picture. `OSS`

## Mine Action, EOD, And Humanitarian Demining

- [MineInsight](https://github.com/mariomlz99/MineInsight) - Multi-sensor, multi-spectral dataset for humanitarian demining robotics in off-road environments. `Dataset`
- [MineInsight Paper](https://arxiv.org/abs/2506.04842) - Paper describing the MineInsight UGV and robotic-arm demining dataset. `Paper` `Dataset`
- [SULAND Dataset](https://github.com/miccunifi/SULAND-Dataset) - Surface landmine detection dataset for optical-imaging research. `Dataset`
- [Demining Research Community Seeded Field Dataset](https://zenodo.org/records/19100554) - Multi-modal seeded field dataset for landmine and UXO detection research. `Dataset`
- [Humanitarian Demining GPR Dataset](https://zenodo.org/records/7348797) - Humanitarian demining research artifact with GPR data, reports, code references, and post-processing material. `Dataset`
- [AMLID](https://arxiv.org/abs/2512.18738) - Adaptive multispectral landmine identification dataset for drone-based detection research. `Paper` `Dataset`
- [TextMine](https://arxiv.org/abs/2509.15098) - LLM-powered knowledge extraction and ontology work for humanitarian mine-action documents. `Paper` `Dataset`

## Research Datasets

- [Anti-UAV410](https://github.com/HwangBo94/Anti-UAV410) - Thermal infrared anti-UAV tracking benchmark. `Dataset`
- [MMAUD](https://github.com/ntu-aris/MMAUD) - Multi-modal anti-UAV dataset. `Dataset`
- [VisDrone Dataset](https://github.com/VisDrone/VisDrone-Dataset) - Aerial image and video object detection and tracking benchmark resources. `Dataset`
- [Drone-detection-dataset](https://github.com/DroneDetectionThesis/Drone-detection-dataset) - IR, visible, and audio drone-detection data. `Dataset`
- [EuRoC MAV Dataset](https://projects.asl.ethz.ch/datasets/euroc-mav/) - Visual-inertial MAV datasets for SLAM and state-estimation research. `Dataset`
- [UZH FPV Drone Racing Dataset](https://fpv.ifi.uzh.ch/datasets/) - Visual-inertial, event-camera, ground-truth, and FPV data for aggressive drone-racing state-estimation research. `Dataset`

## Related Topics To Watch

- [GitHub topic: uav](https://github.com/topics/uav)
- [GitHub topic: drones](https://github.com/topics/drones)
- [GitHub topic: drone-detection](https://github.com/topics/drone-detection)
- [GitHub topic: counter-uas](https://github.com/topics/counter-uas)
- [GitHub topic: sensor-fusion](https://github.com/topics/sensor-fusion)
- [GitHub topic: directed-energy](https://github.com/topics/directed-energy)
- [GitHub topic: remote-sensing](https://github.com/topics/remote-sensing)
- [GitHub topic: cursor-on-target](https://github.com/topics/cursor-on-target)
- [GitHub topic: tak](https://github.com/topics/tak)
- [GitHub topic: mavlink](https://github.com/topics/mavlink)
- [GitHub topic: mesh-networks](https://github.com/topics/mesh-networks)
- [GitHub topic: ugv](https://github.com/topics/ugv)
- [GitHub topic: landmine-detection](https://github.com/topics/landmine-detection)
- [GitHub topic: usv](https://github.com/topics/usv)
- [GitHub topic: maritime-robotics](https://github.com/topics/maritime-robotics)
- [GitHub topic: satellite](https://github.com/topics/satellite)
- [GitHub topic: satellite-imagery](https://github.com/topics/satellite-imagery)
- [GitHub topic: additive-manufacturing](https://github.com/topics/additive-manufacturing)
- [GitHub topic: ros2](https://github.com/topics/ros2)

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

Every entry should be useful, public, clearly described, and relevant to the repository scope.

Maintenance checks and duplicate-review workflow are documented in [docs/maintenance.md](docs/maintenance.md). Allowed metadata tags are defined in [data/tags.json](data/tags.json).

## License

This list is released under [CC0-1.0](LICENSE). You may copy, remix, and reuse it freely.
