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

# hash_table = hash_table_create('images')

load_dotenv()
drivers_list = []
action_list = []
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
# 'guildsnav___704015125958623422','channels___744577282680684664',
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--enable-features=VaapiVideoDecoder")
chrome_options.add_argument("--ignore-gpu-blocklist")
chrome_options.add_argument("--enable-zero-copy")
chrome_options.add_argument("--disable-gpu-driver-bug-workarounds")
chrome_options.add_argument("--enable-accelerated-video-decode")
chrome_options.add_argument('--use-gl=desktop')
chrome_options.add_argument("--ignore-gpu-blacklist")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("disable-infobars")
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
chrome_options.add_experimental_option('prefs', prefs)

chrome_options.add_argument("start-maximized")

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--headless")

# chrome_options.set_preference("dom.push.enabled", False)
# chrome_options.set_preference("media.volume_scale", "0.0")


user_name = os.getenv('DISCORD_USER_NAME')
password = os.getenv('DISCORD_PASSWORD')
id_name = os.getenv('DISCORD_ID_NAME')
user_name1 = os.getenv('DISCORD_USER_NAME_1')
password1 = os.getenv('DISCORD_PASSWORD_1')
id_name1 = os.getenv('DISCORD_ID_NAME_1')
# user_name = input("Enter username:")
# password = input("Enter password:")
# id_name = input("Enter your discord username:")
# id_name = "@" + id_name
threads = []
discord_scrapers = []

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


driver_temp = webdriver.Chrome(options=chrome_options)


action=ActionChains(driver_temp)
drivers_list.append(driver_temp)
action_list.append(action)
temp_ds = Discord_Scraper(driver_temp, action ,user_name, password, 'guildsnav___817561247062818829', 'channels___817563077816877116','XO',False,id_name,True)
x = threading.Thread(target=temp_ds.start_up_kd,args=())
threads.append(x)
discord_scrapers.append(temp_ds)
x.start()
time.sleep(10)

for server_name, channel_name,server_name_list in zip(server_list, channel_list,server_name_list):
    driver = webdriver.Chrome(options=chrome_options)

    action= ActionChains(driver)
    drivers_list.append(driver)
    action_list.append(action)
    temp_ds = Discord_Scraper(driver, action ,user_name, password, server_name, channel_name,server_name_list,False,id_name,True)
    x = threading.Thread(target=temp_ds.start_up,args=())
    discord_scrapers.append(temp_ds)
    threads.append(x)
    x.start()
    time.sleep(10)

    
for server_name, channel_name,server_name_list in zip(server_list_button, channel_list_button,server_name_list_button):
    driver = webdriver.Chrome(options=chrome_options)

    action= ActionChains(driver)
    drivers_list.append(driver)
    action_list.append(action)
    temp_ds = Discord_Scraper(driver, action ,user_name, password, server_name, channel_name,server_name_list,False,id_name,True)
    x = threading.Thread(target=temp_ds.start_up_button,args=())
    discord_scrapers.append(temp_ds)
    threads.append(x)
    x.start()
    time.sleep(10)


# driver_temp = webdriver.Chrome(options=chrome_options)


# action=ActionChains(driver_temp)
# drivers_list.append(driver_temp)
# action_list.append(action)
# temp_ds = Discord_Scraper(driver_temp, action ,user_name1, password1, 'guildsnav___648031568756998155', 'channels___648044573536550922','Hub 1',False,id_name1,False)
# x = threading.Thread(target=temp_ds.start_up_button_dropping,args=())
# threads.append(x)
# discord_scrapers.append(temp_ds)
# x.start()
# time.sleep(30)

# driver_temp = webdriver.Chrome(options=chrome_options)


# action=ActionChains(driver_temp)
# drivers_list.append(driver_temp)
# action_list.append(action)
# temp_ds = Discord_Scraper(driver_temp, action ,user_name1,password1, 'guildsnav___648031568756998155', 'channels___776520559621570621','Hub 2',False,id_name1,False)
# x = threading.Thread(target=temp_ds.start_up_button,args=())
# threads.append(x)
# discord_scrapers.append(temp_ds)
# x.start()
# time.sleep(10)

# second
# driver_temp = webdriver.Chrome(options=chrome_options)

# stealth(driver_temp,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
# action=ActionChains(driver_temp)
# drivers_list.append(driver_temp)
# action_list.append(action)
# temp_ds = Discord_Scraper(driver_temp, action ,user_name, password, 'guildsnav___648031568756998155', 'channels___648044573536550922','Karuta Hub',False,id_name_1)
# x = threading.Thread(target=temp_ds.start_up_hub,args=())
# threads.append(x)
# discord_scrapers.append(temp_ds)
# x.start()
# time.sleep(120)

# for server_name, channel_name,server_name_list in zip(server_list, channel_list,server_name_list):
#     driver = webdriver.Chrome(options=chrome_options)
#     stealth(driver_temp,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
#     action= ActionChains(driver)
#     drivers_list.append(driver)
#     action_list.append(action)
#     temp_ds = Discord_Scraper(driver, action ,user_name_1, password_1, server_name, channel_name,server_name_list,False,id_name_1)
#     x = threading.Thread(target=temp_ds.start_up_server,args=())
#     discord_scrapers.append(temp_ds)
#     threads.append(x)
#     x.start()
#     time.sleep(120)

# TEST TEST

# driver_temp = webdriver.Chrome(options=chrome_options)

# action=ActionChains(driver_temp)
# drivers_list.append(driver_temp)
# action_list.append(action)
# temp_ds = Discord_Scraper(driver_temp, action ,user_name, password, 'guildsnav___817561247062818829', 'channels___817563077816877116','XO',False,id_name,True)
# x = threading.Thread(target=temp_ds.start_up_button,args=())
# threads.append(x)
# discord_scrapers.append(temp_ds)
# x.start()
# time.sleep(10)


flag_stop = False
while not flag_stop:
    print("waiting")
    if input() == 'q':
        flag_stop = True
        for t,d in zip(threads,discord_scrapers):
            print("Stopped")
            d.flag_stop_true()
            t.join()
        break
    elif input() == 'd':
        for t,d in zip(threads,discord_scrapers):
            d.debug_on()
    time.sleep(5)



 