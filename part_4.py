
travel_log = []

while True:
    try:
        angle = int(input("What is the Sensor Reading (Slope Angle):"))
        if angle > 45:
            print("CRITICAL TILT! HALTING.")
            break
        else:
            travel_log.append(angle)
            "Path Stable. Moving forward."
    except:
        print("Sensor Glitch")

print("Mission Terminated.")
print(f"Total steps taken: {len(travel_log)}")
print(travel_log)