from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import numpy as np
import time
import threading
import cv2

class RobotController:
    def __init__(self):
        self.mini = None
        self.running = False
        self._is_moving = False

    def connect(self, use_local_camera=False):
        self.use_local_camera = use_local_camera
        if self.use_local_camera:
            print("📸 Using computer camera (webcam)...")
            self.cap = cv2.VideoCapture(0)
            
        try:
            self.mini = ReachyMini()
            self.mini.__enter__() 
            self.running = True
            print("✅ Connected to Reachy Mini")
            self.trigger_gesture("happy")
            return True
        except Exception as e:
            print(f"⚠️ Robot hardware connection skipped/failed: {e}")
            self.mini = None
            if not self.use_local_camera:
                 print("📸 Falling back to computer camera...")
                 self.use_local_camera = True
                 self.cap = cv2.VideoCapture(0)
            return True # Allow running in "brain-only" mode if cam works

    def disconnect(self):
        if hasattr(self, 'cap'):
            self.cap.release()
        if self.mini:
            self.mini.__exit__(None, None, None)
            self.mini = None
            self.running = False

    def get_frame(self):
        if self.use_local_camera:
            ret, frame = self.cap.read()
            if ret:
                return frame
            return None
            
        if self.mini and self.running:
            try:
                f = self.mini.media.get_frame()
                if f is not None: return f
            except:
                pass
        
        # Last resort fallback if we haven't opened cap yet
        if not hasattr(self, 'cap'):
            self.cap = cv2.VideoCapture(0)
            self.use_local_camera = True
        
        return None

    # --- Gestures (Threaded to not block main API) ---
    def trigger_gesture(self, gesture_name):
        if self._is_moving: return
        method = getattr(self, f"_{gesture_name}", None)
        if method:
            threading.Thread(target=method, daemon=True).start()
        else:
            print(f"⚠️ Gesture {gesture_name} not found")

    def _happy(self):
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                antennas=np.deg2rad([45, -45]), # Wiggle
                head=create_head_pose(z=10, pitch=-10, degrees=True, mm=True),
                duration=0.5
            )
            time.sleep(0.5)
            self.mini.goto_target(
                antennas=np.deg2rad([0, 0]),
                head=create_head_pose(pitch=0, degrees=True, mm=True),
                duration=0.5
            )
            time.sleep(0.5)
        finally:
            self._is_moving = False

    def _sad(self):
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                antennas=np.deg2rad([130, -130]), # Droopy
                head=create_head_pose(z=-10, pitch=20, degrees=True, mm=True), # Look down
                duration=1.0
            )
            time.sleep(1.0)
            self.mini.goto_target(
                head=create_head_pose(pitch=0, degrees=True, mm=True),
                duration=0.5
            )
            time.sleep(0.5)
        finally:
            self._is_moving = False

    def _curious(self):
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                head=create_head_pose(roll=20, degrees=True, mm=True), # Tilt
                duration=0.5
            )
            time.sleep(0.5)
            # Stay tilted a bit longer or return?
            self.mini.goto_target(
                head=create_head_pose(roll=0, degrees=True, mm=True),
                duration=0.5
            )
            time.sleep(0.5)
        finally:
            self._is_moving = False

    def _thinking(self):
        """Looks up and circles antennas slightly."""
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                head=create_head_pose(pitch=-20, roll=10, degrees=True, mm=True),
                antennas=np.deg2rad([20, 20]),
                duration=0.8
            )
            time.sleep(0.8)
            self.mini.goto_target(
                head=create_head_pose(pitch=0, roll=0, degrees=True, mm=True),
                antennas=np.deg2rad([0, 0]),
                duration=0.5
            )
            time.sleep(0.5)
        finally:
            self._is_moving = False

    def _surprised(self):
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                antennas=np.deg2rad([90, -90]), # Straight out
                head=create_head_pose(z=20, pitch=-30, degrees=True, mm=True), # Lean back & up
                duration=0.3
            )
            time.sleep(0.6)
            self.mini.goto_target(
                head=create_head_pose(pitch=0, degrees=True, mm=True),
                duration=0.5
            )
        finally:
            self._is_moving = False

    def _angry(self):
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                antennas=np.deg2rad([-45, 45]), # Flattened forward
                head=create_head_pose(pitch=15, roll=5, degrees=True, mm=True), # Lean forward
                duration=0.4
            )
            time.sleep(0.8)
            self.mini.goto_target(
                antennas=np.deg2rad([0, 0]),
                head=create_head_pose(pitch=0, degrees=True, mm=True),
                duration=0.5
            )
        finally:
            self._is_moving = False

    def _confused(self):
        if not self.mini: return
        self._is_moving = True
        try:
            # Asymmetric antennas
            self.mini.goto_target(
                antennas=np.deg2rad([40, 10]), 
                head=create_head_pose(roll=25, pitch=-5, degrees=True, mm=True),
                duration=0.6
            )
            time.sleep(1.0)
            self.mini.goto_target(
                antennas=np.deg2rad([10, 40]),
                duration=0.6
            )
            time.sleep(0.6)
            self.mini.goto_target(
                antennas=np.deg2rad([0, 0]),
                head=create_head_pose(roll=0, pitch=0, degrees=True, mm=True),
                duration=0.5
            )
        finally:
            self._is_moving = False

    def _excited(self):
        if not self.mini: return
        self._is_moving = True
        try:
            # Rapid antenna wiggle and head bob
            for _ in range(2):
                self.mini.goto_target(
                    antennas=np.deg2rad([60, -60]),
                    head=create_head_pose(z=15, degrees=True, mm=True),
                    duration=0.2
                )
                time.sleep(0.2)
                self.mini.goto_target(
                    antennas=np.deg2rad([-60, 60]),
                    head=create_head_pose(z=5, degrees=True, mm=True),
                    duration=0.2
                )
                time.sleep(0.2)
            self.mini.goto_target(antennas=np.deg2rad([0, 0]), head=create_head_pose(), duration=0.4)
        finally:
            self._is_moving = False

    def _bashful(self):
        if not self.mini: return
        self._is_moving = True
        try:
            self.mini.goto_target(
                antennas=np.deg2rad([110, -110]), # Droopy
                head=create_head_pose(pitch=15, roll=-15, degrees=True, mm=True), # Look down and away
                duration=0.8
            )
            time.sleep(1.2)
            self.mini.goto_target(
                head=create_head_pose(pitch=0, roll=0, degrees=True, mm=True),
                duration=0.8
            )
        finally:
            self._is_moving = False
