#!/bin/sh

# Move to script location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Copy systemd files
sudo cp etc/systemd/system/* /etc/systemd/system/

# Reload systemd daemon
sudo systemctl daemon-reload

# Enable services / timers
sudo systemctl enable --now web_host.service
sudo systemctl enable --now web_host_update.timer

# Copy git hooks
cp git/hooks/* ../.git/hooks/
