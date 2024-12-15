from luh_pakuri import Pakuri
from pakudex import Pakudex

# Display menu board
def display_menu():
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")

# Define the welcome message
def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    # Prompt the user to enter the max capacity of the Pakudex
    capacity = input("Enter the max capacity of the Pakudex: ")

    # Validate the input
    while not capacity.isdigit() or int(capacity) <= 0:
        print("Please enter a valid size.")
        capacity = input("Enter the max capacity of the Pakudex: ")
    
    capacity = int(capacity)
    
    # Create a new Pakudex with the specified capacity
    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    # Main menu loop
    while True:
        display_menu()
        choice = input("What would you like to do? ")

        if choice == '1':
            # List all Pakuri species in the Pakudex
            species_array = pakudex.get_species_array()
            if species_array:
                print("Pakuri In Pakudex:")
                for i, species in enumerate(species_array, 1):  # Enumerate the list with numbers
                    print(f"{i}. {species}")
            else:
                print("No Pakuri in Pakudex yet!")

        elif choice == '2':
            # Show stats for a specific Pakuri species
            species = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species)
            if stats:
                print(f"\nSpecies: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")

        elif choice == '3':
            # Add a new Pakuri species to the Pakudex
            if pakudex.get_size() >= pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                species = input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(species):
                    print(f"Pakuri species {species} successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")

        elif choice == '4':
            # Evolve an existing Pakuri species
            species = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(species):
                print(f"{species} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif choice == '5':
            # Sort all Pakuri species in the Pakudex
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == '6':
            # Exit message
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()