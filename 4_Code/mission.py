from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to SITL
print("Connecting to drone...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    print("Taking off...")
    vehicle.simple_takeoff(target_altitude)
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {altitude:.1f}m")
        if altitude >= target_altitude * 0.95:
            print("Target altitude reached!")
            break
        time.sleep(1)

# Waypoints
waypoints = [
    LocationGlobalRelative(17.4325, 78.3012, 20),
    LocationGlobalRelative(17.4335, 78.3022, 20),
    LocationGlobalRelative(17.4345, 78.3032, 20),
    LocationGlobalRelative(17.4355, 78.3042, 20),
]

arm_and_takeoff(20)

print("Navigating waypoints...")
for i, wp in enumerate(waypoints):
    print(f"Going to waypoint {i+1}...")
    vehicle.simple_goto(wp)
    time.sleep(10)

print("Returning to launch...")
vehicle.mode = VehicleMode("RTL")
time.sleep(15)

print("Mission complete!")
vehicle.close()
