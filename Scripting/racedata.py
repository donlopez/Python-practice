def get_race_data():
    """
    Function to get the race data from the user.
    """
    fuel_level = int(input("Enter your current fuel level percentage: "))
    people_passed = int(input("Enter the number of people you have passed: "))
    laps_in_same_place = int(input("Enter the number of laps you have maintained the same position: "))
    return fuel_level, people_passed, laps_in_same_place

def should_pitstop(fuel_level, people_passed, laps_in_same_place):
    """
    Function to decide if the racer should pull in for a pitstop.
    """
    conditions = {
        "low_fuel_and_people_passed": fuel_level < 50 and people_passed >= 2,
        "low_fuel_and_laps_in_same_place": fuel_level < 50 and laps_in_same_place >= 5
    }

    if conditions["low_fuel_and_people_passed"] or conditions["low_fuel_and_laps_in_same_place"]:
        return "Pull in for a pitstop."
    else:
        return "Keep racing!"

def race_advice():
    """
    Function to get race data, determine if a pitstop is needed, and provide a response.
    """
    print("Welcome to the Racing Strategy Advisor!")
    print("Let's determine if you need a pitstop.")
    fuel_level, people_passed, laps_in_same_place = get_race_data()
    
    decision = should_pitstop(fuel_level, people_passed, laps_in_same_place)
    print("\nDecision: " + decision)
    
    if decision == "Pull in for a pitstop.":
        print("Looks like your car needs a break! Time to refuel and re-energize.")
    else:
        print("You're doing great! Keep pushing those limits on the track!")

# Start the race advice
race_advice()
