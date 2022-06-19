from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from csv import writer
import time
import requests


# Creating a class to commence Project
class Webscraping:

    # Importing Mozila driver
    driver = webdriver.Firefox(executable_path=r"C:\WebDriver\geckodriver1.exe")
    url_flipkart = 'https://www.flipkart.com/'
    time.sleep(1)

    # Loging into the Flipkart website
    def flipkart_login(self):
        self.driver.get(self.url_flipkart)
        search = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input'
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/button').click()
        self.driver.find_element(by=By.XPATH, value=search).send_keys('Laptops')
        self.driver.find_element(by=By.XPATH, value=search).submit()
        time.sleep(3)

    # Using Filters to scrap the configuration given
    def laptop_config(self):
        # Filter by Processor i5
        processor = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[2]/div/label'
        self.driver.find_element(by=By.XPATH, value=processor).click()
        time.sleep(5)

        # Filter by 8GB ram
        self.driver.execute_script("window.scrollBy(0,1500)", "")
        ram1 = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[18]/div/div'
        self.driver.find_element(by=By.XPATH, value=ram1).click()
        ram2 = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[18]/div[2]/div/div[1]/div/label/div[2]'
        self.driver.find_element(by=By.XPATH, value=ram2).click()
        time.sleep(3)

        # Filter by 1 TB Hardisk Capacity
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        hdd1 = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div/div'
        self.driver.find_element(by=By.XPATH, value=hdd1).click()
        hdd2 = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div[2]/div/div[1]/div/label/div[2]'
        self.driver.find_element(by=By.XPATH, value=hdd2).click()

        # Sorting price of the products by low to high
        sort = '/html/body/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[3]'
        element = self.driver.find_element(by=By.XPATH, value=sort)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)

    # Scrapping the info in current web page
    def scrapinfo(self):
        url = 'https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.system_memory%255B%255D%3D8%2BGB&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&p%5B%5D=facets.hard_disk_capacity%255B%255D%3D1%2BTB'
        data = requests.get(url)
        self.soup = BeautifulSoup(data.content, 'lxml')
        products = []
        prices = []

        with open('Laptops.csv', 'w', encoding='utf8', newline='') as lap:
            thewriter = writer(lap)
            header = ['Model Name', 'price']
            thewriter.writerow(header)
            for data in self.soup.findAll('div', class_='_3pLy-c row'):
                names = data.find('div', class_='_4rR01T')
                price = data.find('div', class_='_30jeq3 _1_WHN1')
                products.append(names.text)
                prices.append(price.text)

        print(products)
        print(prices)


Web = Webscraping()
Web.flipkart_login()
Web.laptop_config()
Web.scrapinfo()
