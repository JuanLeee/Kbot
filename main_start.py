import logging
import logging.handlers

from main import *

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
                # ,'guildsnav___632548882231984129'
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
            # ,'channels___829646818996256788'
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
                    # ,'Hangout'
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
                ,'guildsnav___632548882231984129'
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
            ,'channels___829646818996256788'
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
<<<<<<< HEAD
                    ,'Hangout'    
=======
                    # ,'Hangout'
>>>>>>> parent of 1013f08 (Cleaned and fixed)
                    # ,'Karuta Hub'
                    ]
flag_server_list = [False,True,False,False,False,False,False]

        
load_dotenv()
user_name = os.getenv('DISCORD_USER_NAME')
password = os.getenv('DISCORD_PASSWORD')
id_name = os.getenv('DISCORD_ID_NAME')    
user_name1 = os.getenv('DISCORD_USER_NAME_1')
password1 = os.getenv('DISCORD_PASSWORD_1')
id_name1 = os.getenv('DISCORD_ID_NAME_1')



<<<<<<< HEAD
main = Main(user_name,password,id_name)
main.add_thread('guildsnav___540784184470274069', 'channels___817045744845586452','My Anime Land',True,1)
for server_name, channel_name,server_name_list in zip(server_list, channel_list,server_name_list):
    main.add_thread(server_name, channel_name,server_name_list,True,2)
for server_name, channel_name,server_name_list in zip(server_list_button, channel_list_button,server_name_list_button):
    main.add_thread(server_name, channel_name,server_name_list,True,3)
main.run_threads(20)
main.debug_stop_loop()



# main1 = Main(user_name1,password1,id_name1)

# main1.add_thread('guildsnav___648031568756998155', 'channels___648044573536550922','Hub 1',False,3)
# main1.add_thread('guildsnav___648031568756998155', 'channels___776520559621570621','Hub 2',False,4)
# main1.run_threads(30)
# main1.debug_stop_loop()
=======
# main = Main(user_name,password,id_name)
# main.add_thread('guildsnav___540784184470274069', 'channels___817045744845586452','My Anime Land',True,1)
# for server_name, channel_name,server_name_list in zip(server_list, channel_list,server_name_list):
#     main.add_thread(server_name, channel_name,server_name_list,True,2)
# for server_name, channel_name,server_name_list in zip(server_list_button, channel_list_button,server_name_list_button):
#     main.add_thread(server_name, channel_name,server_name_list,True,3)
# main.run_threads(10)
# main.debug_stop_loop()



main1 = Main(user_name1,password1,id_name1)
main1.add_thread('guildsnav___648031568756998155', 'channels___648044573536550922','Hub 1',False,3)
main1.add_thread('guildsnav___648031568756998155', 'channels___776520559621570621','Hub 2',False,4)
main1.run_threads(30)
main1.debug_stop_loop()
>>>>>>> parent of 1013f08 (Cleaned and fixed)



# TEST TEST
# main3 = Main(user_name,password,id_name)
# main3.add_thread('guildsnav___648031568756998155', 'channels___648044573536550922','Hub 1',True,3)
# main3.run_threads(0)
# main3.debug_stop_loop()



 