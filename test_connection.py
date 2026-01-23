from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import time
import numpy as np

print("🤖 Connecting to Reachy (Simulation or Real)...")

try:
    with ReachyMini() as mini:
        print("✅ Connected!")
        
        print("📸 Checking Camera...")
        try:
            frame = mini.media.get_frame()
            if frame is not None:
                print(f"   Camera OK! Frame shape: {frame.shape}")
            else:
                print("   ⚠️ Camera returned None. (Simulation might not support camera stream without extra config)")
        except Exception as e:
            print(f"   ⚠️ Camera Error: {e}")

        print("💃 Performing Motion Test...")
        # Look around (Simulation check)
        mini.goto_target(
            head=create_head_pose(roll=20, degrees=True, mm=True),
            duration=1.0
        )
        time.sleep(1.0)
        mini.goto_target(
            head=create_head_pose(roll=-20, degrees=True, mm=True),
            duration=1.0
        )
        time.sleep(1.0)
        mini.goto_target(head=create_head_pose(), duration=1.0)
        
        print("✅ Test Complete!")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    print("   Make sure the simulation is running! (./run_sim.sh)")
