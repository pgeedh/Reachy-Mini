#!/bin/bash
echo "🚀 Initializing Reachy Empath Super-Launch..."

# 1. Kill everything
echo "🧹 Cleaning up old processes..."
ps aux | grep -E "empath.main|reachy_mini.daemon" | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null

# 2. Start MuJoCo Simulation (Root of Reachy-Mini)
echo "🌍 Starting MuJoCo Simulation..."
chmod +x run_sim.sh
nohup ./run_sim.sh > sim.log 2>&1 &
sleep 5

# 3. Start Empath Backend
echo "🧠 Starting Empath Backend..."
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 -m empath.main
