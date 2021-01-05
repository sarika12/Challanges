from selenium import webdriver
from selenium.webdriver.common.by import  By
import  os
class RunChrome():
    def testMethod1(self):
        # i remove this path beccuase 
        # chrome_location="D:\\selenium\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"]= chrome_location
        driver=webdriver.Chrome()
        driver.get("https://letskodeit.teachable.com/p/practice")


        findElementByClass =driver.find_elements(By.CLASS_NAME,"inputs")
        find_len_class=len(findElementByClass)
        if findElementByClass is not None :
            print("Class is presnt please print the len"+str(find_len_class))
        findElementBytag=driver.find_elements(By.TAG_NAME,"td")
        find_len_tag=len(findElementBytag)
        if findElementBytag is not None :
            print("Class is presnt please print the len"+str(find_len_tag))
        print ("let code it ")
t=RunChrome()
t.testMethod1()
