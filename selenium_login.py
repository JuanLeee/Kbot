from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from tesseract_ocr import *
from card_image import url_to_image
import tesseract_ocr
import sys
import random
import logging
import json
from discord_webhook import DiscordWebhook
from good_stuffs import dict_good_stuff_static
from good_stuffs import dict_good_stuff_addition
from good_stuffs import char_numbers
import time
import math


import time
from dotenv import load_dotenv

load_dotenv()


class Discord_Scraper:
    def __init__(self, driver, action, user_name, password, server_name, channel_name, server_name_list, id_name, timer):
        self.hash_table = {}
        self.count_messages = 0
        self.driver = driver
        self.action = action
        self.user_name = user_name
        self.password = password
        self.server_name = server_name
        self.server_name_list = server_name_list
        self.channel_name = channel_name
        global flag_debug
        global flag_cd_grab
        global flag_cd_grab_long
        global flag_global_clicked
        global flag_refresh
        global flag_stop
        flag_debug = False
        flag_refresh = False
        flag_global_clicked = False
        self.clicked_card = ''
        self.flag_clicked = False
        self.count_reset = 10
        self.count_clicked = self.count_reset
        self.id_name = id_name
        self.curr_id = ''
        if timer:
            self.sleep_timer_grab = 300
            self.sleep_timer_drop = 900
        else:
            self.sleep_timer_grab = 600
            self.sleep_timer_drop = 1800
        flag_stop = False
        self.ocr = OCR_PyTes()
        self.dict_good_stuff = dict_good_stuff_static
        self.dict_good_stuff_addition = dict_good_stuff_addition

        for key in self.dict_good_stuff.keys():
            temp_value = self.dict_good_stuff[key].split(' ', 1)[0]
            self.dict_good_stuff[key] = temp_value

        for key in self.dict_good_stuff_addition.keys():
            temp_value = self.dict_good_stuff_addition[key].split(' ', 1)[0]
            self.dict_good_stuff_addition[key] = temp_value
        self.time = time.time()
        self.counter = 50

        self.disc_webhook = os.getenv('DISCORD_LINK')

    def login_sign(self):
        error_count = 0
        while error_count < 2:
            try:
                self.driver.get("https://discord.com/login")

                print('Login')
                username_input = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.NAME, 'email')))
                username_input.send_keys(self.user_name)

                password_input = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.NAME, 'password')))
                password_input.send_keys(self.password)

                print('Submit button')
                login_button = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
                self.driver.execute_script(
                    "arguments[0].click();", login_button)

                server_name = "//*[@data-list-item-id=\"" + \
                    self.server_name + "\"]"

                print("Trying if School Pop up")
                try:
                    hcaptcha = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'flexCenter-3_1bcw')))
                    print("HCaptcha")
                    pop_up = WebDriverWait(self.driver, 120).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'content-1LAB8Z')))
                    pop_up_button = WebDriverWait(pop_up, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'close-hZ94c6')))
                    self.driver.execute_script(
                        "arguments[0].click();", pop_up_button)
                    print("School Pop up")
                except:
                    print("No HCaptcha")
                    # logging.error("Exception occurred", exc_info=True)
                    try:
                        pop_up = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.CLASS_NAME, 'content-1LAB8Z')))
                        pop_up_button = WebDriverWait(pop_up, 5).until(
                            EC.presence_of_element_located((By.CLASS_NAME, 'close-hZ94c6')))
                        self.driver.execute_script(
                            "arguments[0].click();", pop_up_button)
                        print("School Pop up")
                    except:
                        print("School No Pop up")
                        # logging.error("Exception occurred", exc_info=True)

                print('Server')
                server_icon = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, server_name)))
                self.driver.execute_script(
                    "arguments[0].click();", server_icon)

                print("Trying to see if pop up")

                try:
                    pop_up = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'focusLock-Ns3yie')))
                    self.driver.execute_script("arguments[0].click();", WebDriverWait(pop_up, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'button-38aScr'))))
                    print("Pop up")
                except:
                    print("No Pop up")
                    # logging.error("Exception occurred", exc_info=True)

                print('Channel Scroll')
                channel_list = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'scroller-RmtA4e')))
                self.action.move_to_element(channel_list.find_elements(
                    By.CLASS_NAME, 'containerDefault--pIXnN')[-1]).perform()
                time.sleep(1)
                self.action.move_to_element(channel_list.find_elements(
                    By.CLASS_NAME, 'containerDefault--pIXnN')[-1]).perform()

                channel_name = "//*[@data-list-item-id=\"" + \
                    self.channel_name + "\"]"

                print('Channel')
                logging.info("Logged into " + self.server_name_list)
                channel_icon = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, channel_name)))

                self.driver.execute_script(
                    "arguments[0].click();", channel_icon)

                webhook = DiscordWebhook(url=self.disc_webhook, rate_limit_retry=True,
                                         content='Logged into ' + self.user_name + ' and into server ' + self.server_name_list)
                response = webhook.execute()

                break
            except:
                logging.warning("Starting up")
                logging.error("Exception occurred", exc_info=True)
                time.sleep(5)

    def message_log(self, f_condition, f_action):
        global flag_debug
        global flag_refresh
        global flag_global_clicked
        global flag_cd_grab
        global flag_cd_grab_long
        global flag_stop
        flag_cd_grab_long = True
        flag_cd_grab = True
        refresh_counter = 0
        logs = WebDriverWait(self.driver, 120, poll_frequency=0.05).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-2qnXI6')))
        i = len(logs)-1
        while i <= 0:
            logs = WebDriverWait(self.driver, 120, poll_frequency=0.05).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-2qnXI6')))
            i = len(logs)-1
        interval = 0.33
        print('Message Scroll')
        self.action.move_to_element(WebDriverWait(self.driver, 120, poll_frequency=0.05).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-2qnXI6')))[-2]).perform()
        for n in range(1, 15):
            WebDriverWait(self.driver, 120, poll_frequency=0.05).until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'message-2qnXI6')))[-1].send_keys(Keys.ARROW_DOWN)
        n = 20
        self.current_state_fill_hash(n)
        count_clear = 0
        while not flag_stop:
            try:

                for j in range(1, n):
                    z = 1 * j
                    if flag_debug:
                        print(z)
                    try:
                        logs = WebDriverWait(self.driver, 120, poll_frequency=0.05).until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-2qnXI6')))
                        data_list_str = logs[z].get_attribute('id')
                        self.curr_id = str(data_list_str)
                    except:
                        logging.info("NO ATTRIBUTES START" +
                                     " " + self.server_name_list)
                        logging.info(data_list_str)
                        logging.info(str(z) + " FAILED ")
                        break

                    if data_list_str not in self.hash_table:
                        text = logs[z].text
                        self.hash_table[data_list_str] = self.count_messages
                        self.count_messages += 1
                        if self.flag_clicked:
                            self.count_clicked -= 1

                            if self.id_name + ', your Evasion' in text:
                                self.count_clicked = self.count_reset
                                self.flag_clicked = False
                                flag_cd_grab_long = True
                                flag_cd_grab = True
                                flag_global_clicked = False
                                webhook = DiscordWebhook(url=self.disc_webhook, rate_limit_retry=True,
                                                         content=self.user_name + ' got ' + self.clicked_card + ' in ' + self.server_name_list)
                                logging.info("Evasion Proc")
                                webhook.execute()

                                break
                            elif self.id_name + ' fought off' in text or self.id_name + ' took the' in text:
                                self.count_clicked = self.count_reset
                                self.flag_clicked = False
                                flag_cd_grab_long = False
                                logging.info("GOTTEM")
                                print("Gottem")
                                webhook = DiscordWebhook(url=self.disc_webhook, rate_limit_retry=True,
                                                         content=self.user_name + ' got ' + self.clicked_card + ' in ' + self.server_name_list)
                                webhook.execute()
                                self.clean_hash_table()
                                time.sleep(self.sleep_timer_grab)
                                self.current_state_fill_hash(n)
                                flag_cd_grab_long = True
                                flag_cd_grab = True
                                flag_global_clicked = False
                                print("Exit: " + self.server_name_list)

                                break
                            elif self.count_clicked <= 0 or self.clicked_card in text.lower():
                                print("Fled")
                                self.count_clicked = self.count_reset
                                self.flag_clicked = False
                                flag_cd_grab = False
                                self.clean_hash_table()
                                time.sleep(60)
                                self.current_state_fill_hash(n)
                                flag_cd_grab = True
                                flag_cd_grab_long = True
                                flag_global_clicked = False
                                print("Exit: " + self.server_name_list)

                                break
                        elif f_condition(text):
                            f_action()

                    else:
                        break
                if not flag_cd_grab:
                    print("Enter: " + self.server_name_list)
                    self.count_clicked = self.count_reset
                    self.flag_clicked = False
                    self.clean_hash_table()
                    time.sleep(59)

                    print("Exit: " + self.server_name_list)
                    self.current_state_fill_hash(n)

                elif not flag_cd_grab_long:
                    print("Enter: " + self.server_name_list)
                    self.count_clicked = self.count_reset
                    self.flag_clicked = False
                    self.clean_hash_table()
                    time.sleep(self.sleep_timer_grab-1)


                    print("Exit: " + self.server_name_list)
                    self.current_state_fill_hash(n)

                time.sleep(interval)
            except:
                logging.warning("Error ml " + self.server_name_list)
                logging.error("Exception occurred", exc_info=True)
            if flag_stop:
                self.driver.quit()
                print("Quit " + self.server_name_list)
                break

    def clean_hash_table(self):
        print("Cleaning Hash Table")
        for key, value in list(self.hash_table.items()):
            if value < (self.count_messages-100):
                del self.hash_table[key]

    def current_state_fill_hash(self, n):
        try:
            print("Filling hash table")
            logs = WebDriverWait(self.driver, 120, poll_frequency=0.05).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'message-2qnXI6')))
            for j in range(1, n):
                z = -1 * j
                try:
                    data_list_str = logs[z].get_attribute('id')
                    if data_list_str not in self.hash_table:
                        self.hash_table[data_list_str] = self.count_messages
                        self.count_messages += 1
                    else:
                        break
                except:
                    logging.info("NO ATTRIBUTES START" +
                                 " " + self.server_name_list)
                    logging.info(str(z) + " FAILED " + self.curr_id)

                    logging.warning(
                        "NO ATTRIBUTES START END", exc_info=True)
                    break
        except:
            logging.warning(
                "Failed Filling", exc_info=True)

    def kd_every(self):
        global flag_refresh
        global flag_global_clicked
        global flag_cd_grab
        global flag_cd_grab_long
        global flag_stop
        flag_cd_grab_long = True
        flag_cd_grab = True
        flag_stop = False
        sleep(90)
        while not flag_stop:
            if not flag_cd_grab or not flag_cd_grab_long or flag_global_clicked:
                sleep(20)
            else:
                try:
                    logging.warning('Drop')
                    textbox = self.driver.find_element_by_class_name(
                        'markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP')
                    textbox.send_keys('kd')
                    textbox.send_keys(Keys.ENTER)
                    sleep(float(random.randrange(
                        self.sleep_timer_drop, self.sleep_timer_drop+300)))
                except:
                    logging.error("Exception occurred", exc_info=True)
        self.driver.quit()
        print("Quit DROP " + self.server_name_list)

    def condition_BOT_droppping(self, text):
        try:
            if "dropping 4 cards" in text or "dropping 3 cards" in text:
                if self.driver.find_element_by_id(self.curr_id).find_element_by_class_name('anchor-3Z-8Bb'):
                    return True
        except:
            return False
        return False

    def condition_BOT_droppping_Server(self, text):
        try:
            if "cards since this server is currently active!" in text:
                if self.driver.find_element_by_id(self.curr_id).find_element_by_class_name('anchor-3Z-8Bb'):
                    return True
        except:
            return False
        return False

    def flag_stop_true(self):
        global flag_stop
        flag_stop = True
        self.driver.quit()
        print("Quit " + self.server_name_list)

    def action_href_img(self):
        global flag_global_clicked
        global flag_cd_grab

        error_count = 0
        flag_finished = False
        while(error_count < 3 and not flag_finished):
            try:
                img_container = self.driver.find_element_by_id(
                    self.curr_id).find_element_by_class_name('anchor-3Z-8Bb')
                href_link = img_container.get_attribute('href')

                error_count_image = 0
                try:
                    image = url_to_image(href_link)
                    while image is None:
                        error_count_image += 1
                        if error_count_image > 3:
                            break
                        logging.info("Cant get image:" +
                                     href_link + " " + str(error_count_image))
                        image = url_to_image(href_link)
                    h, w, c = image.shape
                except:
                    
                    logging.warning("Cant get image:" + href_link)
                    logging.warning("Unexpected error:", sys.exc_info()[0])
                    error_count += 1
                    if error_count_image > 3:
                            break
                    continue
                max = 4 if w > 900 else 3
                pos = max-1
                try:
                    while pos >= 0 and not self.flag_clicked:
                        print_num = self.ocr.get_print_num(image, pos)
                        if (math.log10(print_num))+1 > 0 and (int(print_num) > 100) and not flag_global_clicked:
                            name_card = print_num
                            read_series = print_num
                            series = print_num
                            try:
                                self.click_reactions(pos)
                                name_card = self.ocr.get_names_single(
                                    image, pos)
                                print(str(name_card) + str(series) +
                                      self.server_name_list)
                                logging.info("Got Name: " + str(name_card) + " Series: " + str(
                                    read_series) + " Server: " + self.server_name_list + " URL: " + href_link)
                                self.clicked_card = name_card.split(' ', 1)[0]
                                self.flag_clicked = True
                            except:
                                error_count += 1
                                logging.warning(
                                    "Cant Click Edition" + self.server_name_list, exc_info=True)
                        elif(not flag_global_clicked):
                            name_card = self.ocr.get_names_single(
                                image, pos)
                            if (name_card in self.dict_good_stuff) and not flag_global_clicked:
                                series = self.dict_good_stuff.get(
                                    name_card, '-1')
                                read_series = self.ocr.get_names_bottom(
                                    image, pos).split(' ', 1)[0]
                                if series == '123456' or read_series == series:
                                    try:
                                        self.click_reactions(pos)
                                        print(name_card + " " + series +
                                              " " + self.server_name_list)
                                        logging.info("Got Name: " + name_card + " Series: " + read_series +
                                                     " Server: " + self.server_name_list + " URL: " + href_link)
                                        self.clicked_card = name_card.split(' ', 1)[
                                            0]
                                        self.flag_clicked = True
                                    except:
                                        error_count += 1
                                        logging.warning(
                                            "Cant Click Edition " + self.server_name_list, exc_info=True)
                            elif name_card in self.dict_good_stuff_addition and not flag_global_clicked:
                                series = self.dict_good_stuff_addition.get(
                                    name_card, '-1')
                                read_series = self.ocr.get_names_bottom(
                                    image, pos).split(' ', 1)[0]
                                if series == '123456' or read_series == series:
                                    if name_card in char_numbers:
                                        edition = self.ocr.get_edition_number(
                                            image, pos)
                                        if edition == char_numbers[name_card]:
                                            try:
                                                self.click_reactions(
                                                    pos)
                                                print(
                                                    name_card + " " + series + " " + self.server_name_list)
                                                logging.info("Got Name: " + name_card + " Series: " + read_series +
                                                             " Server: " + self.server_name_list + " URL: " + href_link)
                                                self.clicked_card = name_card.split(' ', 1)[
                                                    0]
                                                self.flag_clicked = True
                                            except:
                                                error_count += 1
                                                logging.warning(
                                                    "Cant Click Edition " + self.server_name_list, exc_info=True)
                        pos -= 1
                    flag_finished = True
                except:
                    error_count += 1
                    logging.error("Exception occurred", exc_info=True)
                    logging.warning(
                        "Cant get card name:" + href_link + " pos:" + str(pos) + " w:" + str(w))
            except:
                logging.warning("Error")
                logging.error("Exception occurred", exc_info=True)
                error_count += 1

    def debug_on(self):
        global flag_debug
        flag_debug = not flag_debug

    def get_webelement_id(self):
        return self.driver.find_element_by_id(self.curr_id)

    def click_reactions(self, pos):
        global flag_global_clicked
        global flag_cd_grab
        try:
            reactions_container = WebDriverWait(self.driver.find_element_by_id(
                self.curr_id), 600, poll_frequency=0.05).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'reactions-12N0jA')))
            reactions = WebDriverWait(reactions_container, 600, poll_frequency=0.05).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'reaction-1hd86g')))

            while len(reactions) < pos+1:
                reactions = reactions_container.find_elements(
                    By.CLASS_NAME, 'reaction-1hd86g')
            if not flag_global_clicked:
                self.driver.execute_script("arguments[0].click();", reactions[pos].find_element(
                    By.CLASS_NAME, 'reactionInner-15NvIl'))
                flag_global_clicked = True
                print("clicked 1")
        except:
            time.sleep(0.05)
            logging.info("Failed to Click 1st " +
                         self.server_name_list, exc_info=True)
            try:
                logs = self.get_webelement_id()
                reactions_container = WebDriverWait(logs, 600, poll_frequency=0.05).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'reactions-12N0jA')))
                reactions = WebDriverWait(reactions_container, 600, poll_frequency=0.05).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'reaction-1hd86g')))
                while len(reactions) < pos+1:
                    reactions = reactions_container.find_elements(
                        By.CLASS_NAME, 'reaction-1hd86g')
                if not flag_global_clicked:
                    self.driver.execute_script("arguments[0].click();", reactions[pos].find_element(
                        By.CLASS_NAME, 'reactionInner-15NvIl'))
                    flag_global_clicked = True
                    print("clicked 2")
            except:
                logging.info("Failed to Click 2nd " +
                             self.server_name_list, exc_info=True)

    def button_click(self, pos):
        global flag_global_clicked
        global flag_cd_grab
        try:
            logs = self.driver.find_element_by_id(
                self.curr_id)
            reactions_container = WebDriverWait(logs, 600, poll_frequency=0.05).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'children-2goeSq')))
            reactions = WebDriverWait(reactions_container, 600, poll_frequency=0.05).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'button-38aScr')))
            if not flag_global_clicked:
                WebDriverWait(logs, 600, poll_frequency=0.05).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'button-38aScr')))
                self.driver.execute_script(
                    "arguments[0].click();", reactions[pos])
                flag_global_clicked = True
                print("clicked 1")
        except:
            time.sleep(0.05)
            logging.info("Failed to Click 1st " +
                         self.server_name_list, exc_info=True)
            try:
                logs = self.get_webelement_id()
                reactions_container = WebDriverWait(logs, 600, poll_frequency=0.05).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'children-2goeSq')))
                reactions = WebDriverWait(reactions_container, 600, poll_frequency=0.05).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'button-38aScr')))
                if not flag_global_clicked:
                    WebDriverWait(logs, 600, poll_frequency=0.05).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, 'button-38aScr')))
                    self.driver.execute_script(
                        "arguments[0].click();", reactions[pos])
                    flag_global_clicked = True
                    print("clicked 2")
            except:
                logging.info("Failed to Click 2nd " +
                             self.server_name_list, exc_info=True)

    def action_href_img_button(self):
        global flag_global_clicked
        global flag_cd_grab

        error_count = 0
        flag_finished = False
        while(error_count < 5 and not flag_finished):
            try:
                img_container = self.driver.find_element_by_id(
                    self.curr_id).find_element_by_class_name('anchor-3Z-8Bb')
                href_link = img_container.get_attribute('href')

                error_count_image = 0
                try:
                    image = url_to_image(href_link)
                    while image is None:
                        error_count_image += 1
                        if error_count_image > 10:
                            break
                        logging.info("Cant get image:" +
                                     href_link + " " + str(error_count_image))
                        image = url_to_image(href_link)
                    h, w, c = image.shape
                except:
                    time.sleep(0.1)
                    logging.warning("Cant get image:" + href_link)
                    logging.warning("Unexpected error:", sys.exc_info()[0])
                    error_count += 1
                    continue
                max = 4 if w > 900 else 3
                pos = max-1
                try:
                    while pos >= 0 and not self.flag_clicked:
                        print_num = self.ocr.get_print_num(image, pos)
                        if (math.log10(print_num))+1 > 0 and (int(print_num) > 100) and not flag_global_clicked:
                            name_card = print_num
                            read_series = print_num
                            series = print_num
                            try:
                                self.button_click(pos)
                                name_card = self.ocr.get_names_single(
                                    image, pos)
                                print(str(name_card) + str(series) +
                                      self.server_name_list)
                                logging.info("Got Name: " + str(name_card) + " Series: " + str(
                                    read_series) + " Server: " + self.server_name_list + " URL: " + href_link)
                                self.clicked_card = name_card.split(' ', 1)[0]
                                self.flag_clicked = True
                            except:
                                error_count += 1
                                logging.warning(
                                    "Cant Click Edition " + self.server_name_list, exc_info=True)
                        else:
                            name_card = self.ocr.get_names_single(
                                image, pos)
                            if (name_card in self.dict_good_stuff and not flag_global_clicked):
                                series = self.dict_good_stuff.get(
                                    name_card, '-1')
                                read_series = self.ocr.get_names_bottom(
                                    image, pos).split(' ', 1)[0]

                                if series == '123456' or read_series == series:
                                    try:
                                        self.button_click(pos)
                                        print(name_card + " " + series +
                                              " " + self.server_name_list)
                                        logging.info("Got Name: " + name_card + " Series: " + read_series +
                                                     " Server: " + self.server_name_list + " URL: " + href_link)
                                        self.clicked_card = name_card.split(' ', 1)[
                                            0]
                                        self.flag_clicked = True
                                    except:
                                        error_count += 1
                                        logging.warning(
                                            "Cant Click Edition " + self.server_name_list, exc_info=True)
                            elif (name_card in self.dict_good_stuff_addition and not flag_global_clicked):
                                series = self.dict_good_stuff_addition.get(
                                    name_card, '-1')
                                read_series = self.ocr.get_names_bottom(
                                    image, pos).split(' ', 1)[0]

                                if series == '123456' or read_series == series:
                                    if name_card in char_numbers:
                                        edition = self.ocr.get_edition_number(
                                            image, pos)
                                        if edition == char_numbers[name_card]:
                                            try:
                                                self.button_click(
                                                    pos)
                                                print(
                                                    name_card + " " + series + " " + self.server_name_list)
                                                logging.info("Got Name: " + name_card + " Series: " + read_series +
                                                             " Server: " + self.server_name_list + " URL: " + href_link)
                                                self.clicked_card = name_card.split(' ', 1)[
                                                    0]
                                                self.flag_clicked = True
                                            except:
                                                error_count += 1
                                                logging.warning(
                                                    "Cant Click Edition " + self.server_name_list, exc_info=True)
                        pos -= 1
                    flag_finished = True
                except:
                    error_count += 1
                    logging.error("Exception occurred", exc_info=True)
                    logging.warning(
                        "Cant get card name:" + href_link + " pos:" + str(pos) + " w:" + str(w))
            except:
                logging.warning("Error")
                logging.error("Exception occurred", exc_info=True)
                error_count += 1

    def action_href_img_button_dropping(self):
        if self.counter > 100:
            if (time.time() - self.time) > self.sleep_timer_drop:
                logging.warning('Drop')
                textbox = self.driver.find_element_by_class_name(
                    'markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP')
                textbox.send_keys('kd')
                textbox.send_keys(Keys.ENTER)
                self.time = time.time()
            self.counter = 0
        self.counter += 1
        self.action_href_img_button()

    def start_up(self):
        self.login_sign()
        self.message_log(self.condition_BOT_droppping, self.action_href_img)

    def start_up_button(self):
        self.login_sign()
        self.message_log(self.condition_BOT_droppping,
                         self.action_href_img_button)

    def start_up_button_dropping(self):
        self.login_sign()
        self.message_log(self.condition_BOT_droppping,
                         self.action_href_img_button_dropping)

    def start_up_server(self):
        self.login_sign()
        self.message_log(self.condition_BOT_droppping_Server,
                         self.action_href_img)

    def start_up_kd(self):
        self.login_sign()
        self.kd_every()
