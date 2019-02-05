# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

download_dir = './downloads'
options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)

for i in range(2, 10):
    url = "https://freemusicarchive.org/search/?adv=1&quicksearch=&search-genre=Electronic&duration_from=&duration_to=&music-filter-CC-attribution-only=on&music-filter-CC-attribution-sharealike=1&music-filter-CC-attribution-noderivatives=1&music-filter-public-domain=1&music-filter-commercial-allowed=1&sort=track_interest&d=1&page=" + str(i) + "&per_page=200" 
    driver.get(url)
    dl_buttons = driver.find_elements_by_class_name('icn-arrow')

    for btn in dl_buttons:
        btn.click()

        while any(fn.endswith('crdownload') for fn in os.listdir(download_dir)):
            time.sleep(2)
