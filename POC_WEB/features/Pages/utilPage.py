import yaml
from selenium import webdriver

class Util():

    def screenshot(self, driver, name):
        driver.get_screenshot_as_file('features/Screenshots/' + name + '.png') 

    def validate_text(self, driver, text):
        assert text in driver.page_source

    def yaml_loader(self, filepath):
        with open(filepath, "r", encoding='utf-8') as file_descriptor:
            data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
        return data


  
