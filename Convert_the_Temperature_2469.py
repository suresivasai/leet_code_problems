def convertTemperature(celsius):
    return [celsius + 273.15, celsius * 1.8 + 32]

a = float(input())
k, f = convertTemperature(a)
print(f"[{k:.5f},{f:.5f}]")