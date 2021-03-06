import unittest
import time
from selenium import webdriver


class TestSelectSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_check_one_checkbutton(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

        time.sleep(3)
        options_list = [
            "//input[@id='isAgeSelected']",
              ]
        for s in options_list:
            check_button = driver.find_element_by_xpath(s)
            check_button.click()
            time.sleep(3)
        resultado = driver.find_element_by_xpath("//div[@id='txtAge']")
        self.assertEqual(resultado.text, "Success - Check box is checked")



    def test_suma_dos_numeros(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        text_input_1 = driver.find_element_by_xpath("//input[@id='user-message']")
        total_button = driver.find_element_by_xpath("//button[contains(text(),'Show Message')]")
        text_output = driver.find_element_by_xpath("//span[@id='display']")

        text_input_1.send_keys('Angel Paredes Puma')
        total_button.click()
        self.assertEqual('Angel Paredes Puma', text_output.text)

    def test_check_radio_button(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

        radio_button_male = driver.find_element_by_xpath(
            "//body/div[@id='easycont']/div[1]/div[2]/div[1]/div[2]/label[1]/input[1]"
        )

        get_values_button = driver.find_element_by_xpath(
            "//button[@id='buttoncheck']"
        )
        text_output = driver.find_element_by_css_selector(
            "div.container-fluid.text-center:nth-child(2) div.row div.col-md-6.text-left:nth-child(2) div.panel.panel-default:nth-child(4) div.panel-body > p.radiobutton:nth-child(7)"
        )

        radio_button_male.click()
        time.sleep(2)
        get_values_button.click()
        time.sleep(2)
        self.assertRegex(text_output.text, "Male")
        time.sleep(2)