from flask import request
from flask.ext.restful import Resource

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebScraperAPI(Resource):
    def post(self):
        url = request.json.get('url')
        driver = webdriver.PhantomJS()
        driver.wait = WebDriverWait(driver, 5)
        driver.get(url)
        return {'name': driver.find_element_by_id('name').text,
                'summary': driver.find_element_by_class_name('description').text,
                'job_title': driver.find_element_by_class_name('headline').text,
                'location': driver.find_element_by_class_name('locality').text,
                'photo': driver.find_element_by_class_name('image').get_attribute('src')
        }
        time.sleep(5)
        driver.quit()

# "//img[contains(@src)]/parent::a"

# login_form = driver.find_element_by_xpath("/html/body/form[1]")

# driver.find_element_by_css_selector()