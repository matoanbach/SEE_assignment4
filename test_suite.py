import time
import unittest
from datetime import datetime
import logging
from logging.handlers import MemoryHandler
import colorlog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ANSI escape codes for extra coloring.
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

# Configure the console handler with colorlog.
console_handler = colorlog.StreamHandler()
console_handler.setFormatter(colorlog.ColoredFormatter(
    fmt="%(log_color)s%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        'DEBUG':    'blue',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    }
))
# Set the console handler to only show INFO and above.
console_handler.setLevel(logging.INFO)

# Create a memory handler to capture DEBUG messages.
mem_handler = MemoryHandler(capacity=10000, flushLevel=logging.ERROR, target=console_handler)
mem_handler.setLevel(logging.DEBUG)

# Configure the root logger.
logger = colorlog.getLogger()
logger.setLevel(logging.DEBUG)  # Capture all logs
logger.addHandler(console_handler)
logger.addHandler(mem_handler)

# URL for the Real Estate Predictor webpage.
BASE_URL = "https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor.html"

def log_test_case(test_id, description, tester="John Doe", environment="QA Environment, Chrome v123"):
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info("=================================")
    logger.info(f"{MAGENTA}Test Case ID: {test_id}{RESET}")
    logger.info(f"Description: {description}")
    logger.info(f"Date & Time: {dt}")
    logger.info(f"Tested By: {tester}")
    logger.info(f"Environment: {environment}")
    logger.info("Steps: See test script for detailed steps.")
    logger.info("Expected Result: As described in test case documentation.")

def log_test_case_end(test_id, status="Pass", notes="N/A"):
    if status == "Fail":
        logger.error(f"{RED}Status: {status}{RESET}")
        logger.error(f"{RED}Notes: {notes}{RESET}")
        logger.error("Screenshot: (Attach screenshot if applicable)")
        logger.error("Log File: (Refer to log output)")
        logger.error("Issue: N/A")
        logger.error("Resolution: N/A")
    else:
        logger.info(f"{GREEN}Status: {status}{RESET}")
        logger.info(f"{GREEN}Notes: {notes}{RESET}")
        logger.info("Screenshot: (Attach screenshot if applicable)")
        logger.info("Log File: (Refer to log output)")
        logger.info("Issue: N/A")
        logger.info("Resolution: N/A")
    logger.info("=================================")
    if status == "Fail":
        logger.error(f"{RED}[{test_id}] - END test{RESET}")
    else:
        logger.info(f"{BLUE}[{test_id}] - END test{RESET}")
    logger.info("")

class RealEstatePredictorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("=================================")
        logger.info("[RE-01] Setting up WebDriver for test suite...")
        cls.driver = webdriver.Chrome()  # Change to webdriver.Firefox() if preferred.
        cls.driver.maximize_window()
        logger.info("[RE-01] WebDriver setup completed.")
        logger.info("=================================")

    @classmethod
    def tearDownClass(cls):
        logger.info("Closing WebDriver...")
        cls.driver.quit()
        logger.info("WebDriver closed.")

    def tearDown(self):
        # Check if test failed; if so, temporarily output DEBUG logs.
        failed = False
        outcome = self._outcome
        for test, exc in outcome.errors:
            if exc:
                failed = True
        for test, exc in outcome.failures:
            if exc:
                failed = True
        if failed:
            logger.info(f"{RED}Test failed; dumping DEBUG logs from memory handler...{RESET}")
            # Temporarily set console handler level to DEBUG to flush debug logs.
            console_handler.setLevel(logging.DEBUG)
            mem_handler.flush()
            console_handler.setLevel(logging.INFO)

    def setUp(self):
        logger.info("Opening Real Estate Predictor webpage...")
        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(1)  # Allow onload to initialize the homes.
        logger.info("Page loaded.")

    def test_initial_display(self):
        test_id = "RE-02"
        log_test_case(test_id, "Verify initial home display with image and estimated value.")
        driver = self.driver
        picture = driver.find_element(By.ID, "picture")
        pic_src = picture.get_attribute("src")
        logger.info(f"Picture source: {pic_src}")
        self.assertNotEqual(pic_src, "", "House image source should not be empty on initial load.")
        
        value_elem = driver.find_element(By.ID, "value")
        value_text = value_elem.text
        logger.info(f"Value text: {value_text}")
        self.assertIn("This home should be worth", value_text,
                      "Estimated value text missing or incorrect on initial load.")
        log_test_case_end(test_id)

    def test_navigation_buttons(self):
        test_id = "RE-03"
        log_test_case(test_id, "Verify that Next and Prev buttons navigate correctly with wrap-around.")
        driver = self.driver
        initial_src = driver.find_element(By.ID, "picture").get_attribute("src")
        logger.info(f"Initial image src: {initial_src}")

        next_button = driver.find_element(By.ID, "next")
        logger.info("Clicking Next button...")
        next_button.click()
        time.sleep(1)
        new_src = driver.find_element(By.ID, "picture").get_attribute("src")
        logger.info(f"Image src after Next: {new_src}")
        self.assertNotEqual(initial_src, new_src, "Next button did not change the displayed home.")

        prev_button = driver.find_element(By.ID, "prev")
        logger.info("Clicking Prev button...")
        prev_button.click()
        time.sleep(1)
        reverted_src = driver.find_element(By.ID, "picture").get_attribute("src")
        logger.info(f"Image src after Prev: {reverted_src}")
        self.assertEqual(initial_src, reverted_src, "Prev button did not revert to the original home.")
        log_test_case_end(test_id)

    def test_comment_submission_and_persistence(self):
        test_id = "RE-04"
        log_test_case(test_id, "Verify that comment submission works and persists after navigation.")
        driver = self.driver
        username_field = driver.find_element(By.CSS_SELECTOR, "textarea.username")
        comment_field = driver.find_element(By.CSS_SELECTOR, "textarea.comment")
        submit_button = driver.find_element(By.ID, "submit")
        
        test_username = "TestUser"
        test_comment = "This is a test comment."
        logger.info(f"Entering username: {test_username} and comment: {test_comment}")
        username_field.clear()
        username_field.send_keys(test_username)
        comment_field.clear()
        comment_field.send_keys(test_comment)
        logger.info("Clicking Submit button...")
        submit_button.click()

        blogs_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "blogs"))
        )
        blogs_html = blogs_div.get_attribute("innerHTML")
        logger.info(f"Blogs HTML after submission: {blogs_html}")
        self.assertIn(test_username, blogs_html, "Submitted username not found in comments.")
        self.assertIn(test_comment, blogs_html, "Submitted comment text not found in comments.")

        self.assertEqual(username_field.get_attribute("value"), "", "Username field not cleared after submission.")
        self.assertEqual(comment_field.get_attribute("value"), "", "Comment field not cleared after submission.")

        next_button = driver.find_element(By.ID, "next")
        logger.info("Navigating to next home for comment persistence test...")
        next_button.click()
        time.sleep(1)
        prev_button = driver.find_element(By.ID, "prev")
        prev_button.click()
        time.sleep(1)
        blogs_html = driver.find_element(By.ID, "blogs").get_attribute("innerHTML")
        logger.info(f"Blogs HTML after navigation: {blogs_html}")
        self.assertIn(test_username, blogs_html, "Comment did not persist after navigation.")
        log_test_case_end(test_id)

    def test_stress_navigation(self):
        test_id = "RE-05"
        log_test_case(test_id, "Stress test: Rapidly click Next button multiple times.")
        driver = self.driver
        next_button = driver.find_element(By.ID, "next")
        for i in range(20):
            logger.debug(f"Stress navigation iteration: {i+1}")
            next_button.click()
            time.sleep(0.2)
        picture_src = driver.find_element(By.ID, "picture").get_attribute("src")
        logger.info(f"Final picture src after stress navigation: {picture_src}")
        self.assertNotEqual(picture_src, "", "Picture src should not be empty after rapid navigation.")
        log_test_case_end(test_id)

    def test_scalability_comments(self):
        test_id = "RE-06"
        log_test_case(test_id, "Scalability test: Add multiple comments and verify responsiveness.")
        driver = self.driver
        username_field = driver.find_element(By.CSS_SELECTOR, "textarea.username")
        comment_field = driver.find_element(By.CSS_SELECTOR, "textarea.comment")
        submit_button = driver.find_element(By.ID, "submit")
        num_comments = 50
        logger.info(f"Adding {num_comments} comments...")
        for i in range(num_comments):
            username_field.clear()
            comment_field.clear()
            username_field.send_keys(f"User{i}")
            comment_field.send_keys(f"Comment {i}")
            submit_button.click()
            time.sleep(0.3)
        blogs_html = driver.find_element(By.ID, "blogs").get_attribute("innerHTML")
        logger.info("Final blogs section HTML (truncated): " + blogs_html[:200])
        self.assertIn("User0", blogs_html, "Comment from User0 not found.")
        self.assertIn("Comment 49", blogs_html, "Last comment not found.")
        log_test_case_end(test_id)

    def test_performance_navigation(self):
        test_id = "RE-07"
        log_test_case(test_id, "Performance test: Measure time taken to navigate to next home.")
        driver = self.driver
        next_button = driver.find_element(By.ID, "next")
        start_time = time.time()
        next_button.click()
        WebDriverWait(driver, 5).until(
            lambda d: d.find_element(By.ID, "picture").get_attribute("src") != ""
        )
        elapsed = time.time() - start_time
        logger.info(f"Navigation to next home took {elapsed:.4f} seconds.")
        self.assertLess(elapsed, 5, "Navigation took longer than expected (over 5 seconds).")
        log_test_case_end(test_id)

    def test_intentional_failure(self):
        test_id = "RE-08"
        log_test_case(test_id, "Intentional failure test to demonstrate red logging.", tester="John Doe")
        try:
            self.assertEqual(1, 2, "Intentional failure: 1 is not equal to 2.")
        except AssertionError as e:
            log_test_case_end(test_id, status="Fail", notes=str(e))
            raise

if __name__ == "__main__":
    unittest.main()
