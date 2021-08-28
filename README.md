
<!-- About The Project -->
# Discord Scraper

Discord Scraper made with python, selenium, openCV and tesseract(OCR)

Filters through messages selecting matching images to react with.

Remade Repository because of sensitive information leaked sorry.

# Built With

* [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR to read images
* [Selenium](https://selenium-python.readthedocs.io) - Webdriver automation
* [OpenCV](https://pypi.org/project/opencv-python/) - Images processing

<!-- GETTING STARTED -->
# Getting Started

# Prerequisites

## Libraries Used

* Selenium
* Discord Webhook
* Numpy
* OpenCV
* Dotenv

## Installation

1. Download and setup [Tesseract](https://github.com/tesseract-ocr/tesseract)

2. Download and setup [Selenium](https://selenium-python.readthedocs.io/installation.html)

3. Clone the repo
   ```sh
   git clone https://github.com/JuanLeee/Kbot.git
   ```
4. Install all packages 
   ```sh
   pip install -r requirements.txt
   ```

5. Setup .env file
   
   **NEED THESE INFORMATION**
   * Discord User Name
     * DISCORD_USER_NAME
   * Discord Password
     * DISCORD_PASSWORD
   * Discord Display Nickname
     * DISCORD_ID_NAME
   * Discord Webhook
     * DISCORD_LINK
   * Server Class Identifier
     * Found through debug on discord page of server of interest
   * Channel Class Identifier
     * Found through debug on discord page of channel of interest

6. Make main_startup script with Object Main
   ```sh
   user_name = os.getenv('DISCORD_USER_NAME')
   password = os.getenv('DISCORD_PASSWORD')
   id_name = os.getenv('DISCORD_ID_NAME')    
   
   main = Main(user_name,password,id_name)
   main.add_thread(server_html_class,channel_html_class,server_name,timer_flag,typing)
   main.run_threads(10)
   main.debug_stop_loop()
   ```

7. Run main file
    ```sh
    py main_start.py
    ```

