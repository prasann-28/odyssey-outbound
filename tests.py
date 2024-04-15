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

    def test_parallax_images_existence(self):
        # Test existence of parallax images
        self.driver.get("http://127.0.0.1:8000")  # Replace with your website URL

        # Parallax images presence tests
        image = self.driver.find_element(By.CSS_SELECTOR, 'div.parallax-one')
        self.assertTrue(image.is_displayed())
        print("Image one is displayed")

        image = self.driver.find_element(By.CSS_SELECTOR, 'div.parallax-two')
        self.assertTrue(image.is_displayed())
        print("Image two is displayed")

        image = self.driver.find_element(By.CSS_SELECTOR, 'div.parallax-three')
        self.assertTrue(image.is_displayed())
        print("Image three is displayed")

    def test_carousel_presence(self):
        # Test presence of carousel images and slider
        self.driver.get("http://127.0.0.1:8000/")
        element = self.driver.find_element_by_class_name("owl-stage")
        self.assertTrue(element.is_displayed(), "Element is not displayed")
        print("Carousel images are displayed")

        element = self.driver.find_element_by_class_name("owl-dots")
        self.assertTrue(element.is_displayed(), "Element is not displayed")
        print("Slider is displayed")

    def test_button_presence(self):
        # Test presence of button
        self.driver.get("http://127.0.0.1:8000/")
        button = self.driver.find_element(By.XPATH, "//a[text()='See Destinations']")
        self.assertTrue(button.is_displayed(), "Button is not visible on the page")
        print("Button is displayed")

    def test_form_presence(self):
        # Test presence of form
        self.driver.get("http://127.0.0.1:8000/")
        form = self.driver.find_element(By.ID, "destinations-form")
        self.assertTrue(form.is_displayed(), "Form is not visible on the page")
        print("Form is displayed")

    def test_parallax_image_positions(self):
        # Test positions of parallax images
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)

        parallax_one_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-one").location['y']
        parallax_two_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-two").location['y']
        parallax_three_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-three").location['y']

        assert parallax_one_top < parallax_two_top, "Parallax two is not correctly located below one"
        assert parallax_two_top < parallax_three_top, "Parallax three is not correctly located below two"
        print("Parallax images are correctly located")

    def test_slider_button_positions(self):
        # Test positions of slider, button, and parallax images
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)

        parallax_two_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-two").location['y']
        slider_top = self.driver.find_element(By.CLASS_NAME, "owl-stage").location['y']
        button_top = self.driver.find_element(By.XPATH, "//a[text()='See Destinations']").location['y']
        parallax_three_top = self.driver.find_element(By.CSS_SELECTOR, ".parallax-three").location['y']

        assert parallax_two_top < slider_top, "Parallax two is not above the slider"
        assert slider_top < button_top, "Slider is not above the button"
        assert button_top < parallax_three_top, "Button is not above parallax three"
        print("Slider, button, and parallax images are correctly positioned")

    def test_element_sizes(self):
        # Test sizes of elements
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)

        parallax_width = self.driver.find_element(By.CLASS_NAME, "parallax-two").size['width']
        assert parallax_width > 100, "Parallax width is not as expected"
        parallax_width = self.driver.find_element(By.CLASS_NAME, "parallax-one").size['width']
        assert parallax_width > 100, "Parallax width is not as expected"
        parallax_width = self.driver.find_element(By.CLASS_NAME, "parallax-three").size['width']
        assert parallax_width > 100, "Parallax width is not as expected"

        parallax_size = self.driver.find_element(By.CLASS_NAME, "parallax-two").size
        owl_stage_size = self.driver.find_element(By.CLASS_NAME, "owl-stage").size
        form_size = self.driver.find_element(By.ID, "destinations-form").size

        assert owl_stage_size['width'] > parallax_size['width'], "Width of owl-stage is less than parallax"
        assert owl_stage_size['height'] < parallax_size['height'], "Height of owl-stage is not less than parallax"
        assert form_size['width'] < parallax_size['width'], "Width of form is not less than parallax"
        assert form_size['height'] < parallax_size['height'], "Height of form is not less than parallax"
        print("Sizes are as expected")

    def test_content(self):
        # Test content of elements
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)

        script = """
            return document.querySelector('.parallax-one').textContent.trim();
        """
        parallax_one_text = self.driver.execute_script(script)
        assert "ODYSSEY OUTBOUND" in parallax_one_text, "Parallax One text is incorrect"

        script = """
            return document.querySelector('.parallax-two').textContent.trim();
        """
        parallax_two_text = self.driver.execute_script(script)
        assert "EXPLORE PACKAGES" in parallax_two_text, "Parallax Two text is incorrect"

        script = """
            return document.querySelector('.parallax-three').textContent.trim();
        """
        parallax_three_text = self.driver.execute_script(script)
        assert "EXPLORE OUR DESTINATIONS" in parallax_three_text, "Parallax Three text is incorrect"

        script = """
            var owlStage = document.querySelector('.owl-stage');
            return owlStage.textContent.trim();
        """
        owl_stage_content = self.driver.execute_script(script)

        assert "Japan" in owl_stage_content, "Text 'Japan' not found in owl-stage content"
        print("Contents are as expected")

    def test_form_submission(self):
        # Test form submission functionality
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1440, 814)

        # See Destinations Button navigates to Form
        ok3=self.driver.find_element_by_css_selector('#navigateToForm')
        self.driver.execute_script("arguments[0].click();",ok3)
        assert "destinations-form" in self.driver.current_url
        print("Navigated to form successfully")

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
        prevlen = len(driver.current_url)
        print(prevlen)
        terms_checkbox.click()
        submit_button = self.driver.find_element_by_css_selector('#form-submit')
        self.driver.execute_script("arguments[0].click();",submit_button)
        # Wait for the form submission to be processed
        sleep(3)
        # If the redirect URL contains the expected URL
        print(driver.current_url)
        assert prevlen < len(driver.current_url), "Navigation unsuccessfull"
        print("Form submitted successfully")

        # Form cannot be submitted without email and agreeing to terms and conditions
        # Find form fields by name
    def test_unsuccessful_submission(self):
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
        assert '/destinations' not in self.driver.current_url
        print("Form submission without required fields blocked")

    def tearDown(self):
        sleep(1)  # Optional delay for better visualization
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
