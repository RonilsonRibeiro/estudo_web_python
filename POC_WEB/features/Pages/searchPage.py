from selenium.webdriver.common.keys import Keys

class Search():

    def __init__(self, driver):
        self.driver = driver

        self.searchBox_textBox_id = "q"
        
    
    def search_content(self, content):
        self.driver.find_element_by_name(self.searchBox_textBox_id).clear()
        self.driver.find_element_by_name(self.searchBox_textBox_id).send_keys(content + Keys.RETURN)

    

class Result():

    def __init__(self, driver):
        self.driver = driver

        self.santander_link_class = "LC20lb"

    def click_highlight_result(self):
        self.driver.find_element_by_class_name(self.santander_link_class).click()