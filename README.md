# Free Music Archive Scraper

Downloading music from the [Free Music Archive](https://freemusicarchive.org) using the [Chrome Web Driver](http://chromedriver.chromium.org/downloads) with python 2.

Instructions
---
* Install Chrome Driver

```
pip install selenium
wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
chmod +x chromedriver
mv chromedriver ~/bin
rm chromedriver_mac64.zip
```

* Adapt URL to your needs
* Launch download with `python main.py`