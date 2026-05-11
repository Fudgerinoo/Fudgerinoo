Hi I'm @Fudgerinoo
I love all things IT, and have been practicing network and systems engineering in linux

Automated BGP Provisioning & Router-on-a-Stick Lab

# Overview
This project simulates a modern 5G Telco infrastructure (CU/DU/RU nodes) using a Type-1 hypervisor architecture. It includes a custom Python automation tool designed to dynamically fetch, modify, and push BGP configurations to a centralized REST API controller.

# Core Technologies
* **Virtualization:** KVM / libvirt (`virt-manager`)
* **Networking:** 802.1Q VLAN Tagging, Dual-Stack IPv6 ULA routing, Linux Bridges
* **OS:** Ubuntu Server 24.04 (Headless)
* **Automation:** Python 3 (`requests`, `json`, `argparse`), SSH Key-Based Auth

# Architecture
The lab environment is built using a "Router-on-a-Stick" topology to conserve host resources. A single Ubuntu Server VM acts as the gateway, utilizing `netplan` to split a single virtual NIC into multiple broadcast domains (VLAN 10 Management, VLAN 20 Data), as well as configuring 'nftables' to control data moving through the gateway 

# Usage: Python API Automation Tool
The included Python script intercepts BGP configuration payloads, modifies operational states and hold timers, and pushes the updated JSON to the SDN controller.

**To run the provisioning script:**
`python3 bgp_provision.py --gurl https://httpbin.org/post --peer 192.168.122.105 --status up`
args = --gurl, --purl, --peer, --status, 

<!---
Fudgerinoo/Fudgerinoo is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
