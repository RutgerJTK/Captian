from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import re 

def read_species(species_list):
    with open(species_list, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        return data

def scrape_waarnemingen_species_nrs(species_data):
    s = Service("D:\\Code\\Captian\\chromedriver.exe")  # Specify the path to your chromedriver executable
    driver = webdriver.Chrome(service=s)
    
    url = "https://waarneming.nl/species/search/?q=Alternanthera+philoxeroides&species_group=0&deep=on&include_inactive=on"
    driver.get(url)
    driver.implicitly_wait(15)  # Adjust the waiting time as needed
    driver.find_element(By.XPATH, '(//a//i)[1]').click()
    driver.implicitly_wait(10)  
    spec_id = re.findall("[0-9]{1,9}", driver.current_url)[0]
    
    pass

def main():
    species_list = "D:\Code\Captian\Data\species_ln.txt"
    species_data = read_species(species_list)
    scrape_waarnemingen_species_nrs(species_data)

if __name__ == "__main__":
    main()