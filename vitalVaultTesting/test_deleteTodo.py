# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDeleteTodo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deleteTodo(self):
    self.driver.get("https://vitalvault.vercel.app/")
    self.driver.set_window_size(1292, 1396)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("testing")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Completed").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item.list-group-item-action.list-group-item-danger").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, " .btn.btn-primary")
    assert len(elements) > 0
  
