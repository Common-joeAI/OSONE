#!/bin/bash
# OSONE Arch Linux base setup
# Installs the minimal environment needed to run skyd

set -e

echo "[OSONE] Setting up minimal Arch base..."

# Update system
pacman -Syu --noconfirm

# Core dependencies
pacman -S --noconfirm \
  base-devel \
  python \
  python-pip \
  git \
  cmake \
  gcc \
  make \
  curl \
  wget \
  htop \
  linux-headers

# llama.cpp for local LLM inference
echo "[OSONE] Installing llama.cpp..."
git clone https://github.com/ggerganov/llama.cpp /opt/osone/llama.cpp
cd /opt/osone/llama.cpp
make -j$(nproc)

# Python dependencies for skyd
pip install --break-system-packages \
  psutil \
  requests \
  aiohttp

# Create OSONE directories
mkdir -p /opt/osone/models
mkdir -p /var/log/osone/failforward
mkdir -p /etc/osone

echo "[OSONE] Base setup complete."
echo "[OSONE] Next: download a Mistral 7B Q4 GGUF model to /opt/osone/models/"
echo "[OSONE] Then run: python3 skyd/core/skyd.py"
