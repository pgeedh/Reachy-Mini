#!/bin/bash
echo "🤖 Starting Reachy MuJoCo Simulation..."

# Check if we are on Mac
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 Detected macOS. Using mjpython..."
    # Ensure we are in the venv
    source venv/bin/activate
    
    # Launch with mjpython for GUI support
    ./venv/bin/mjpython -m reachy_mini.daemon.app.main --sim --scene minimal
else
    echo "🐧 Detected Linux/Other. Using fast launch..."
    source venv/bin/activate
    reachy-mini-daemon --sim --scene minimal
fi

echo "⚠️  If the simulation failed, makes sure you ran ./run_empath.sh first to install dependencies!"
