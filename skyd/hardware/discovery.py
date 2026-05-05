#!/usr/bin/env python3
"""
skyd hardware discovery
Queries connected devices and builds a hardware manifest.
skyd will use this manifest to generate or load appropriate drivers.
"""

import os
import logging

log = logging.getLogger("skyd.hardware")


def discover():
    """
    Scan all connected hardware and return a manifest dict.
    Uses /sys and /proc on Linux as initial data sources.
    Eventually skyd will generate its own discovery mechanisms.
    """
    manifest = {}

    # PCI devices
    manifest["pci"] = _scan_pci()

    # USB devices
    manifest["usb"] = _scan_usb()

    # Block devices (storage)
    manifest["block"] = _scan_block()

    # Network interfaces
    manifest["network"] = _scan_network()

    log.info(f"hardware manifest built: {len(manifest)} categories")
    return manifest


def _scan_pci():
    devices = []
    pci_path = "/sys/bus/pci/devices"
    if os.path.exists(pci_path):
        for dev in os.listdir(pci_path):
            devices.append({"id": dev, "path": f"{pci_path}/{dev}"})
    return devices


def _scan_usb():
    devices = []
    usb_path = "/sys/bus/usb/devices"
    if os.path.exists(usb_path):
        for dev in os.listdir(usb_path):
            devices.append({"id": dev})
    return devices


def _scan_block():
    devices = []
    block_path = "/sys/block"
    if os.path.exists(block_path):
        for dev in os.listdir(block_path):
            devices.append({"name": dev})
    return devices


def _scan_network():
    interfaces = []
    net_path = "/sys/class/net"
    if os.path.exists(net_path):
        for iface in os.listdir(net_path):
            interfaces.append({"name": iface})
    return interfaces
