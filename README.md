# TechClicker

Before either install options  
``sudo apt-get update & sudo apt-get upgrade``  

## Install Manualy
### Install Python
``sudo apt-get install python3 python3-pip``

### Install Firefox
``sudo apt-get install firefox``

### Install Selenium
``sudo pip install selenium || sudo pip3 install selenium``

### Install GeckoDriver
``wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz`` 
``sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver'``  
``sudo chmod +x /usr/bin/geckodriver``  
``rm geckodriver-v0.26.0-linux64.tar.gz``  

### Get the Clicker
``wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/UbuntuSetupScript.sh``  

### Run the Clicker
``nohup python3 TechClicker.py``  

## Using the Install script
``wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/UbuntuSetupScript.sh``  
``sudo chmod +x UbuntuSetupScript.sh``  
``./UbuntuSetupScript.sh``  
``wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/TechClicker.py``  
``nohup python3 TechClicker.py``  
