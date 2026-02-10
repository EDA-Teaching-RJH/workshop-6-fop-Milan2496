def speed():
    try:
        motor_speed = int(input("Enter Motor Speed: "))
        print(f"Speed set to {motor_speed}")
    except ValueError:
        print("Error: Corrupted Signal. Maintaining current speed.")

def get_coordinate():
    while True:
        try:
            X = int(input("Enter the x coordinate: "))
            if X > 100 or X < -100:
                print("Coordinate out of range")
            else:
                return X
        except:
            print("Invalid coordinate")

        


def main():
    speed()
    X = get_coordinate()

main()

