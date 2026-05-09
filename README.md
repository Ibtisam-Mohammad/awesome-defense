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

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

Every entry should be useful, public, clearly described, and relevant to the repository scope.

## License

This list is released under [CC0-1.0](LICENSE). You may copy, remix, and reuse it freely.
