import time  # Import the time module for sleep functionality
import sys   # Import the sys module for standard input/output operations

class SuperAdvancedLoadingSystem:
    def __init__(self):
        self.timeToSleep = 0.1  # Define the sleep duration for the loading animation

    def welcome(self):
        welcome_message = "\n\nWelcome to InfoTech Center V1.0\n"  # Define the welcome message
        for char in welcome_message:
            print(char, end='', flush=True)  # Print each character of the welcome message
            time.sleep(self.timeToSleep)     # Pause briefly after printing each character
        time.sleep(self.timeToSleep)         # Pause after printing the entire message

    def loading(self):
        loading_message = "InfoTech Center Operating System Loading"  # Define the loading message
        for x in range(20):  # Iterate 20 times for the loading animation
            message = loading_message + "." * (x % 4)  # Append dots to the loading message
            print("\r" + message, end='', flush=True)  # Print the loading message with carriage return
            time.sleep(0.05)   # Pause briefly after printing each frame of the animation
            sys.stdout.flush() # Flush the standard output buffer to ensure immediate display
            time.sleep(0.2)    # Pause after each frame to control the animation speed

        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")  # Print the final message

if __name__ == "__main__":
    loading_system = SuperAdvancedLoadingSystem()  # Create an instance of the loading system
    loading_system.welcome()                      # Display the welcome message
    loading_system.loading()                      # Run the loading animation
