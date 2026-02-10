sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(f"first item = {sample_bay[0]}")
i = int(len(sample_bay)) - 1
print(f"last item = {sample_bay[i]}")
j = len(sample_bay)
print(f"total number of samples in bay = {j}")

for sample_name in range(len(sample_bay)):
    print(f"Transmitting data for: {sample_bay[sample_name]}")