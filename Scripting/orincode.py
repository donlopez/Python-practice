fuel_level = 45
people_passed = 3
laps_in_same_place = 5

if (fuel_level < 50 and people_passed >= 2) or (fuel_level < 50 and laps_in_same_place >= 5):
    print("Pull in for a pitstop.")
else:
    print("Keep racing!")
