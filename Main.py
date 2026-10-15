
import time
import random

def intro():
    print("\n==================================================")
    print("        WELCOME TO THE LEXOMASTICON LAIR        ")
    print("==================================================")
    print("You are Professor Gittles, elite Git administrator.")
    print("You stand in a dimly lit server farm. Before you")
    print("are two massive mainframes blinking with green lights.")
    time.sleep(1)
    choose_path()

def choose_path():
    print("\nWhat is your move?")
    print("1. Inspect the 'Gobbledygook' mainframe on the left.")
    print("2. Audit the 'Fidelity' server core on the right.")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        gobbledygook_path()
    elif choice == "2":
        fidelity_path()
    else:
        print("\n❌ Invalid keystroke! Your typing digit slipped past the bounds.")
        choose_path()

def gobbledygook_path():
    print("\nYou approach the left mainframe. The screen is filled")
    print("with raw markdown code and chaotic character configurations.")
    print("Suddenly, a rogue extension bug appears on line 7!")
    time.sleep(1)
    
    print("\nOptions:")
    print("1. Deploy a rapid Pencil-Icon correction maneuver.")
    print("2. Hit the 'Cancel Changes' emergency shutdown switch.")
    
    action = input("Enter 1 or 2: ").strip()
    
    if action == "1":
        print("\n🎉 SUCCESS! You flawlessly patched the file extension on the fly.")
        print("The system synchronizes perfectly. You win the Git Tenure-Track Award!")
    else:
        print("\n💨 You hit cancel! The slate is wiped completely clean.")
        print("You safely escape back to the dashboard directory to fight another day.")

def fidelity_path():
    print("\nYou step toward the right server core. The air is crisp")
    print("and smells of premium computing processing power.")
    print("A prompt asks you to verify the matrix accuracy.")
    
    accuracy = random.randint(90, 100)
    print(f"\nScanning pipeline... System Integrity Ratio at {accuracy}%!")
    
    if accuracy >= 95:
        print("\n🏆 OPTIMAL VALUE! Professor Gittles has achieved 100% true alignment.")
        print("The repository dashboard glows in pristine software perfection.")
    else:
        print("\n⚠️ Minor deviation detected! Salary docked 4/5 by administrative error.")
        print("Don't worry, you easily appeal it and restore your status.")

# Start the game loop
if __name__ == "__main__":
    intro()
Use code with caution.
