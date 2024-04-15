
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import warnings

# class TravelWebsiteTests(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("http://127.0.0.1:8000/")
#         self.driver.set_window_size(1440, 814)
#         form = self.driver.find_element_by_id("destinations-form")
#         first_name_field = form.find_element_by_name("firstname")
#         last_name_field = form.find_element_by_name("lastname")
#         email_field = form.find_element_by_name("email")
#         phone_field = form.find_element_by_name("phone")
#         category_field = form.find_element_by_name("querycategory")
#         message_field = form.find_element_by_name("queryaddn")
#         newsletter_checkbox = form.find_element_by_name("newsletter")
#         first_name_field.send_keys("John")
#         last_name_field.send_keys("Doe")
#         email_field.send_keys("example@example.com")
#         phone_field.send_keys("1234567890")
#         category_field.send_keys("Regarding Destinations")
#         message_field.send_keys("This is a test message")
#         newsletter_checkbox.click()
#         terms_checkbox = self.driver.find_element_by_css_selector("#defaultCheck2")
#         terms_checkbox.location_once_scrolled_into_view
#         sleep(1)
#         terms_checkbox.click()
#         submit_button = self.driver.find_element_by_css_selector('#form-submit')
#         self.driver.execute_script("arguments[0].click();",submit_button)
#         # Wait for the form submission to be processed
#         WebDriverWait(self.driver, 10).until(EC.url_contains('/destinations'))
#         see_packages_button = self.driver.find_element_by_css_selector('#packagesButton')
#         self.driver.execute_script("arguments[0].click();",see_packages_button)
#         # Wait for the form submission to be processed
#         WebDriverWait(self.driver, 10).until(EC.url_contains('/packages'))

#     def test_existence(self):
#         # Cards
#         card = self.driver.find_elements_by_css_selector('.card')
#         assert card is not None, "card is not present on the page"
#         card_img = self.driver.find_elements_by_css_selector('.card-img-top')
#         assert card_img is not None, "card_img is not present on the page"
#         card_body = self.driver.find_elements_by_css_selector('.card-body')
#         assert card_body is not None, "card_body is not present on the page"
#         card_text = self.driver.find_elements_by_css_selector('.card-text')
#         assert card_text is not None, "card_text is not present on the page"

#         # rangeValueLabel
#         slider = self.driver.find_elements_by_css_selector('#customRange1')
#         assert slider is not None, "slider is not present on the page"

#         # packageSelect
#         selectRange = self.driver.find_elements_by_css_selector('#packageSelect')
#         assert selectRange is not None, "selectRange is not present on the page"

#     def test_location(self):
#         cards = self.driver.find_elements_by_css_selector('.card')
#         slider = self.driver.find_element_by_css_selector('#customRange1')
#         button = self.driver.find_element_by_css_selector('.btn')

#         # Get the locations of the elements
#         cards_location = cards[0].location
#         slider_location = slider.location
#         button_location = button.location

#         # Assert that cards are above slider
#         assert cards_location['y'] < slider_location['y'], "Cards are not above the slider"

#         # Assert that button is below slider
#         assert button_location['y'] > slider_location['y'], "Button is not below the slider"
        
#     def test_size(self):
#         image = self.driver.find_element_by_css_selector('.card-img-top')

#         # Get the size of the image
#         image_size = image.size

#         # Assert that both width and height are greater than zero
#         assert image_size['width'] > 0 and image_size['height'] > 0, "Image size is zero"

#     def test_content(self):
#         ul_element = self.driver.find_element_by_css_selector('.list-group')

#         # Get all child elements of the ul
#         child_elements = ul_element.find_elements_by_css_selector('*')

#         # Assert that the ul has at least one child element
#         assert len(child_elements) > 0, "The ul element is empty"
    
#     def test_functionality(self):
#         # button = self.driver.find_element_by_css_selector(".btn")
#         # button.click()
#         submit_button = self.driver.find_element_by_css_selector('.btn')
#         self.driver.execute_script("arguments[0].click();",submit_button)

#         # Wait for the alert to appear
#         sleep(2)  # Adjust the sleep time as needed

#         # Switch to the alert
#         alert = self.driver.switch_to.alert

#         # Get the text of the alert
#         alert_text = alert.text

#         # Print or use the alert text as needed
#         print("Alert Text:", alert_text)

#         # Dismiss the alert (clicking the OK button)
#         alert.accept()  # or alert.dismiss() if you want to dismiss it
#         # Cost for selected package is: $4300
#         assert "Cost for selected package is: $4300" == alert_text, "The ul element is empty"




#     def tearDown(self):
#         sleep(1)  # Optional delay for better visualization
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TravelWebsiteTests(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning, module='urllib3')
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)
        form = self.driver.find_element_by_id("destinations-form")
        first_name_field = form.find_element_by_name("firstname")
        last_name_field = form.find_element_by_name("lastname")
        email_field = form.find_element_by_name("email")
        phone_field = form.find_element_by_name("phone")
        category_field = form.find_element_by_name("querycategory")
        message_field = form.find_element_by_name("queryaddn")
        newsletter_checkbox = form.find_element_by_name("newsletter")
        first_name_field.send_keys("John")
        last_name_field.send_keys("Doe")
        email_field.send_keys("example@example.com")
        phone_field.send_keys("1234567890")
        category_field.send_keys("Regarding Destinations")
        message_field.send_keys("This is a test message")
        newsletter_checkbox.click()
        terms_checkbox = self.driver.find_element_by_css_selector("#defaultCheck2")
        terms_checkbox.location_once_scrolled_into_view
        sleep(1)
        terms_checkbox.click()
        submit_button = self.driver.find_element_by_css_selector('#form-submit')
        self.driver.execute_script("arguments[0].click();", submit_button)
        # Wait for the form submission to be processed
        WebDriverWait(self.driver, 10).until(EC.url_contains('/destinations'))
        see_packages_button = self.driver.find_element_by_css_selector('#packagesButton')
        self.driver.execute_script("arguments[0].click();", see_packages_button)
        # Wait for the form submission to be processed
        WebDriverWait(self.driver, 10).until(EC.url_contains('/packages'))

    def test_card_existence(self):
        card = self.driver.find_elements_by_css_selector('.card')
        assert card is not None, "card is not present on the page"

    def test_card_img_existence(self):
        card_img = self.driver.find_elements_by_css_selector('.card-img-top')
        assert card_img is not None, "card_img is not present on the page"

    def test_card_body_existence(self):
        card_body = self.driver.find_elements_by_css_selector('.card-body')
        assert card_body is not None, "card_body is not present on the page"

    def test_card_text_existence(self):
        card_text = self.driver.find_elements_by_css_selector('.card-text')
        assert card_text is not None, "card_text is not present on the page"

    def test_slider_existence(self):
        slider = self.driver.find_elements_by_css_selector('#customRange1')
        assert slider is not None, "slider is not present on the page"

    def test_package_select_existence(self):
        selectRange = self.driver.find_elements_by_css_selector('#packageSelect')
        assert selectRange is not None, "selectRange is not present on the page"

    def test_card_location(self):
        cards = self.driver.find_elements_by_css_selector('.card')
        slider = self.driver.find_element_by_css_selector('#customRange1')
        button = self.driver.find_element_by_css_selector('.btn')
        cards_location = cards[0].location
        slider_location = slider.location
        button_location = button.location
        assert cards_location['y'] < slider_location['y'], "Cards are not above the slider"
        assert button_location['y'] > slider_location['y'], "Button is not below the slider"

    def test_image_size(self):
        image = self.driver.find_element_by_css_selector('.card-img-top')
        image_size = image.size
        assert image_size['width'] > 0 and image_size['height'] > 0, "Image size is zero"

    def test_ul_element_content(self):
        ul_element = self.driver.find_element_by_css_selector('.list-group')
        child_elements = ul_element.find_elements_by_css_selector('*')
        assert len(child_elements) > 0, "The ul element is empty"

    def test_alert_content(self):
        submit_button = self.driver.find_element_by_css_selector('.btn')
        self.driver.execute_script("arguments[0].click();", submit_button)
        sleep(2)  # Adjust the sleep time as needed
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "Cost for selected package is: $4300" == alert_text, "The alert content is not as expected"

    def tearDown(self):
        sleep(1)  # Optional delay for better visualization
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
