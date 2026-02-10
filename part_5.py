
status = {
    "Power": 100,
    "Samples": 0

}

inventory = []

while  True:
    print("-------MENU-------")
    print("1.Dig for sample")
    print("2.Report Status")
    print("3.Emergency Stop")

    option = int(input("Enter an option"))

    if option == 1:
        name = input("Enter a sample name")
        inventory.append(name)
        status("power") == status("power") - 10
    elif option == 2:
        print(inventory)
        print(status)
    elif option == 3:
        break
    else:
        print("Invalid option")

