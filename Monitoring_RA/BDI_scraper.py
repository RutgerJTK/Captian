import requests
from bs4 import BeautifulSoup
import xlsxwriter 

def read_spec():
    spec_file = "D:\Code\Captian\Data\species_ln.txt"
    names = [line.rstrip('\n') for line in open(spec_file).readlines()]
    print(names)
    return names

def get_site(spec_names):
    url = "https://species.biodiversityireland.ie/?keyword=Catalogue%20of%20Irelands%20Non-native%20Species"
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    print(soup)

def main():
    spec_names = read_spec()
    get_site(spec_names)
    # Your code here

if __name__ == "__main__":
    main()