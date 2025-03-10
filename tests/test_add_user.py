import time
import unittest

from selenium import webdriver

from pages.admin_page import AdminPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.excel_utils import read_excel


class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        self.admin_page = AdminPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    def test_add_user(self):
        # Step 1: Login
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()

        # Step 2: Click on Admin menu
        self.admin_page.click_admin_menu()

        # Step 3: Click on Add button
        self.admin_page.click_add_button()

        # Step 4: Fill in user details from Excel
        user_data = read_excel("user_data.xlsx", "Sheet1")[0]
        username, password, employee_name, user_role, status = user_data

        # Step 5: Fill the form
        self.admin_page.select_user_role(user_role)
        self.admin_page.enter_employee_name(employee_name.split(" ")[0])
        self.admin_page.select_status(status)
        self.admin_page.enter_username(username)
        self.admin_page.enter_password(password)
        self.admin_page.enter_confirm_password(password)

        # Step 6: Click on Save button
        self.admin_page.click_save_button()

        time.sleep(2)

        # Step 7: Search and validate the added user
        self.admin_page.search_user(username)
        self.admin_page.validate_user_search()

        # Step 8: Logout
        self.dashboard_page.click_logout()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
