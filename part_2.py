rover_status = {
"Battery": 100,
"Heater": "Off",
"Camera": "Standby",
}

print(rover_status["Battery"])

(rover_status["Battery"]) = 85
(rover_status["Heater"]) = "On"
(rover_status["Speed"]) = 5

print(rover_status)

mission_log = [
    {   "Dictionary1" : {
            "Site": "Crater A",
            "Radiation": "Low",
            "Water": False,
        }
    },

    {
        "Dictionary2" : {
            "Site": "Dune B",
            "Radiation": "High",
            "Water": True,
        }
    }
]
num = 0
for i in range(len(mission_log)):
    num = num + 1
    if num == 1:
        print(f"Site {mission_log[i]["Dictionary1"]["Site"]} has {mission_log[i]["Dictionary1"]["Radiation"]} radiation.")
    elif num == 2:
        print(f"Site {mission_log[i]["Dictionary2"]["Site"]} has {mission_log[i]["Dictionary2"]["Radiation"]} radiation.")
