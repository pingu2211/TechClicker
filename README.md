# TechClicker
## Install Manualy
### Install Python
sudo apt-get install python3 python3-pip

### Install Firefox
sudo apt-get install firefox

### Install Selenium
sudo pip install selenium

### Install GeckoDriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz<br>
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver'<br>
sudo chmod +x /usr/bin/geckodriver<br>
rm geckodriver-v0.26.0-linux64.tar.gz<br>

### Get the Clicker
wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/UbuntuSetupScript.sh<br>

### Run the Clicker
nohup python3 TechClicker.py <br>

## Using the Install script
wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/UbuntuSetupScript.sh<br>
sudo chmod +x UbuntuSetupScript.sh<br>
./UbuntuSetupScript.sh<br>
wget https://raw.githubusercontent.com/pingu2211/TechClicker/master/TechClicker.py<br>
nohup python3 TechClicker.py 
