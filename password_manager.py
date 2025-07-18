import string
import random

# View all saved passwords
def view():
    try:
        with open("pwd_manager.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user_service, user_name, user_pwd = data.split(" : ")
                print(f"\nService: {user_service}\nUsername: {user_name}\nPassword: {user_pwd}\n")
    except FileNotFoundError:
        print("\nNo password file found. Add a password first.")

# Create a secure password with required character types
def create(length):
    min_length = 8
    if length < min_length:
        raise ValueError("Password length must be at least 8 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbols = "!@#$&"

    # Ensure password contains at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digit),
        random.choice(symbols),
    ]

    # Fill the rest of the password
    all_chars = lower + upper + digit + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)

    return "".join(password)

# Add a new password entry
def add(generated_pwd=None):
    user_service = input("Service: ").strip()
    user_name = input("Username: ").strip()
    user_pwd = generated_pwd if generated_pwd else input("Password: ").strip()

    with open("pwd_manager.txt", "a") as f:
        f.write(f"{user_service} : {user_name} : {user_pwd}\n")

    print("Password saved successfully.")

# Delete a password entry by service name
def delete():
    service_to_delete = input("Enter the service name to delete: ").strip()
    found = False

    try:
        with open("pwd_manager.txt", "r") as f:
            lines = f.readlines()

        with open("pwd_manager.txt", "w") as f:
            for line in lines:
                if not line.startswith(service_to_delete + " :"):
                    f.write(line)
                else:
                    found = True

        if found:
            print(f"Entry for '{service_to_delete}' deleted.")
        else:
            print(f"No entry found for '{service_to_delete}'.")
    except FileNotFoundError:
        print("No password file found.")

# Main program loop
def main():

    while True:

        mode = input("Choose an option (view/add/create/delete), or press 'q' to quit: ").lower()

        if mode == "q":
            break
        elif mode == "add":
            add()
        elif mode == "view":
            view()
        elif mode == "create":

            try:
                length = int(input("Enter desired password length (minimum 8 characters): "))
                pwd = create(length)
                print(f"Generated password: {pwd}")
                ask = input("Do you want to add this password to the manager? (y/n): ").lower()
                if ask == "y":
                    add(generated_pwd=pwd)
            except ValueError as VE:
                print(VE)

        elif mode == "delete":
            delete()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
