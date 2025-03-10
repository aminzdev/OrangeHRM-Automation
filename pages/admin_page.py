import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.add_button = (By.XPATH, '//button[text()=" Add "]')
        self.save_button = (By.XPATH, '//button[text()=" Save "]')
        self.search_button = (By.XPATH, '//button[text()=" Search "]')
        self.search_input = (
            By.XPATH,
            '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        )
        self.user_role_dropdown = (
            By.XPATH,
            '//label[text()="User Role"]'
            '/ancestor::div[contains(@class, "oxd-input-group")]'
            '//div[contains(@class, "oxd-select-text")]'
        )
        self.employee_name_input = (
            By.XPATH,
            '//label[text()="Employee Name"]'
            '/ancestor::div[contains(@class, "oxd-input-group")]'
            '//input'
        )
        self.status_dropdown = (
            By.XPATH,
            '//label[text()="Status"]'
            '/ancestor::div[contains(@class, "oxd-input-group")]'
            '//div[contains(@class, "oxd-select-text")]'
        )
        self.username_input = (
            By.XPATH,
            '//label[text()="Username"]'
            '/ancestor::div[contains(@class, "oxd-input-group")]'
            '//input'
        )
        self.password_input = (
            By.XPATH,
            '//label[text()="Password"]'
            '/ancestor::div[contains(@class, "oxd-input-group")]'
            '//input[@type="password"]'
        )
        self.confirm_password_input = (
            By.XPATH,
            '//label[text()="Confirm Password"]'
            '/ancestor::div[contains(@class, "oxd-input-group")]'
            '//input[@type="password"]'
        )
        self.record_found_message = (
            By.XPATH, '//span[text()="(1) Record Found"]'
        )

    def click_admin_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_menu)
        ).click()

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def click_save_button(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
        save_button.click()

    def search_user(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_input)
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def select_user_role(self, role):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.user_role_dropdown)
        ).click()
        role_option = (By.XPATH, f'//div[@role="option"]/span[text()="{role}"]')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(role_option)
        ).click()

    def enter_employee_name(self, name):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_name_input)
        )
        input_field.click()
        time.sleep(1)

        for char in name:
            input_field.send_keys(char)
            time.sleep(0.2)

        time.sleep(2)

        input_field.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)

        input_field.send_keys(Keys.ENTER)

    def select_status(self, status):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.status_dropdown)
        ).click()
        status_option = (By.XPATH, f'//div[@role="option"]/span[text()="{status}"]')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(status_option)
        ).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        ).send_keys(password)

    def enter_confirm_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_password_input)
        ).send_keys(password)

    def validate_user_search(self):
        message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.record_found_message)
        )

        message_text = message_element.text
        if message_text == "(1) Record Found":
            print("Validation Passed: 1 record found.")
        else:
            print(f"Validation Failed: Expected '(1) Record Found', but got '{message_text}'.")
