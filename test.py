from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module='urllib3')

class TravelWebsiteTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_image_existence(self):
        # Test existence of an image
        self.driver.get("http://127.0.0.1:8000")  # Replace with your website URL

        # Parallax images presence tests
        image = self.driver.find_element(By.CSS_SELECTOR, 'div.parallax-one')
        self.assertTrue(image.is_displayed())
        image = self.driver.find_element(By.CSS_SELECTOR, 'div.parallax-two')
        self.assertTrue(image.is_displayed())
        image = self.driver.find_element(By.CSS_SELECTOR, 'div.parallax-three')
        self.assertTrue(image.is_displayed())

        # Carousel images 
        element = self.driver.find_element_by_class_name("owl-stage")
        self.assertTrue(element.is_displayed(), "Element is not displayed")

        # Slider presence
        element = self.driver.find_element_by_class_name("owl-dots")
        self.assertTrue(element.is_displayed(), "Element is not displayed")

        # Button presence
        button = self.driver.find_element(By.XPATH, "//a[text()='See Destinations']")
        assert button.is_displayed(), "Button is not visible on the page"

        # Form presence
        form = self.driver.find_element(By.ID, "destinations-form")
        assert form.is_displayed(), "Form is not visible on the page"

    def test_location(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)
        
        parallax_one_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-one").location['y']
        parallax_two_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-two").location['y']
        parallax_three_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-three").location['y']
        
        # Positions of parallax images
        assert parallax_one_top < parallax_two_top, "Parallax two is not correctly located below one"
        assert parallax_two_top < parallax_three_top, "Parallax three is not correctly located below two"

        # Position of Sliders and see destinations button
        slider_top = self.driver.find_element(By.CLASS_NAME, "owl-stage").location['y']
        button_top = self.driver.find_element(By.XPATH, "//a[text()='See Destinations']").location['y']

        assert parallax_two_top < slider_top, "Parallax two is not above the slider"
        assert slider_top < button_top, "Slider is not above the button"
        assert button_top < parallax_three_top, "Button is not above parallax three"

        # Form position
        form_top = self.driver.find_element(By.ID, "destinations-form").location['y']
        assert form_top > parallax_three_top, "Form is not below parallax three"

    def test_size(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)
        
        # Get the width of the parallax element
        parallax_width = self.driver.find_element(By.CLASS_NAME, "parallax-two").size['width']
        assert parallax_width > 100, "Parallax width is not as expected"
        parallax_width = self.driver.find_element(By.CLASS_NAME, "parallax-one").size['width']
        assert parallax_width > 100, "Parallax width is not as expected"
        parallax_width = self.driver.find_element(By.CLASS_NAME, "parallax-three").size['width']
        assert parallax_width > 100, "Parallax width is not as expected"

        parallax_size = self.driver.find_element(By.CLASS_NAME, "parallax-two").size
        owl_stage_size = self.driver.find_element(By.CLASS_NAME, "owl-stage").size
        form_size = self.driver.find_element(By.ID, "destinations-form").size
        
        # Check if the size of the owl-stage is less than the size of the parallax
        assert owl_stage_size['width'] > parallax_size['width'], "Width of owl-stage is less than parallax"
        assert owl_stage_size['height'] < parallax_size['height'], "Height of owl-stage is not less than parallax"
        
        # Check if the size of the form is less than the size of the parallax
        assert form_size['width'] < parallax_size['width'], "Width of form is not less than parallax"
        assert form_size['height'] < parallax_size['height'], "Height of form is not less than parallax"

    def test_content(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)

        # Parallax contents
        script = """
            return document.querySelector('.parallax-one').textContent.trim();
        """
        parallax_one_text = self.driver.execute_script(script)
        assert "ODYSSEY OUTBOUND" in parallax_one_text, "Parallax One text is incorrect"
        
        script = """
            return document.querySelector('.parallax-two').textContent.trim();
        """
        parallax_one_text = self.driver.execute_script(script)
        assert "EXPLORE PACKAGES" in parallax_one_text, "Parallax One text is incorrect"

        script = """
            return document.querySelector('.parallax-three').textContent.trim();
        """
        parallax_one_text = self.driver.execute_script(script)
        assert "EXPLORE OUR DESTINATIONS" in parallax_one_text, "Parallax One text is incorrect"

        # Card content
        script = """
            var owlStage = document.querySelector('.owl-stage');
            return owlStage.textContent.trim();
        """
        owl_stage_content = self.driver.execute_script(script)
        
        # Assert that the text "Japan" is present in the content of owl-stage
        assert "Japan" in owl_stage_content, "Text 'Japan' not found in owl-stage content"
    
    
    def test_function(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)
        
        # See Destinations Button navigates to Form
        ok3=self.driver.find_element_by_css_selector('#navigateToForm')
        self.driver.execute_script("arguments[0].click();",ok3)
        assert "destinations-form" in self.driver.current_url

        driver = self.driver
        # Form can be submitted without email and agreeing to terms and conditions
        # Find form fields by name
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
        self.driver.execute_script("arguments[0].click();",submit_button)
        # Wait for the form submission to be processed
        WebDriverWait(driver, 10).until(EC.url_contains('/destinations'))
        # If the redirect URL contains the expected URL
        assert '/destinations' in driver.current_url
        # self.driver.close()

        # Form cannot be submitted without email and agreeing to terms and conditions
        # Find form fields by name
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
        submit_button = self.driver.find_element_by_css_selector('#form-submit')
        self.driver.execute_script("arguments[0].click();",submit_button)
        sleep(3)
        assert '/destinations' not in driver.current_url
            
    def tearDown(self):
        sleep(1)  # Optional delay for better visualization
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
