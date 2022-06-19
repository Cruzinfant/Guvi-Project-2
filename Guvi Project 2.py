from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from csv import writer
import pytest
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

        with open('Flipkart Laptops List.csv', 'w', encoding='utf8', newline='') as lap:
            thewriter = writer(lap)
            header = ['Model Name', 'price']
            thewriter.writerow(header)

            for data in self.soup.findAll('div', class_='_3pLy-c row'):
                names = data.find('div', class_='_4rR01T').text
                price = data.find('div', class_='_30jeq3 _1_WHN1').text
                products.append(names)
                prices.append(price)
                info = [names, price]
                thewriter.writerow(info)


    def mobile_Config(self):

        search = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input'
        # self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/button').click()
        self.driver.find_element(by=By.XPATH, value=search).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.XPATH, value=search).send_keys(Keys.DELETE)
        self.driver.find_element(by=By.XPATH, value=search).send_keys('Mobiles')
        self.driver.find_element(by=By.XPATH, value=search).submit()
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0,1000)", "")
        ram_4gb = '/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[1]/div/label/div[2]'
        self.driver.find_element(by=By.XPATH, value=ram_4gb).click()
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,1000)", "")
        ram_6gb = '/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[7]/div[2]/div/div[6]/div/label/div[2]'
        self.driver.find_element(by=By.XPATH, value=ram_6gb).click()
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,1000)", "")
        storage = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[8]/div[1]/div'
        self.driver.find_element(by=By.XPATH, value=storage).click()
        storage_128 = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[8]/div[2]/div/div[2]/div/label/div[2]'
        self.driver.find_element(by=By.XPATH, value=storage_128).click()
        time.sleep(3)

    def ScarpMobile(self):
        url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3D6%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB'
        data = requests.get(url)
        self.soup = BeautifulSoup(data.content, 'lxml')
        products = []
        prices = []

        with open('Flipkart Mobile list.csv', 'w', encoding='utf8', newline='') as Mob:
            thewriter = writer(Mob)
            header = ['Model Name', 'price']
            thewriter.writerow(header)

            for data in self.soup.findAll('div', class_='_3pLy-c row'):
                names = data.find('div', class_='_4rR01T').text
                price = data.find('div', class_='_30jeq3 _1_WHN1').text
                products.append(names)
                prices.append(price)
                info = [names, price]
                thewriter.writerow(info)

    def amazon_login(self):
        url = 'https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=6384569186943866916&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007810&hvtargid=kwd-10573980&hydadcr=14453_2154373&gclid=Cj0KCQjwkruVBhCHARIsACVIiOxvLunlSsNy3d7Ej3JTaPciUzLi1eL4LVDdVPXEwm37cbkj415FYFYaAl9nEALw_wcB'
        self.driver.get(url)

    def a_laptop_config(self):
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').click()
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys('Laptops')
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').submit()
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[12]/span/a/span').click()
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0,1500)", "")
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/li[5]/span/a/span').click()
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0,3000)", "")
        self.driver.find_element(by=By.XPATH, value='//*[@id="p_n_feature_twenty-six_browse-bin/27399070031"]/span/a/span').click()
        time.sleep(5)

    def a_scrapinfo(self):
        url = 'https://www.amazon.in/s?k=Laptops&i=computers&rh=n%3A1375424031%2Cp_n_feature_thirteen_browse-bin%3A12598162031%2Cp_n_pattern_browse-bin%3A8609969031%2Cp_n_feature_twenty-six_browse-bin%3A27399070031&dc&ds=v1%3ApOuu4fh2V4xuvksRkiTNEMbmKstQFeM2XP20WgRsojU&qid=1655670637&rnid=27399067031&ref=sr_nr_p_n_feature_twenty-six_browse-bin_3'
        data = requests.get(url)
        self.soup = BeautifulSoup(data.content, 'lxml')
        products = []
        prices = []

        with open('Amazon_Laptops.csv', 'w', encoding='utf8', newline='') as lap:
            thewriter = writer(lap)
            header = ['Model Name', 'price']
            thewriter.writerow(header)
            time.sleep(3)
            for data in self.soup.findAll('div', class_='s-card-container s-overflow-hidden aok-relative s-include-content-margin s-latency-cf-section s-card-border'):
                names = data.find('span', class_='a-size-medium a-color-base a-text-normal').text
                price = data.find('span', class_='a-price-whole').text
                products.append(names)
                prices.append(price)
                info = [names, price]
                thewriter.writerow(info)

    def mobile_config(self ):
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').click()
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys(Keys.DELETE)
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys("Mobiles")
        self.driver.find_element(by=By.ID, value='twotabsearchtextbox').submit()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.driver.find_element(by=By.XPATH, value ='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[3]/span/a/span').click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.driver.find_element(by=By.XPATH, value= '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[2]/span/a/span').click()
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.driver.find_element(by=By.XPATH, value= '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[3]/li[7]/span/a/span').click()

    def a_ScarpMobile(self):
        url = 'https://www.amazon.in/s?k=Mobiles&i=electronics&rh=n%3A1805560031%2Cp_n_feature_seven_browse-bin%3A16757455031%7C8561133031%2Cp_n_feature_eight_browse-bin%3A8561112031&dc&ds=v1%3AFMbvNQnN2%2FqKGRtXo5ivGg4lDFcioYYbAZsPrnlke%2BY&qid=1655675618&rnid=8561111031&ref=sr_nr_p_n_feature_eight_browse-bin_7'
        data = requests.get(url)
        self.soup = BeautifulSoup(data.content, 'lxml')
        products = []
        prices = []

        with open('Amazon.csv', 'w', encoding='utf8', newline='') as mob:
            thewriter = writer(mob)
            header = ['Model Name', 'price']
            thewriter.writerow(header)

            for data in self.soup.findAll('div', class_='s-card-container s-overflow-hidden aok-relative s-include-content-margin s-latency-cf-section s-card-border'):
                names = data.find('span', class_='a-size-medium a-color-base a-text-normal').text
                price = data.find('span', class_='a-price-whole').text
                products.append(names)
                prices.append(price)
                info = [names, price]
                thewriter.writerow(info)


Web = Webscraping()
Web.flipkart_login()
Web.laptop_config()
Web.scrapinfo()
Web.mobile_Config()
Web.ScarpMobile()
Web.amazon_login()
Web.a_laptop_config()
Web.a_scrapinfo()
Web.mobile_config()
Web.a_ScarpMobile()



