
try:
    motor_speed = int(input("Enter Motor Speed: "))
    print(f"Speed set to {motor_speed}")
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")


