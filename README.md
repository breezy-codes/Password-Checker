# Password Checker

<div align="center">  
    <a href="  
    [https://www.linkedin.com/in/brianna-laird/](https://www.linkedin.com/in/brianna-laird/)" target="_blank">  
    <img src="  
    [https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge](https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge)" height="25" alt="linkedin logo" />  
    </a>  
    <a href="  
    [https://www.youtube.com/@Breezy-Codes](https://www.youtube.com/@Breezy-Codes)" target="_blank">  
    <img src="  
    [https://img.shields.io/static/v1?message=YouTube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge](https://img.shields.io/static/v1?message=YouTube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge)" height="25" alt="youtube logo" />  
    </a>  
    <a href="  
    [https://briannalaird.com/](https://briannalaird.com/)" target="_blank">  
    <img src="  
    [https://img.shields.io/static/v1?message=My Portfolio&logo=portfolio&label=&color=8A2BE2&logoColor=white&labelColor=&style=for-the-badge](https://img.shields.io/static/v1?message=My%20Portfolio&logo=portfolio&label=&color=8A2BE2&logoColor=white&labelColor=&style=for-the-badge)" height="25" alt="portfolio logo" />  
    </a>  
</div>  


This project is a simple yet effective tool designed to help users avoid using common passwords that are easily guessable by attackers. By checking against popular and leaked password lists, this program ensures that your password is not among the commonly used ones, enhancing your security.

## Features

- **Efficient Loading**: Quickly loads multiple password lists into a set for fast checking.
- **Case-Insensitive Check**: Checks passwords ignoring case sensitivity.
- **Interactive**: Prompts the user to enter a password and provides instant feedback on whether the password is in 
  a list or not.
- **Performance Tracking**: Measures and displays the time taken to load password lists and check passwords.

## Usage

1. **Prepare Password Lists**: The `Lists` folder contains a series of password lists, you are welcome to add others 
   and update the main code. The program will load these lists into memory for quick checking.
2. The following files have been added:
    - `rockyou_1.txt`
    - `rockyou_2.txt`
    - `most_used_passwords.txt`
    - `xato-net-10-million-passwords.txt`
    - `alleged-gmail-passwords.txt`
    - `Ashley-Madison.txt`

2. **Run the Program**: Execute the script. It will load the password lists and prompt you to enter a password to check.

3. **Check Passwords**: Enter a password to check if it is in the loaded password lists. Or type `exit` to quit the 
   program.
4. **Check More Passwords (option)**: If you would like to check more password lists, simply add them to the `Lists` 
   folder, then modify the python script within the `main` to add the new lists.
```
def main():
    # Path to the folder containing the password list files
    folder_path = 'Lists'

    # Get the list of password list files
    password_list_files = [os.path.join(folder_path, filename) for filename in
                           ['rockyou_1.txt', 'rockyou_2.txt', 'most_used_passwords.txt','xato-net-10-million-passwords.txt', 'alleged-gmail-passwords.txt', 'Ashley-Madison.txt']]
```

## Installation

1. **Clone the Repository**:

    `git clone https://github.com/breezy-codes/password-checker.git`
    
   `cd password-checker`

2. **Run the Program**:

    `python password_checker.py`

## Example

```bash
$ python password_checker.py
Loaded password lists in 3.4567 seconds
Enter a password to check (or type 'exit' to quit): password123
HA! Your password is in the list. You should probably change it....
Checked password in 0.000123 seconds
Enter a password to check (or type 'exit' to quit): mySecureP@ss
The password is NOT in the list. Good job!
Checked password in 0.000098 seconds
Enter a password to check (or type 'exit' to quit): exit
```

---

### Disclaimer

This is not a tool to rely on for proper passwords, just a tool to see if passwords you have used are in some 
publicly found password lists. Please ensure to use strong passwords.

---

