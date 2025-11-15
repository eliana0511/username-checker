# 🔐 Unique Username Checker
# Author: A.B.
# Description: Simple program that uses a hash table (dictionary)
# to check, add, and suggest unique usernames.

import random

def show_menu():
    print("\n💻 UNIQUE USERNAME CHECKER")
    print("1. Register new username")
    print("2. View all usernames")
    print("3. Exit")

def suggest_username(username, usernames):
    # Suggests alternative usernames if taken
    suggestions = []
    while len(suggestions) < 3:
        new_name = username + str(random.randint(1, 999))
        if new_name not in usernames:
            suggestions.append(new_name)
    return suggestions

def register_username(usernames):
    username = input("Enter a username: ").lower().strip()

    if username in usernames:
        print(f"❌ Sorry, '{username}' is already taken.")
        print("Here are some suggestions:")
        for suggestion in suggest_username(username, usernames):
            print(f"   🔸 {suggestion}")
    else:
        usernames[username] = True  # store in hash table
        print(f"✅ '{username}' registered successfully!")

def view_usernames(usernames):
    if not usernames:
        print("No usernames registered yet.")
        return

    print("\n🧾 Registered Usernames:")
    for i, user in enumerate(sorted(usernames.keys()), 1):
        print(f"{i}. {user}")

def main():
    usernames = {}  # our hash table (dictionary)
    print("✨ Welcome to the Unique Username Checker ✨")

    while True:
        show_menu()
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            register_username(usernames)
        elif choice == "2":
            view_usernames(usernames)
        elif choice == "3":
            print("\n👋 Goodbye! Your usernames are safe and unique 💖")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
