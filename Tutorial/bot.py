"""
A simple selenium test example written by python
"""
from collections import defaultdict
from this import d
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
import re
import collections
import sys

class Bot:
    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--lang=en")
        chrome_path = "D:\Study\DATA419\Tutorial\chromedriver.exe"
        self.times_restarted = 0  # keep track of how many times profile page has to be refreshed
        self.driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
        self.driver.implicitly_wait(20)

    def tear_down(self):
        """Stop web driver"""
        self.driver.quit()

    def go_to_page(self, url):
        """Find and click top-right button"""
        try:
            self.driver.get(url)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def login(self, username, password):
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
        notNow = self.driver.find_element_by_class_name("HoLwm")
        time.sleep(3)
        notNow.click()
        time.sleep(5)

    def get_my_followers(self, username):
        self.go_to_page("https://instagram.com/" + username + "/")
        time.sleep(5)
        my_followers_set = set()
        #followers = self.driver.find_elements_by_class_name("-nal3")
        followers = self.driver.find_elements_by_class_name("Y8-fY")
        followers[1].click()
        time.sleep(2)
        initialise_vars = 'elem = document.getElementsByClassName("isgrP")[0]; followers = parseInt(document.getElementsByClassName("g47SY")[1].innerText); times = parseInt(followers * 0.14); followersInView1 = document.getElementsByClassName("FPmhX").length'
        initial_scroll = 'elem.scrollTop += 500'
        next_scroll = 'elem.scrollTop += 1500'

        with open('./jquery-3.3.1.min.js', 'r') as jquery_js:
            # 3) Read the jquery from a file
            jquery = jquery_js.read()
            # 4) Load jquery lib
            self.driver.execute_script(jquery)
            # scroll down the page
            self.driver.execute_script(initialise_vars)
            #self.driver.execute_script(scroll_followers)
            self.driver.execute_script(initial_scroll)
            time.sleep(3)
            print("The first scroll.")
            next = True
            while(next):
                #n_li_1 = len(self.driver.find_elements_by_class_name("FPmhX"))
                n_li_1 = len(self.driver.find_elements_by_class_name("wo9IH"))
                print("n_li_1: "+ str(n_li_1))
                self.driver.execute_script(next_scroll)
                print("The next scroll.")
                time.sleep(1.5)
                #n_li_2 = len(self.driver.find_elements_by_class_name("FPmhX"))
                n_li_2 = len(self.driver.find_elements_by_class_name("wo9IH"))
                print("n_li_2: "+ str(n_li_2))
                if(n_li_1 != n_li_2):
                    #following = self.driver.find_elements_by_xpath("//*[contains(text(), 'Following')]")
                    following = self.driver.find_elements_by_class_name("d7ByH")
                    print("The length of following: " + str(len(following)))
                    for follow in following:
                        el = follow.find_element_by_xpath('../..')
                        el = el.find_element_by_tag_name('a')
                        profile = el.get_attribute('href')
                        #profile = follow.get_attribute('href')
                        print(profile)
                        my_followers_set.add(profile)
                else:
                    next = False

            return list(my_followers_set)

    def get_followers(self, my_followers_arr, start_profile, relations_file):
        n_my_followers = len(my_followers_arr)
        count_my_followers = start_profile - 1

        for current_profile in my_followers_arr[start_profile - 1 : -1] + [my_followers_arr[-1]]:
            print("Start scraping " + current_profile)
            self.go_to_page(current_profile)
            #time.sleep(random.randint(5, 20))
            time.sleep(20)
            last_5_following = collections.deque([1, 2, 3, 4, 5])  # queue to keep track of Instagram blocking scroll requests
            #print("initial last_5_following: " + str(set(last_5_following)))
            count_my_followers += 1

            with open('start_profile.txt', 'w+') as outfile: # keep track of last profile checked
                outfile.write(str(count_my_followers))

            followers = self.driver.find_elements_by_class_name("Y8-fY")
            followers[2].click()
            time.sleep(2)
            initialise_vars = 'elem = document.getElementsByClassName("isgrP")[0]; followers = parseInt(document.getElementsByClassName("g47SY")[1].innerText); times = parseInt(followers * 0.14); followersInView1 = document.getElementsByClassName("FPmhX").length'
            initial_scroll = 'elem.scrollTop += 500'
            next_scroll = 'elem.scrollTop += 2000'

            with open('./jquery-3.3.1.min.js', 'r') as jquery_js:
                # 3) Read the jquery from a file
                jquery = jquery_js.read()
                # 4) Load jquery lib
                self.driver.execute_script(jquery)
                # scroll down the page
                self.driver.execute_script(initialise_vars)
                # self.driver.execute_script(scroll_followers)
                self.driver.execute_script(initial_scroll)
                time.sleep(random.randint(2, 5))

                next = True
                follow_set = set()
                # check how many people this person follows
                nr_following = int(re.sub(",","",self.driver.find_elements_by_class_name("g47SY")[2].text))

                n_li = 1
                print(str(count_my_followers) + "/" + str(n_my_followers) + " " + str(n_li) + "/" + str(nr_following))    
                while next:
                    #time.sleep(random.randint(7, 12) / 10.0)
                    time.sleep(3)
                    self.driver.execute_script(next_scroll)
                    #time.sleep(random.randint(7, 12) / 10.0)
                    time.sleep(3)     
                    if nr_following < 100:
                        if not (n_li < nr_following - 15):
                            next = False           
                    if nr_following > 100 and nr_following <= 200:
                        if not (n_li < nr_following - 20):
                            next = False
                    if nr_following > 200 and nr_following <= 300:
                        if not (n_li < nr_following - 30):
                            next = False                
                    if nr_following > 300 and nr_following <= 400:
                        if not (n_li < nr_following - 40):
                            next = False  
                    if nr_following > 400 and nr_following <= 500:
                        if not (n_li < nr_following - 50):
                            next = False  
                    if nr_following > 500 and nr_following <= 600:
                        if not (n_li < nr_following - 60):
                            next = False                                 
                    if nr_following > 600 and nr_following <= 700:
                        if not (n_li < nr_following - 70):
                            next = False 
                    if nr_following > 700 and nr_following <= 800:
                        if not (n_li < nr_following - 80):
                            next = False 
                    if nr_following > 800 and nr_following <= 900:
                        if not (n_li < nr_following - 90):
                            next = False 
                    if nr_following > 900 and nr_following <= 1000:
                        if not (n_li < nr_following - 100):
                            next = False 
                    if nr_following > 1000 and nr_following <= 1100:
                        if not (n_li < nr_following - 110):
                            next = False 
                    if nr_following > 1100 and nr_following <= 1200:
                        if not (n_li < nr_following - 120):
                            next = False 
                    if nr_following > 1200 and nr_following <= 1300:
                        if not (n_li < nr_following - 130):
                            next = False 
                    if nr_following > 1300 and nr_following <= 1400:
                        if not (n_li < nr_following - 140):
                            next = False 
                    if nr_following > 1400:
                        if not (n_li < nr_following - 150):
                            next = False 

                    #n_li = len(self.driver.find_elements_by_class_name("FPmhX"))
                    n_li = len(self.driver.find_elements_by_class_name("wo9IH"))
                    last_5_following.appendleft(n_li)
                    last_5_following.pop()
                    print("current last_5_following: " + str(last_5_following))
                    print(str(count_my_followers) + "/" + str(n_my_followers) + " " + str(n_li) + "/" + str(nr_following))
                    # if instagram starts blocking requests, reload page and start again
                    if len(set(last_5_following)) == 1:
                        print("Instagram seems to keep on loading. Refreshing page in 7 seconds")
                        self.times_restarted += 1
                        if self.times_restarted == 4:
                            print("Instagram keeps on blocking your request. Terminating program. Start it again later.")
                            sys.exit()
                        time.sleep(7)
                        self.get_followers(my_followers_arr, count_my_followers, relations_file)

                self.times_restarted = 0

                #following = self.driver.find_elements_by_class_name("FPmhX")
                following = self.driver.find_elements_by_class_name("d7ByH")
                print("The number of following is: " + str(len(following)))
                for follow in following:
                    el = follow.find_element_by_xpath('../..')
                    el = el.find_element_by_tag_name('a')
                    profile = el.get_attribute('href')
                    if profile in my_followers_arr:
                        print(profile)
                        follow_set.add((current_profile, profile))

                with open(relations_file, "a") as outfile:
                    for relation in follow_set:
                        outfile.write(relation[0].replace("https://www.instagram.com/","").replace("/","") + " " + 
                                        relation[1].replace("https://www.instagram.com/","").replace("/","") + "\n")

                print("This person follows " + str(len(follow_set)) + " of your connections. \n")

        sys.exit()

