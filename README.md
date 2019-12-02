# TechClicker
## Install Python
sudo apt-get install python3
sudo apt-get install python3-pip

## Install Firefox
sudo apt-get install firefox

## Install Selenium
sudo pip install selenium

## Install GeckoDriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
rm geckodriver-v0.26.0-linux64.tar.gz
