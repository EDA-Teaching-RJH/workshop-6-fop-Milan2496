sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
new_findings = []


print(f"first item = {sample_bay[0]}")
i = int(len(sample_bay)) - 1
print(f"last item = {sample_bay[i]}")
j = len(sample_bay)
print(f"total number of samples in bay = {j}")

for sample_name in range(len(sample_bay)):
    print(f"Transmitting data for: {sample_bay[sample_name]}")

count = 3
while count > 0 :
    rock_name = input("Enter the name of a rock: ")
    count = count - 1 
    new_findings.append(rock_name)

print("New Findings:")

for i in range(len(new_findings)):   
    print(f"{new_findings[i]}")
