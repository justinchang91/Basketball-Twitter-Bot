from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
from selenium.webdriver.common.keys import Keys

from secrets import email, password, username


class TwitterBot:
    def __init__(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window()
        self.stats = None

    def login(self):
        # Go to twitter website
        self.driver.get("https://twitter.com/login")
        self.driver.implicitly_wait(5)

        time.sleep(2)
        # enter username and password
        username_search = self.driver.find_element_by_name("session[username_or_email]")
        username_search.send_keys(username)
        time.sleep(2)
        password_search = self.driver.find_element_by_name("session[password]")
        password_search.send_keys(password)
        time.sleep(2)

        # click login button (right click -> copy -> copy full xpath)
        login_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
        login_button.click()
        time.sleep(3)

    def search_stats(self):
        # open a new window and switch to it
        self.driver.execute_script("window.open('');")
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # go to Pascal Siakam nba page
        self.driver.get("https://www.nba.com/player/1627783/pascal-siakam")

        # click on cookies accept button
        cookie_button = self.driver.find_element_by_id("onetrust-accept-btn-handler")
        cookie_button.click()

        # get the data from most recent game
        date = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[1]/a").text
        match_up = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[2]").text
        win_loss = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[3]").text
        minutes = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[4]").text
        points = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[5]").text
        fgm = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[6]/a").text
        fga = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[7]/a").text
        three_p_m = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[9]/a").text
        rebounds = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[17]/a").text
        assists = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[18]/a").text
        ftm = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[12]").text
        fta = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/section[2]/div/div/div/table/tbody/tr[1]/td[13]").text

        # store the data in a dictionary
        self.stats = {
            "date": date,
            "match up": match_up,
            "opponent": match_up[6:len(match_up):],
            "w/l": win_loss,
            "min": minutes,
            "pts": points,
            "fgm": fgm,
            "fga": fga,
            "3pm": three_p_m,
            "reb": rebounds,
            "ast": assists,
            "ftm": ftm,
            "fta": fta
        }

        print("")

    def tweet(self, message):
        # find tweet button
        tweet_button = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        tweet_button.click()
        time.sleep(2)

        # find tweet box
        tweet_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")))
        tweet_box.click()
        tweet_box.send_keys(message)
        time.sleep(1)

        # find the tweet button
        send_tweet = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]")
        send_tweet.click()

    def tweet_stats(self):
        # go back to twitter window
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

        # go to tweet box
        tweet_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        tweet_button.click()

        # check if win or loss
        if self.stats["w/l"] == "W":
            result = "win"
        else:
            result = "loss"

        time.sleep(2)
        # click on the tweet thing (this took forever to figure out, it kept cutting off letters without the wait)
        tweet_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")))
        tweet_box.click()
        tweet_box.send_keys("Pascal Siakam tonight in " + result + " vs. " + str(self.stats["opponent"]) + ": "
                            + str(self.stats["min"]) + " mins, " + str(self.stats["pts"]) + " pts ("
                            + str(self.stats["fgm"]) + "-" + str(self.stats["fga"]) + " FG; " + str(self.stats["3pm"])
                            + " 3PM), " + str(self.stats["reb"]) + " reb, " + str(self.stats["ast"]) + " ast, "
                            + str(self.stats["ftm"]) + "-" + str(self.stats["fta"]) + " FT.")

        time.sleep(1)
        # click tweet button
        send_tweet = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]")
        send_tweet.click()

    def like(self):
        # be on twitter window
        self.driver.switch_to.window(self.driver.window_handles[0])

        time.sleep(2)
        while True:
            # locate all like buttons on screen, store coordinates in list
            like_button_locations = list(pyautogui.locateAllOnScreen("twitter like button.png", confidence=0.81))

            if len(like_button_locations) > 0:
                for location in like_button_locations:
                    print(location)
                    # get the x and y coordinates of the like button
                    x_coordinate = location[0]
                    y_coordinate = location[1]

                    # move the mouse and click
                    pyautogui.moveTo(x_coordinate, y_coordinate)
                    time.sleep(1)
                    pyautogui.click()
                    pyautogui.moveTo(100, 300)
                    time.sleep(2)

            else:
                print("Can't find any like buttons")

            # scroll down to bottom of screen
            pyautogui.scroll(-1050)
            time.sleep(2)

    def search_twitter(self, search_string):
        # be on twitter window
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

        # find the search bar
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             "/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")))
        search_bar.click()

        # send in the string to search and click enter
        search_bar.send_keys(search_string)
        time.sleep(1)
        search_bar.send_keys(Keys.RETURN)


bot = TwitterBot()
bot.login()
bot.search_twitter("Raptors")

