#!/bin/bash
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install firefox
sudo pip install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz 
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver' 
sudo chmod +x /usr/bin/geckodriver 
rm geckodriver-v0.26.0-linux64.tar.gz
wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/TechClicker.sh
sudo chmod +x ./TechClicker.py 
nohup python3 TechClicker.py 
