from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

#     def test_presence(self):
#         japan_radio_button = self.driver.find_element_by_id("radioJapan")
#         assert japan_radio_button is not None, "Japan radio button does not exist"

#         # img presence
#         image_element = self.driver.find_element(By.CLASS_NAME, "destination-image")
#         assert image_element is not None, "Image does not display"

#         # slider buttons
#         prev = self.driver.find_element(By.CLASS_NAME, "previous")
#         next = self.driver.find_element(By.CLASS_NAME, "next")
#         assert prev is not None, "Slider not present"
#         assert next is not None, "Slider not present"

#         # # packagesButton
#         packagesButton = self.driver.find_element(By.ID, "packagesButton")
#         assert packagesButton is not None, "Button does not exists."

#     def test_location(self):
#         radio_buttons = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
#         image = self.driver.find_element(By.CLASS_NAME, "destination-image")

#         # Get the location of the radio buttons and the image
#         radio_buttons_location = radio_buttons[0].location
#         image_location = image.location

#         # Assert that the radio buttons are above the image
#         assert radio_buttons_location['y'] < image_location['y'], "Radio buttons are not above the image."

#         image = self.driver.find_element(By.CLASS_NAME, "destination-image")
#         slider = self.driver.find_element(By.CLASS_NAME, "next")

#         # Get the location of the image and the slider
#         image_location = image.location
#         slider_location = slider.location

#         # Assert that the slider is below the image
#         self.assertGreater(slider_location['y'], image_location['y'], "Slider is not below the image.")

#         slider = self.driver.find_element(By.CLASS_NAME, "next")
#         packagesButton = self.driver.find_element(By.ID, "packagesButton")

#         # Get the location of the image and the slider
#         slider_location = slider.location
#         packagesButton_location = packagesButton.location

#         # Assert that the slider is below the image
#         self.assertGreater( packagesButton_location['y'],slider_location['y'], "Slider is not above the button.")


    
#     def test_size(self):
#         element = self.driver.find_element(By.ID, "japan")

#         # Get the location of the element
#         element_location = element.location

#         # Get the viewport height
#         viewport_height = self.driver.execute_script("return window.innerHeight")

#         # Calculate 80% of the viewport height
#         eighty_percent_height = viewport_height * 0.8

#         # Assert that the element is above 80% of the screen size
#         self.assertLess(element_location['y'], eighty_percent_height, "Element is not above 80% of the screen size.")

#     def test_content(self):
#         sleep(5)
#         h1_element = self.driver.find_element_by_xpath("//h1[@class='title']/span[@class='underline']")
#         text = h1_element.text
#         assert "Explore" in text
    
#     def test_functionality(self):
#         radio_buttons = self.driver.find_elements_by_css_selector('input[name="flexRadioDefault"]')

#         # Iterate through each radio button
#         for radio_button in radio_buttons:
#             # Click on the radio button
#             radio_button.click()
#             # Wait for a brief moment for the JavaScript to execute and the country description to appear
#             sleep(3)
#             # Check if the selected country description is visible while others are hidden
#             country_descriptions = self.driver.find_elements_by_css_selector('.country-description')
#             for description in country_descriptions:
#                 if radio_button.get_attribute('value').lower() in description.get_attribute('id'):
#                     assert 'd-none' not in description.get_attribute('class'), f"{radio_button.get_attribute('value')} description is not visible"
#                 else:
#                     assert 'd-none' in description.get_attribute('class'), f"{description.get_attribute('id')} description is visible while it should be hidden"

#         # Button press
#         see_packages_button = self.driver.find_element_by_css_selector('#see-packages-btn')
#         self.driver.execute_script("arguments[0].click();",see_packages_button)
#         # Wait for the form submission to be processed
#         WebDriverWait(self.driver, 10).until(EC.url_contains('/packages'))
#         assert "/packages" in self.driver.current_url, "Redirection failed"

    
#     def tearDown(self):
#         sleep(1)  # Optional delay for better visualization
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()


class TravelWebsiteTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8000/destinations")
        self.driver.set_window_size(1440, 814)
        WebDriverWait(self.driver, 10).until(EC.url_contains('/destinations'))

    def test_japan_radio_button_existence(self):
        japan_radio_button = self.driver.find_element_by_id("radioJapan")
        self.assertIsNotNone(japan_radio_button, "Japan radio button does not exist")

    def test_image_presence(self):
        image_element = self.driver.find_element(By.CLASS_NAME, "destination-image")
        self.assertIsNotNone(image_element, "Image does not display")

    def test_slider_buttons_presence(self):
        prev = self.driver.find_element(By.CLASS_NAME, "previous")
        next = self.driver.find_element(By.CLASS_NAME, "next")
        self.assertIsNotNone(prev, "Slider not present")
        self.assertIsNotNone(next, "Slider not present")

    def test_packages_button_existence(self):
        packagesButton = self.driver.find_element(By.ID, "packagesButton")
        self.assertIsNotNone(packagesButton, "Button does not exists.")

    def test_radio_buttons_location(self):
        radio_buttons = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
        image = self.driver.find_element(By.CLASS_NAME, "destination-image")
        radio_buttons_location = radio_buttons[0].location
        image_location = image.location
        self.assertLess(radio_buttons_location['y'], image_location['y'], "Radio buttons are not above the image.")

    def test_slider_below_image(self):
        image = self.driver.find_element(By.CLASS_NAME, "destination-image")
        slider = self.driver.find_element(By.CLASS_NAME, "next")
        image_location = image.location
        slider_location = slider.location
        self.assertGreater(slider_location['y'], image_location['y'], "Slider is not below the image.")

    def test_button_above_slider(self):
        slider = self.driver.find_element(By.CLASS_NAME, "next")
        packagesButton = self.driver.find_element(By.ID, "packagesButton")
        slider_location = slider.location
        packagesButton_location = packagesButton.location
        self.assertGreater(packagesButton_location['y'], slider_location['y'], "Slider is not above the button.")

    def test_element_size(self):
        element = self.driver.find_element(By.ID, "japan")
        element_location = element.location
        viewport_height = self.driver.execute_script("return window.innerHeight")
        eighty_percent_height = viewport_height * 0.8
        self.assertLess(element_location['y'], eighty_percent_height, "Element is not above 80% of the screen size.")

    def test_content(self):
        sleep(5)
        h1_element = self.driver.find_element_by_xpath("//h1[@class='title']/span[@class='underline']")
        text = h1_element.text
        self.assertIn("Explore", text)

    def test_radio_buttons_functionality(self):
        radio_buttons = self.driver.find_elements_by_css_selector('input[name="flexRadioDefault"]')
        for radio_button in radio_buttons:
            radio_button.click()
            sleep(3)
            country_descriptions = self.driver.find_elements_by_css_selector('.country-description')
            for description in country_descriptions:
                if radio_button.get_attribute('value').lower() in description.get_attribute('id'):
                    self.assertNotIn('d-none', description.get_attribute('class'), f"{radio_button.get_attribute('value')} description is not visible")
                else:
                    self.assertIn('d-none', description.get_attribute('class'), f"{description.get_attribute('id')} description is visible while it should be hidden")

    def test_see_packages_button_functionality(self):
        see_packages_button = self.driver.find_element_by_css_selector('#packagesButton')
        self.driver.execute_script("arguments[0].click();",see_packages_button)
        WebDriverWait(self.driver, 10).until(EC.url_contains('/packages'))
        self.assertIn("/packages", self.driver.current_url, "Redirection failed")

    def tearDown(self):
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
