# skyd Kernel Module

This directory will contain the Linux kernel module that gives skyd ring 0 access.

## Plan

1. Start with a loadable kernel module (LKM) — safer for early development
2. Hook into key kernel subsystems (memory, I/O, process scheduling)
3. Expose a secure channel between the kernel and skyd userspace process
4. Gradually move more of skyd into kernel space as trust is established

## Files (coming soon)

- `skyd_module.c` — main kernel module
- `skyd_hooks.c` — kernel hook implementations  
- `Makefile` — build system for the kernel module

## Build Requirements

- Linux kernel headers
- gcc
- make
