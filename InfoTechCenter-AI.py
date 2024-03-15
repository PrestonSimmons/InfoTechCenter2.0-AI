import time, sys

class SuperAdvancedLoadingSystem:
    def __init__(self):
        self.timeToSleep = 0.1

    def welcome(self):
        welcome_message = "\n\nWelcome to InfoTech Center V1.0\n"
        for char in welcome_message:
            print(char, end='', flush=True)
            time.sleep(self.timeToSleep)
        time.sleep(self.timeToSleep)

    def loading(self):
        loading_message = "InfoTech Center Operating System Loading"
        for x in range(20):
            message = loading_message + "." * (x % 4)
            print("\r" + message, end='', flush=True)
            time.sleep(0.05)
            sys.stdout.flush()
            time.sleep(0.2)

        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    loading_system = SuperAdvancedLoadingSystem()
    loading_system.welcome()
    loading_system.loading()
