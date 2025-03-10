from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu = (By.XPATH, '//span[@class="oxd-userdropdown-tab"]')
        self.logout_link = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]//a[text()="Logout"]')

    def click_logout(self):
        self.driver.find_element(*self.menu).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
