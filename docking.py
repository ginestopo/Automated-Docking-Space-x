'''
Automated system to Dock SpaceX crew Dragon 9 to
International Space Station using spacex simulator

https://iss-sim.spacex.com/

by Gines Diaz Chamorro
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def wait(time_to_wait):
    i = 0
    while(i<time_to_wait): #wait until menu loads
        time.sleep(1)
        i = i + 1
        print(time_to_wait-i)

driver = webdriver.Firefox() #creating Firefox instance

#confirming that SPACEX is included in the title
driver.get("https://iss-sim.spacex.com/")
assert "SPACEX" in driver.title

wait(6);
print("\nLaunched\n")

begin = driver.find_element_by_xpath("//*[@id="+"\"begin-button\""+"]").click()

wait(16);
print("\nController Activated\n")

dato = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[1]")

while(True):
    print(dato.text)

#to ensure some results are found
assert "No results found." not in driver.page_source

#closing tab
driver.close()
