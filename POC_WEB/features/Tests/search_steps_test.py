
# coding=utf-8
"""Pesquisar Santander feature tests."""

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from features.Pages.searchPage import Search, Result
from features.Pages.utilPage import Util
import coverage 
import yaml
from pathlib import Path
 

# Scenarios 
scenarios(Path('../search.feature')) 

# Carrega a classe util
util = Util() 
    
#open YAML file
yaml = util.yaml_loader(Path('features/fixtures/data.yml')) 

#Inicia o driver antes de começar o teste
@pytest.fixture
def driver(): 
    driver = webdriver.Chrome(executable_path = "C:/Users/Administrator/Anaconda3/selenium/webdriver/drivers/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(10)        
    yield driver
    driver.quit()

    
@given('I am in Google website')
def i_am_in_google_website(driver):    
    driver.get(yaml.get("set_url"))

@when('I search for Santander')
def i_search_for_santander(driver):
    search = Search(driver)
    search.search_content("Santander")


@when('access the first result')
def access_the_first_result(driver):
    result = Result(driver)
    result.click_highlight_result() 


@then('I enter Santanders website')
def i_enter_santanders_website(driver):      
    util.validate_text(driver, yaml.get("text_validation"))
    util.screenshot(driver, "Santander")