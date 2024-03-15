import random
from time import sleep


def gas_level_gauge():
    """Simulate reading the gas level."""
    gas_levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gas_levels)


def list_of_gas_stations():
    """Simulate listing nearby gas stations."""
    gas_stations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobile", "Costco", "Meijers", "7Eleven"]
    return random.choice(gas_stations)


def find_nearest_gas_station(miles):
    """Simulate finding the nearest gas station."""
    gas_station = list_of_gas_stations()
    print(f"The closest gas station is {gas_station}, {miles} miles away.")
    sleep(1.5)  # Add delay for a more realistic simulation


def gas_level_alert():
    """Alert the user based on the gas level."""
    gas_level = gas_level_gauge()
    print(f"Gas Tank Level: {gas_level}")
    sleep(1)  # Add delay for a more realistic simulation

    if gas_level == "Empty":
        print("***WARNING - YOUR TANK IS EMPTY***")
        sleep(2.5)
        print("Calling Triple AAA")
    elif gas_level == "Low":
        print("Gas Tank is low. Searching for the nearest gas station...")
        find_nearest_gas_station(round(random.uniform(1, 25), 1))
    elif gas_level == "Quarter Tank":
        print("Quarter Tank. Searching for the nearest gas station...")
        find_nearest_gas_station(round(random.uniform(25.1, 50), 1))
    elif gas_level == "Half Tank":
        print("Gas Tank is at half.")
    else:
        print("Gas Tank is full.")


def main():
    """Main function to execute the gas level alert system."""
    print("*******************************")
    print("Gasoline Branch\n\n")

    # Alert the user based on the gas level
    gas_level_alert()


if __name__ == "__main__":
    main()



