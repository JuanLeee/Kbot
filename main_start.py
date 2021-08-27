from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import logging
import threading
import time
import logging.handlers
import sys
from selenium import webdriver

from card_image import *
from selenium_login import *


import time
import os
from dotenv import load_dotenv


filename = "botting_logs.log"


# your logging setup

should_roll_over = os.path.isfile(filename)
handler = logging.handlers.RotatingFileHandler(filename, mode='w', backupCount=20,delay=True)
if should_roll_over:  # log already exists, roll over!
    handler.doRollover()

logging.basicConfig(filename=filename, encoding='utf-8', level=logging.INFO, force=True)



server_list = [
    # 'guildsnav___752315009324941343'
                # ,'guildsnav___817561247062818829'
                'guildsnav___721059198816747580'
                ,'guildsnav___704015125958623422'
                ,'guildsnav___540784184470274069'
                ,'guildsnav___821165740711346238'
                # ,'guildsnav___821165740711346238'
                ,'guildsnav___632548882231984129'
                # ,'guildsnav___819339531122638888'
                # ,'guildsnav___648031568756998155'
                ]
channel_list = [
    # 'channels___763438026168074261'
            # ,'channels___817563077816877116'
            'channels___846619170661859398'
            ,'channels___744577282680684664'
            ,'channels___817045744845586452'
            ,'channels___848772351645450311'
            # ,'channels___874768183704322088'
            ,'channels___829646818996256788'
            # , 'channels___819369794993389569'
            # ,'channels___648044573536550922'
            ]
server_name_list = [
    # "KaruDye"
                    # ,'XO'
                    "City"
                    ,"Good Vibes"
                    ,"My Anime Land"
                    ,'Cafe'
                    # ,'Cafe Server'
                    ,'Hangout'
                    # , 'Spanish Bois'
                    # ,'Karuta Hub'
                    ]

server_list_button = [
                'guildsnav___819339531122638888'
    ,'guildsnav___752315009324941343'
                ,'guildsnav___817561247062818829'
                # ,'guildsnav___721059198816747580'
                # 'guildsnav___704015125958623422'
                # ,'guildsnav___540784184470274069'
                # ,'guildsnav___821165740711346238'
                # ,'guildsnav___632548882231984129'
                # ,'guildsnav___648031568756998155'
                ]
channel_list_button = [
    'channels___819369794993389569'
    ,'channels___763438026168074261'
            ,'channels___817563077816877116'
            # ,'channels___846619170661859398'
            # 'channels___744577282680684664'
            # ,'channels___817045744845586452'
            # ,'channels___848772351645450311'
            # ,'channels___829646818996256788'
            # ,'channels___648044573536550922'
            ]
server_name_list_button = [
    'Spanish Bois'
    ,"KaruDye"
                    ,'XO'
                    # ,"City"
                    # "Good Vibes"
                    # ,"My Anime Land"
                    # ,'Cafe'
                    # ,'Hangout'
                    # ,'Karuta Hub'
                    ]
flag_server_list = [False,True,False,False,False,False,False]

class Main:
    def __init__(self,user_name,password,id_name):
        # chrome_options.add_argument("--headless")

        # chrome_options.set_preference("dom.push.enabled", False)
        # chrome_options.set_preference("media.volume_scale", "0.0")
        self.user_name = user_name
        self.password = password
        self.id_name = id_name
        # 'guildsnav___704015125958623422','channels___744577282680684664',
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("no-sandbox")
        # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--enable-features=VaapiVideoDecoder")
        self.chrome_options.add_argument("--ignore-gpu-blocklist")
        self.chrome_options.add_argument("--enable-zero-copy")
        self.chrome_options.add_argument("--disable-gpu-driver-bug-workarounds")
        self.chrome_options.add_argument("--enable-accelerated-video-decode")
        self.chrome_options.add_argument('--use-gl=desktop')
        self.chrome_options.add_argument("--ignore-gpu-blacklist")
        self.chrome_options.add_argument("--disable-software-rasterizer")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--mute-audio")
        self.chrome_options.add_argument("--disable-plugins-discovery")
        self.chrome_options.add_argument("disable-infobars")
        prefs = {"profile.managed_default_content_settings.images":1,
                "profile.default_content_setting_values.notifications":2,
                "profile.managed_default_content_settings.stylesheets":2,
                "profile.managed_default_content_settings.cookies":1,
                "profile.managed_default_content_settings.javascript":1,
                "profile.managed_default_content_settings.plugins":2,
                "profile.managed_default_content_settings.popups":2,
                #  "profile.managed_default_content_settings.geolocation":2,
                #  "profile.managed_default_content_settings.media_stream":2,
                #  "profile.managed_javascript_blocked_for_urls":'https://cdn.discordapp.com/',
                'disk-cache-size': 4096
        }
        prefs = {'profile.default_content_setting_values': {'cookies': 2,  
                                    'plugins': 2, 'popups': 2, 'geolocation': 2, 
                                    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                                    'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                                    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                                    'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                                    'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                                    'durable_storage': 2}}
        self.chrome_options.add_experimental_option('prefs', prefs)

        self.chrome_options.add_argument("start-maximized")

        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.threads = []
        self.discord_scrapers = []
        self.drivers_list = []
        self.action_list = []
    
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)
     
    # Type 1 -> Dropping
    # Type 2 -> Reactions
    # Type 3 -> Buttons
    # Type 4 -> Buttons + Dropping
    def add_thread(self, server_name, channel_name,server_nickname,timer,type):
        driver_temp = webdriver.Chrome(options=self.chrome_options)
        action=ActionChains(driver_temp)
        self.drivers_list.append(driver_temp)
        self.action_list.append(action)
        temp_ds = Discord_Scraper(driver_temp, action ,self.user_name, self.password, server_name, channel_name,server_nickname,self.id_name,timer)
        if type == 1:
            x = threading.Thread(target=temp_ds.start_up_kd,args=())
        elif type == 2:
            x = threading.Thread(target=temp_ds.start_up,args=())
        elif type == 3:
            x = threading.Thread(target=temp_ds.start_up_button,args=())
        elif type == 4:
            x = threading.Thread(target=temp_ds.start_up_button_dropping,args=())
        self.threads.append(x)
        self.discord_scrapers.append(temp_ds)
        
    def run_threads(self,sleep_timer):
        for thread in self.threads:
            thread.start()
            time.sleep(sleep_timer)
            
    def debug_stop_loop(self):
        flag_stop = False
        while not flag_stop:
            print("waiting")
            if input() == 'q':
                flag_stop = True
                for t,d in zip(self.threads,self.discord_scrapers):
                    print("Stopped")
                    d.flag_stop_true()
                    t.join()
                break
            elif input() == 'd':
                for t,d in zip(self.threads,self.discord_scrapers):
                    d.debug_on()
            time.sleep(5)
            

load_dotenv()
user_name = os.getenv('DISCORD_USER_NAME')
password = os.getenv('DISCORD_PASSWORD')
id_name = os.getenv('DISCORD_ID_NAME')    
user_name1 = os.getenv('DISCORD_USER_NAME_1')
password1 = os.getenv('DISCORD_PASSWORD_1')
id_name1 = os.getenv('DISCORD_ID_NAME_1')



main = Main(user_name,password,id_name)
main.add_thread('guildsnav___540784184470274069', 'channels___817045744845586452','My Anime Land',True,1)
for server_name, channel_name,server_name_list in zip(server_list, channel_list,server_name_list):
    main.add_thread(server_name, channel_name,server_name_list,True,2)
for server_name, channel_name,server_name_list in zip(server_list_button, channel_list_button,server_name_list_button):
    main.add_thread(server_name, channel_name,server_name_list,True,3)
main.run_threads(10)
main.debug_stop_loop()



# main1 = Main(user_name1,password1,id_name1)
# main1.add_thread('guildsnav___648031568756998155', 'channels___648044573536550922','Hub 1',False,4)
# main1.add_thread('guildsnav___648031568756998155', 'channels___776520559621570621','Hub 2',False,3)
# main1.run_threads(30)
# main1.debug_stop_loop()



# TEST TEST
# main3 = Main(user_name,password,id_name)
# main3.add_thread('guildsnav___817561247062818829', 'channels___817563077816877116','XO',True,3)
# main3.run_threads(0)
# main3.debug_stop_loop()



 