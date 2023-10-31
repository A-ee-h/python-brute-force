from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep   

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Webdrive:
    """
    A class used to represent a Selenium webdriver for Instagram login

    ...

    Attributes
    ----------
    driver : webdriver
        a Selenium webdriver object for Chrome
    submit : WebElement
        a WebElement object for the login submit button

    Methods
    -------
    loadtime()
        Returns the time it takes for the login page to load
    check_in()
        Checks if the user has successfully logged in
    login(payload)
        Logs in the user with the given username and password
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Webdrive object.
        Initializes the Chrome webdriver and navigates to the Instagram login page.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)

    @property
    def loadtime(self):
        """
        Returns the time it takes for the login page to load
        """
        if not self.submit.is_enabled():
            self.loadtime(self.submit)
        return 
    
    def checkin(self):
        """
        Checks if the user has successfully logged in
        """
        self.driver.implicitly_wait(0)
        if self.driver.current_url != "https://www.instagram.com/accounts/login/":
            return True
        if self.driver.find_element(By.CLASS_NAME, "_ab2z"):
            return False
        else:
            print("Exception: got into trouble")
            return True
        
    def login(self, payload):
        """
        Logs in the user with the given username and password

        Parameters
        ----------
        payload : list
            a list containing the username and password of the user

        Returns
        -------
        bool
            True if the user has successfully logged in, False otherwise
        """
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(Keys.CONTROL + "a")
        username.send_keys(payload[0])
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(Keys.CONTROL + "a")
        password.send_keys(payload[1])

        self.submit = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        self.submit.click()

        sleep(3)

        check = self.checkin()
        return check

class word_engine:
    """
    word_engine is a class that generates the next word in a sequence based on a given alphabet.

    Attributes:
    alnum (str): The alphabet used to generate the next word. Defaults to "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789".

    Methods:
    next_word(word, index=None, alnum=None): Generates the next word in the sequence based on the given word and alphabet.
    """
    def __init__(self, alnum=None):
        self.alnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789" if alnum==None else alnum

    next_letter = lambda self, letter, alp : "a" if letter=="9" else alp[alp.index(letter)+1] 


    def next_word(self, word, *, index = None, alnum=None):
        """
        Generates the next word in the sequence based on the given word and alphabet.

        Args:
        word (str): The current word in the sequence.
        index (int, optional): The index of the letter to be changed. Defaults to None.
        alnum (str, optional): The alphabet used to generate the next word. Defaults to None.

        Returns:
        str: The next word in the sequence.
        """
        alnum = self.alnum if alnum is None else alnum
        index = len(word)-1 if index is None else index
        ch = self.next_letter(word[index], alnum)

        if ch == "a":
            if index != 0:
                word = self.next_word(word, index=index-1, alnum=alnum)
            else: 
                word = "a"*(len(word)+1)        
              
        word = word[:index]+ch+word[index+1:]

        return word