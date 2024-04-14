from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Exit")
    print("4.Add quote")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-3): ")

        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2"
            count = int(input("Enter t
