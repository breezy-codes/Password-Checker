import time
import os

# Password Checker
# This program checks if a password is in a list of common passwords, both popular lists and leaked password lists.
# The purpose of this is to help users avoid using common passwords that are easily guessable by attackers.

# Load all the password lists into a set for checking against
def load_password_list(file_paths):
    passwords = set()
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            passwords.update(line.strip().lower() for line in file)
    return passwords

# Check if the entered password is in the password list ignoring case sensitivity
def check_password(password, password_set):
    return password.lower() in password_set

def main():
    # Path to the folder containing the password list files
    folder_path = 'Lists'

    # Get the list of password list files
    password_list_files = [os.path.join(folder_path, filename) for filename in
                           ['rockyou_1.txt', 'rockyou_2.txt', 'most_used_passwords.txt',
                            'xato-net-10-million-passwords.txt', 'alleged-gmail-passwords.txt', 'Ashley-Madison.txt']]

    # Load the password lists
    start_time = time.time()
    password_set = load_password_list(password_list_files)
    load_time = time.time() - start_time
    print(f"Loaded password lists in {load_time:.4f} seconds")

    while True:
        # Prompt the user to enter a password
        sample_password = input("Enter a password to check (or type 'exit' to quit): ")
        if sample_password.lower() == 'exit':
            break

        # Check the entered password
        start_time = time.time()
        is_password_in_list = check_password(sample_password, password_set)
        check_time = time.time() - start_time

        # Print the result
        if is_password_in_list:
            print(f"HA! Your password is in the list. You should probably change it....")
        else:
            print(f"The password is NOT in the list. Good job!")

        print(f"Checked password in {check_time:.6f} seconds")

if __name__ == "__main__":
    main()
