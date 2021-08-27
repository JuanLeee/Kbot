from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time
import sys
from selenium import webdriver

from card_image import *
from selenium_login import *


import time
import os

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