from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login")

        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "submit")

        username.send_keys("student")
        password.send_keys("Password123")
        submit_button.click()

    def test_exceptions_page(self):
        self.driver.get("https://practicetestautomation.com/practice-test-exceptions")

        # Test Case 1: Add Button
        try:
            add_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add_btn")))
            add_button.click()

            row_2 = self.wait.until(EC.visibility_of_element_located((By.ID, "row2")))
            print("✅ Test Case 1 (Add Button): Passed")
        except TimeoutException:
            print("❌ Test Case 1 (Add Button): Failed - Element not found")
            return

        # Test Case 2: Enter text in the new row input
        try:
            text_field = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#row2 input"))
            )
            text_field.clear()
            text_field.send_keys("New Text")
            print("✅ Test Case 2 (Input Field): Passed")
        except TimeoutException:
            print("❌ Test Case 2 (Input Field): Failed - Element not found")
            return

        # Test Case 3: Click Save button in row 2
        try:
            # Save button under row2
            save_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#row2 #save_btn"))
            )
            save_button.click()
            print("✅ Save button clicked!")

            confirmation = self.wait.until(
                EC.visibility_of_element_located((By.ID, "confirmation"))
            )
            assert "Row 2 was saved" in confirmation.text
            print("✅ Test Case 3 (Save Button): Passed")

        except Exception as e:
            print(f"❌ Test Case 3 (Save Button): Failed with error: {e}")

if __name__ == "__main__":
    test = TestAutomation()
    try:
        test.login()
        test.test_exceptions_page()
    finally:
        print("برنامه تا 10 ثانیه دیگر متوقف می‌شود و مرورگر بسته خواهد شد...")
        time.sleep(10)
        test.driver.quit()
