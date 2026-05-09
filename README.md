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

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

Every entry should be useful, public, clearly described, and relevant to the repository scope.

## License

This list is released under [CC0-1.0](LICENSE). You may copy, remix, and reuse it freely.
