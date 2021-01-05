from selenium import webdriver
class RunFirst:
    def testMethod(self):
        driver=webdriver.Firefox(executable_path="D:\\selenium\\geckodriver.exe")
        driver.get("http://www.letskodeit.com")
        print ("let code it ")
t=RunFirst
t.testMethod()
