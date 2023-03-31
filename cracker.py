import subprocess
from tqdm import tqdm
from termcolor import colored
import os

# Set the path to the 7z command line executable
seven_zip_executable = "7z"

var = ""

# # Set the path to the password dictionary file
# password_dict_file = "E:/Hidden-Pirates/My Files/Password Dictionary/my-used-psk-list.txt"

# # Set the path to the password-protected ZIP file
# zip_file = "C:/Users/nura5/Desktop/aa.zip"


# Prompt the user to enter the path to the password-protected ZIP file
zip_file_input = input("Enter the path to the password-protected archive file: ")
zip_file = os.path.normpath(zip_file_input.strip("\"'"))

# Prompt the user to enter the path to the password dictionary file
password_dict_file_input = input("Enter the path to the password dictionary file: ")
password_dict_file = os.path.normpath(password_dict_file_input.strip("\"'"))

# Get the total number of passwords in the dictionary
with open(password_dict_file, "r") as f:
    num_passwords = sum(1 for _ in f)

# Loop through each line in the password dictionary file and extract the ZIP file
with open(password_dict_file, "r") as f:
    for password in tqdm(f, total=num_passwords):
        # Try to extract the ZIP file using the current password
        try:
            cmd = [seven_zip_executable, "x", "-aoa", "-p{}".format(password.strip()), zip_file]
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
            # print("\nPassword found: {}".format(password.strip()))
            var = password.strip()
            break
        except subprocess.CalledProcessError:
            # If the password was incorrect, continue to the next password in the dictionary
            continue

if(var != ""):
    print(colored("\n[+] Password found: {}".format(var), 'green'))

else:
    print(colored("\n[+] Password does not found.", 'red'))
