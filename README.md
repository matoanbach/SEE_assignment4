# Assignment 4 – Automated Web-Page Testing with Selenium

## Steps to set up the test suite

- Create and activate a python virtual environment
**- Note:** If there is any virtual existed before, delete it and create a new one (referred to the last step below)
```sh
python3 -m venv venv # create a virtual environment named "venv" at the current directory
source venv/bin/activate # activate the virtual environment
```

- Verify if the virtual environment is activated
```sh
which python3 # expected: /Users/tieuma/Library/CloudStorage/OneDrive-Seneca/Seneca/SEMESTER5/SEE600a4/venv/bin/python3
which pip3 # expected: /Users/tieuma/Library/CloudStorage/OneDrive-Seneca/Seneca/SEMESTER5/SED600/a4/venv/bin/pip3
```

- Install dependencies
```sh
pip3 install selenium
pip3 install colorlog
```


- Run tests:
```sh
python3 test_suite.py
```

## Questions & Answers

### 1. What is Robot Framework, and how does Selenium fit inside Robot Framework?

**Description:**  
Robot Framework is an open-source, generic test automation framework that uses a keyword-driven approach. This makes it easier to write test cases in a human-readable tabular format without needing extensive programming expertise. It is commonly used for acceptance testing and robotic process automation.

**How Selenium Fits In:**  
Selenium integrates with Robot Framework through the SeleniumLibrary. This library exposes keywords (such as "Open Browser", "Input Text", "Click Button") that internally use Selenium WebDriver to interact with web browsers. This allows testers to create high-level test cases in Robot Framework that leverage Selenium’s powerful browser automation capabilities.

---

### 2. How could you use Selenium to perform record and playback?

**Description:**  
Selenium offers record-and-playback functionality primarily through Selenium IDE—a browser extension that can capture all user interactions (clicks, form entries, navigations, etc.) and convert them into a test script.

**How to Use It:**  
- **Record:** Launch Selenium IDE (available for Chrome and Firefox) and start a new recording session. Perform the manual test (e.g., navigating to a login page, entering credentials, and clicking the login button). Selenium IDE will record these actions.
- **Playback:** Once the recording is complete, Selenium IDE can play back the recorded test steps automatically. This is useful for regression testing, as you can rerun the same manual test without having to repeat it by hand.
- **Export:** Tests can be exported from Selenium IDE into various programming languages (like Python), so they can be integrated into larger automated test suites.

**Example Use:**  
In a project, I could record a user registration process using Selenium IDE and then export the test to a Python script. This script can later be integrated into our continuous integration pipeline to verify that the registration feature works correctly after each update.

---

### 3. In this assignment we used Selenium WebDriver. What is Selenium IDE?

**Description:**  
Selenium IDE is an integrated development environment for creating Selenium tests. It is available as a browser extension for both Chrome and Firefox and provides a simple interface for recording, editing, and debugging tests without writing code manually.

**Key Features:**  
- **Record-and-Playback:** Allows users to record their interactions with a web application and then replay those interactions as tests.
- **Editing & Debugging:** Provides a GUI to easily modify and troubleshoot test scripts.
- **Export Capability:** Recorded tests can be exported to various programming languages (e.g., Python, Java) for more robust test automation using Selenium WebDriver.

**Example Use:**  

For a project in BSA, I might use Selenium IDE to quickly create and verify tests for critical user flows (such as login or checkout). Once confirmed, these tests could be exported to Python and integrated into a larger test suite for regression testing. Open Browser http://example.com Chrome Input Text username_field myUsername Click Button login_button Page Should Contain Welcome, myUsername!

---

### 4. What is Selenium Grid?

**Description:**  
Selenium Grid is a tool that enables you to run Selenium tests in parallel across multiple machines, browsers, and operating systems. It employs a hub-node architecture where a central hub receives test requests and distributes them to registered nodes (each running a specific browser and OS configuration).

**Benefits:**  
- **Parallel Execution:** Reduces test execution time by running tests simultaneously across different environments.
- **Cross-Browser Testing:** Ensures your application behaves correctly on multiple browsers and operating systems.
- **Scalability:** Easily scales testing across various environments without modifying the test code.

**Example Use:**  
In a real-world project, if I need to verify that a web application works across Chrome, Firefox, and Edge on Windows and macOS, I would set up Selenium Grid. This setup would allow me to distribute my test cases over several nodes and run them concurrently, significantly speeding up the testing process and ensuring cross-browser compatibility.




## Test logging

```log
Last login: Mon Mar 10 15:15:33 on ttys000
(base) tieuma@Tieus-MacBook-Pro A4 % source venv/bin/activate
(venv) (base) tieuma@Tieus-MacBook-Pro A4 % python test_suite.py 
2025-03-10 15:54:05 [INFO] =================================
2025-03-10 15:54:05 [INFO] [RE-01] Setting up WebDriver for test suite...
2025-03-10 15:54:06 [INFO] [RE-01] WebDriver setup completed.
2025-03-10 15:54:06 [INFO] =================================
2025-03-10 15:54:06 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:07 [INFO] Page loaded.
2025-03-10 15:54:07 [INFO] =================================
2025-03-10 15:54:07 [INFO] Test Case ID: RE-04
2025-03-10 15:54:07 [INFO] Description: Verify that comment submission works and persists after navigation.
2025-03-10 15:54:07 [INFO] Date & Time: 2025-03-10 15:54:07
2025-03-10 15:54:07 [INFO] Tested By: John Doe
2025-03-10 15:54:07 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:07 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:07 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:07 [INFO] Entering username: TestUser and comment: This is a test comment.
2025-03-10 15:54:08 [INFO] Clicking Submit button...
2025-03-10 15:54:08 [INFO] Blogs HTML after submission: <p><b>TestUser</b>: This is a test comment.</p>
2025-03-10 15:54:08 [INFO] Navigating to next home for comment persistence test...
2025-03-10 15:54:10 [INFO] Blogs HTML after navigation: <p><b>TestUser</b>: This is a test comment.</p>
2025-03-10 15:54:10 [INFO] Status: Pass
2025-03-10 15:54:10 [INFO] Notes: N/A
2025-03-10 15:54:10 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:10 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:10 [INFO] Issue: N/A
2025-03-10 15:54:10 [INFO] Resolution: N/A
2025-03-10 15:54:10 [INFO] =================================
2025-03-10 15:54:10 [INFO] [RE-04] - END test
2025-03-10 15:54:10 [INFO] 
E2025-03-10 15:54:10 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:11 [INFO] Page loaded.
2025-03-10 15:54:11 [INFO] =================================
2025-03-10 15:54:11 [INFO] Test Case ID: RE-02
2025-03-10 15:54:11 [INFO] Description: Verify initial home display with image and estimated value.
2025-03-10 15:54:11 [INFO] Date & Time: 2025-03-10 15:54:11
2025-03-10 15:54:11 [INFO] Tested By: John Doe
2025-03-10 15:54:11 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:11 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:11 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:11 [INFO] Picture source: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:11 [INFO] Value text: This home should be worth 902500.00
2025-03-10 15:54:11 [INFO] Status: Pass
2025-03-10 15:54:11 [INFO] Notes: N/A
2025-03-10 15:54:11 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:11 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:11 [INFO] Issue: N/A
2025-03-10 15:54:11 [INFO] Resolution: N/A
2025-03-10 15:54:11 [INFO] =================================
2025-03-10 15:54:11 [INFO] [RE-02] - END test
2025-03-10 15:54:11 [INFO] 
E2025-03-10 15:54:11 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:12 [INFO] Page loaded.
2025-03-10 15:54:12 [INFO] =================================
2025-03-10 15:54:12 [INFO] Test Case ID: RE-08
2025-03-10 15:54:12 [INFO] Description: Intentional failure test to demonstrate red logging.
2025-03-10 15:54:12 [INFO] Date & Time: 2025-03-10 15:54:12
2025-03-10 15:54:12 [INFO] Tested By: John Doe
2025-03-10 15:54:12 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:12 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:12 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:12 [ERROR] Status: Fail
2025-03-10 15:54:05 [INFO] =================================
2025-03-10 15:54:05 [INFO] [RE-01] Setting up WebDriver for test suite...
2025-03-10 15:54:05 [DEBUG] Selenium Manager binary found at: /Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/venv/lib/python3.12/site-packages/selenium/webdriver/common/macos/selenium-manager
2025-03-10 15:54:05 [DEBUG] Executing process: /Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/venv/lib/python3.12/site-packages/selenium/webdriver/common/macos/selenium-manager --browser chrome --debug --language-binding python --output json
2025-03-10 15:54:05 [DEBUG] chromedriver not found in PATH
2025-03-10 15:54:05 [DEBUG] chrome detected at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
2025-03-10 15:54:05 [DEBUG] Running command: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
2025-03-10 15:54:05 [DEBUG] Output: "Google Chrome 134.0.6998.45 "
2025-03-10 15:54:05 [DEBUG] Detected browser: chrome 134.0.6998.45
2025-03-10 15:54:05 [DEBUG] Required driver: chromedriver 134.0.6998.35
2025-03-10 15:54:05 [DEBUG] chromedriver 134.0.6998.35 already in the cache
2025-03-10 15:54:05 [DEBUG] Driver path: /Users/tieuma/.cache/selenium/chromedriver/mac-arm64/134.0.6998.35/chromedriver
2025-03-10 15:54:05 [DEBUG] Browser path: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
2025-03-10 15:54:05 [DEBUG] Started executable: `/Users/tieuma/.cache/selenium/chromedriver/mac-arm64/134.0.6998.35/chromedriver` in a child process with pid: 9776 using 0 to output -3
2025-03-10 15:54:05 [DEBUG] POST http://localhost:49719/session {'capabilities': {'firstMatch': [{}], 'alwaysMatch': {'browserName': 'chrome', 'pageLoadStrategy': <PageLoadStrategy.normal: 'normal'>, 'browserVersion': None, 'goog:chromeOptions': {'extensions': [], 'binary': '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', 'args': []}}}}
2025-03-10 15:54:05 [DEBUG] Starting new HTTP connection (1): localhost:49719
2025-03-10 15:54:06 [DEBUG] http://localhost:49719 "POST /session HTTP/1.1" 200 0
2025-03-10 15:54:06 [DEBUG] Remote response: status=200 | data={"value":{"capabilities":{"acceptInsecureCerts":false,"browserName":"chrome","browserVersion":"134.0.6998.45","chrome":{"chromedriverVersion":"134.0.6998.35 (ea6ef4c2ac15ae95d2cfd65682da62c093415099-refs/branch-heads/6998@{#1472})","userDataDir":"/var/folders/gd/j6n530ds7t5_zxgkn2xwbkcr0000gn/T/.org.chromium.Chromium.15Vm1j"},"fedcm:accounts":true,"goog:chromeOptions":{"debuggerAddress":"localhost:49727"},"networkConnectionEnabled":false,"pageLoadStrategy":"normal","platformName":"mac","proxy":{},"setWindowRect":true,"strictFileInteractability":false,"timeouts":{"implicit":0,"pageLoad":300000,"script":30000},"unhandledPromptBehavior":"dismiss and notify","webauthn:extension:credBlob":true,"webauthn:extension:largeBlob":true,"webauthn:extension:minPinLength":true,"webauthn:extension:prf":true,"webauthn:virtualAuthenticators":true},"sessionId":"9daa00d7f734a1208184110a60ee3b9d"}} | headers=HTTPHeaderDict({'Content-Length': '890', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:06 [DEBUG] Finished Request
2025-03-10 15:54:06 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/window/maximize {}
2025-03-10 15:54:06 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/window/maximize HTTP/1.1" 200 0
2025-03-10 15:54:06 [DEBUG] Remote response: status=200 | data={"value":{"height":1055,"width":1920,"x":-275,"y":-1055}} | headers=HTTPHeaderDict({'Content-Length': '57', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:06 [DEBUG] Finished Request
2025-03-10 15:54:06 [INFO] [RE-01] WebDriver setup completed.
2025-03-10 15:54:06 [INFO] =================================
2025-03-10 15:54:06 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:06 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:06 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:06 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:06 [DEBUG] Finished Request
2025-03-10 15:54:06 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:06 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:06 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.9"}} | headers=HTTPHeaderDict({'Content-Length': '125', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:06 [DEBUG] Finished Request
2025-03-10 15:54:07 [INFO] Page loaded.
2025-03-10 15:54:07 [INFO] =================================
2025-03-10 15:54:07 [INFO] Test Case ID: RE-04
2025-03-10 15:54:07 [INFO] Description: Verify that comment submission works and persists after navigation.
2025-03-10 15:54:07 [INFO] Date & Time: 2025-03-10 15:54:07
2025-03-10 15:54:07 [INFO] Tested By: John Doe
2025-03-10 15:54:07 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:07 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:07 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:07 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': 'textarea.username'}
2025-03-10 15:54:07 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:07 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.2"}} | headers=HTTPHeaderDict({'Content-Length': '125', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:07 [DEBUG] Finished Request
2025-03-10 15:54:07 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': 'textarea.comment'}
2025-03-10 15:54:07 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:07 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.3"}} | headers=HTTPHeaderDict({'Content-Length': '125', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:07 [DEBUG] Finished Request
2025-03-10 15:54:07 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="submit"]'}
2025-03-10 15:54:07 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:07 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.8"}} | headers=HTTPHeaderDict({'Content-Length': '125', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:07 [DEBUG] Finished Request
2025-03-10 15:54:07 [INFO] Entering username: TestUser and comment: This is a test comment.
2025-03-10 15:54:07 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.2/clear {}
2025-03-10 15:54:07 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.2/clear HTTP/1.1" 200 0
2025-03-10 15:54:07 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:07 [DEBUG] Finished Request
2025-03-10 15:54:07 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.2/value {'text': 'TestUser', 'value': ['T', 'e', 's', 't', 'U', 's', 'e', 'r']}
2025-03-10 15:54:07 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.2/value HTTP/1.1" 200 0
2025-03-10 15:54:07 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:07 [DEBUG] Finished Request
2025-03-10 15:54:07 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.3/clear {}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.3/clear HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.3/value {'text': 'This is a test comment.', 'value': ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '.']}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.3/value HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [INFO] Clicking Submit button...
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.8/click {}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.8/click HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="blogs"]'}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.34"}} | headers=HTTPHeaderDict({'Content-Length': '126', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.34'}, 'innerHTML']}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":"\u003Cp>\u003Cb>TestUser\u003C/b>: This is a test comment.\u003C/p>"} | headers=HTTPHeaderDict({'Content-Length': '79', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [INFO] Blogs HTML after submission: <p><b>TestUser</b>: This is a test comment.</p>
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.2'}, 'value']}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":""} | headers=HTTPHeaderDict({'Content-Length': '12', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.3'}, 'value']}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":""} | headers=HTTPHeaderDict({'Content-Length': '12', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="next"]'}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.5"}} | headers=HTTPHeaderDict({'Content-Length': '125', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:08 [INFO] Navigating to next home for comment persistence test...
2025-03-10 15:54:08 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.5/click {}
2025-03-10 15:54:08 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.5/click HTTP/1.1" 200 0
2025-03-10 15:54:08 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:08 [DEBUG] Finished Request
2025-03-10 15:54:09 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="prev"]'}
2025-03-10 15:54:09 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:09 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.4"}} | headers=HTTPHeaderDict({'Content-Length': '125', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:09 [DEBUG] Finished Request
2025-03-10 15:54:09 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.4/click {}
2025-03-10 15:54:09 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.4/click HTTP/1.1" 200 0
2025-03-10 15:54:09 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:09 [DEBUG] Finished Request
2025-03-10 15:54:10 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="blogs"]'}
2025-03-10 15:54:10 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:10 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.34"}} | headers=HTTPHeaderDict({'Content-Length': '126', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:10 [DEBUG] Finished Request
2025-03-10 15:54:10 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.189D199017DCD3AB80949BD786C7C8A1.e.34'}, 'innerHTML']}
2025-03-10 15:54:10 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:10 [DEBUG] Remote response: status=200 | data={"value":"\u003Cp>\u003Cb>TestUser\u003C/b>: This is a test comment.\u003C/p>"} | headers=HTTPHeaderDict({'Content-Length': '79', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:10 [DEBUG] Finished Request
2025-03-10 15:54:10 [INFO] Blogs HTML after navigation: <p><b>TestUser</b>: This is a test comment.</p>
2025-03-10 15:54:10 [INFO] Status: Pass
2025-03-10 15:54:10 [INFO] Notes: N/A
2025-03-10 15:54:10 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:10 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:10 [INFO] Issue: N/A
2025-03-10 15:54:10 [INFO] Resolution: N/A
2025-03-10 15:54:10 [INFO] =================================
2025-03-10 15:54:10 [INFO] [RE-04] - END test
2025-03-10 15:54:10 [INFO] 
2025-03-10 15:54:10 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:10 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:10 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:10 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:10 [DEBUG] Finished Request
2025-03-10 15:54:10 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:10 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:10 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.73A6D9F421C2B68B16024C2598300E72.e.79"}} | headers=HTTPHeaderDict({'Content-Length': '126', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:10 [DEBUG] Finished Request
2025-03-10 15:54:11 [INFO] Page loaded.
2025-03-10 15:54:11 [INFO] =================================
2025-03-10 15:54:11 [INFO] Test Case ID: RE-02
2025-03-10 15:54:11 [INFO] Description: Verify initial home display with image and estimated value.
2025-03-10 15:54:11 [INFO] Date & Time: 2025-03-10 15:54:11
2025-03-10 15:54:11 [INFO] Tested By: John Doe
2025-03-10 15:54:11 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:11 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:11 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:11 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="picture"]'}
2025-03-10 15:54:11 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:11 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.73A6D9F421C2B68B16024C2598300E72.e.72"}} | headers=HTTPHeaderDict({'Content-Length': '126', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:11 [DEBUG] Finished Request
2025-03-10 15:54:11 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.73A6D9F421C2B68B16024C2598300E72.e.72'}, 'src']}
2025-03-10 15:54:11 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:11 [DEBUG] Remote response: status=200 | data={"value":"https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG"} | headers=HTTPHeaderDict({'Content-Length': '124', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:11 [DEBUG] Finished Request
2025-03-10 15:54:11 [INFO] Picture source: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:11 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="value"]'}
2025-03-10 15:54:11 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:11 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.73A6D9F421C2B68B16024C2598300E72.e.84"}} | headers=HTTPHeaderDict({'Content-Length': '126', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:11 [DEBUG] Finished Request
2025-03-10 15:54:11 [DEBUG] GET http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.73A6D9F421C2B68B16024C2598300E72.e.84/text {}
2025-03-10 15:54:11 [DEBUG] http://localhost:49719 "GET /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.73A6D9F421C2B68B16024C2598300E72.e.84/text HTTP/1.1" 200 0
2025-03-10 15:54:11 [DEBUG] Remote response: status=200 | data={"value":"This home should be worth 902500.00"} | headers=HTTPHeaderDict({'Content-Length': '47', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:11 [DEBUG] Finished Request
2025-03-10 15:54:11 [INFO] Value text: This home should be worth 902500.00
2025-03-10 15:54:11 [INFO] Status: Pass
2025-03-10 15:54:11 [INFO] Notes: N/A
2025-03-10 15:54:11 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:11 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:11 [INFO] Issue: N/A
2025-03-10 15:54:11 [INFO] Resolution: N/A
2025-03-10 15:54:11 [INFO] =================================
2025-03-10 15:54:11 [INFO] [RE-02] - END test
2025-03-10 15:54:11 [INFO] 
2025-03-10 15:54:11 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:11 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:11 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:11 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:11 [DEBUG] Finished Request
2025-03-10 15:54:11 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:11 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:11 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.7061CF688964D3E105921526E2A59EAF.e.115"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:11 [DEBUG] Finished Request
2025-03-10 15:54:12 [INFO] Page loaded.
2025-03-10 15:54:12 [INFO] =================================
2025-03-10 15:54:12 [INFO] Test Case ID: RE-08
2025-03-10 15:54:12 [INFO] Description: Intentional failure test to demonstrate red logging.
2025-03-10 15:54:12 [INFO] Date & Time: 2025-03-10 15:54:12
2025-03-10 15:54:12 [INFO] Tested By: John Doe
2025-03-10 15:54:12 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:12 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:12 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:12 [ERROR] Status: Fail
2025-03-10 15:54:12 [ERROR] Notes: 1 != 2 : Intentional failure: 1 is not equal to 2.
2025-03-10 15:54:12 [ERROR] Notes: 1 != 2 : Intentional failure: 1 is not equal to 2.
2025-03-10 15:54:12 [ERROR] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:12 [ERROR] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:12 [ERROR] Log File: (Refer to log output)
2025-03-10 15:54:12 [ERROR] Log File: (Refer to log output)
2025-03-10 15:54:12 [ERROR] Issue: N/A
2025-03-10 15:54:12 [ERROR] Issue: N/A
2025-03-10 15:54:12 [ERROR] Resolution: N/A
2025-03-10 15:54:12 [ERROR] Resolution: N/A
2025-03-10 15:54:12 [INFO] =================================
2025-03-10 15:54:12 [ERROR] [RE-08] - END test
2025-03-10 15:54:12 [INFO] =================================
2025-03-10 15:54:12 [ERROR] [RE-08] - END test
2025-03-10 15:54:12 [INFO] 
FE2025-03-10 15:54:12 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:13 [INFO] Page loaded.
2025-03-10 15:54:13 [INFO] =================================
2025-03-10 15:54:13 [INFO] Test Case ID: RE-03
2025-03-10 15:54:13 [INFO] Description: Verify that Next and Prev buttons navigate correctly with wrap-around.
2025-03-10 15:54:13 [INFO] Date & Time: 2025-03-10 15:54:13
2025-03-10 15:54:13 [INFO] Tested By: John Doe
2025-03-10 15:54:13 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:13 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:13 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:13 [INFO] Initial image src: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:13 [INFO] Clicking Next button...
2025-03-10 15:54:14 [INFO] Image src after Next: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/3956Beacham.PNG
2025-03-10 15:54:14 [INFO] Clicking Prev button...
2025-03-10 15:54:15 [INFO] Image src after Prev: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:15 [INFO] Status: Pass
2025-03-10 15:54:15 [INFO] Notes: N/A
2025-03-10 15:54:15 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:15 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:15 [INFO] Issue: N/A
2025-03-10 15:54:15 [INFO] Resolution: N/A
2025-03-10 15:54:15 [INFO] =================================
2025-03-10 15:54:15 [INFO] [RE-03] - END test
2025-03-10 15:54:15 [INFO] 
E2025-03-10 15:54:15 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:16 [INFO] Page loaded.
2025-03-10 15:54:16 [INFO] =================================
2025-03-10 15:54:16 [INFO] Test Case ID: RE-07
2025-03-10 15:54:16 [INFO] Description: Performance test: Measure time taken to navigate to next home.
2025-03-10 15:54:16 [INFO] Date & Time: 2025-03-10 15:54:16
2025-03-10 15:54:16 [INFO] Tested By: John Doe
2025-03-10 15:54:16 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:16 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:16 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:16 [INFO] Navigation to next home took 0.0299 seconds.
2025-03-10 15:54:16 [INFO] Status: Pass
2025-03-10 15:54:16 [INFO] Notes: N/A
2025-03-10 15:54:16 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:16 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:16 [INFO] Issue: N/A
2025-03-10 15:54:16 [INFO] Resolution: N/A
2025-03-10 15:54:16 [INFO] =================================
2025-03-10 15:54:16 [INFO] [RE-07] - END test
2025-03-10 15:54:16 [INFO] 
E2025-03-10 15:54:16 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:17 [INFO] Page loaded.
2025-03-10 15:54:17 [INFO] =================================
2025-03-10 15:54:17 [INFO] Test Case ID: RE-06
2025-03-10 15:54:17 [INFO] Description: Scalability test: Add multiple comments and verify responsiveness.
2025-03-10 15:54:17 [INFO] Date & Time: 2025-03-10 15:54:17
2025-03-10 15:54:17 [INFO] Tested By: John Doe
2025-03-10 15:54:17 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:17 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:17 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:17 [INFO] Adding 50 comments...
2025-03-10 15:54:38 [INFO] Final blogs section HTML (truncated): <p><b>User0</b>: Comment 0</p><p><b>User1</b>: Comment 1</p><p><b>User2</b>: Comment 2</p><p><b>User3</b>: Comment 3</p><p><b>User4</b>: Comment 4</p><p><b>User5</b>: Comment 5</p><p><b>User6</b>: Com
2025-03-10 15:54:38 [INFO] Status: Pass
2025-03-10 15:54:38 [INFO] Notes: N/A
2025-03-10 15:54:38 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:38 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:38 [INFO] Issue: N/A
2025-03-10 15:54:38 [INFO] Resolution: N/A
2025-03-10 15:54:38 [INFO] =================================
2025-03-10 15:54:38 [INFO] [RE-06] - END test
2025-03-10 15:54:38 [INFO] 
E2025-03-10 15:54:38 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:39 [INFO] Page loaded.
2025-03-10 15:54:39 [INFO] =================================
2025-03-10 15:54:39 [INFO] Test Case ID: RE-05
2025-03-10 15:54:39 [INFO] Description: Stress test: Rapidly click Next button multiple times.
2025-03-10 15:54:39 [INFO] Date & Time: 2025-03-10 15:54:39
2025-03-10 15:54:39 [INFO] Tested By: John Doe
2025-03-10 15:54:39 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:39 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:39 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:44 [INFO] Final picture src after stress navigation: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:44 [INFO] Status: Pass
2025-03-10 15:54:44 [INFO] Notes: N/A
2025-03-10 15:54:44 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:44 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:44 [INFO] Issue: N/A
2025-03-10 15:54:44 [INFO] Resolution: N/A
2025-03-10 15:54:44 [INFO] =================================
2025-03-10 15:54:44 [INFO] [RE-05] - END test
2025-03-10 15:54:44 [INFO] 
E2025-03-10 15:54:44 [INFO] Closing WebDriver...
2025-03-10 15:54:44 [INFO] WebDriver closed.

======================================================================
ERROR: test_comment_submission_and_persistence (__main__.RealEstatePredictorTests.test_comment_submission_and_persistence)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
ERROR: test_initial_display (__main__.RealEstatePredictorTests.test_initial_display)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
ERROR: test_intentional_failure (__main__.RealEstatePredictorTests.test_intentional_failure)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
ERROR: test_navigation_buttons (__main__.RealEstatePredictorTests.test_navigation_buttons)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
ERROR: test_performance_navigation (__main__.RealEstatePredictorTests.test_performance_navigation)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
ERROR: test_scalability_comments (__main__.RealEstatePredictorTests.test_scalability_comments)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
ERROR: test_stress_navigation (__main__.RealEstatePredictorTests.test_stress_navigation)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 103, in tearDown
    for test, exc in outcome.errors:
                     ^^^^^^^^^^^^^^
AttributeError: '_Outcome' object has no attribute 'errors'

======================================================================
FAIL: test_intentional_failure (__main__.RealEstatePredictorTests.test_intentional_failure)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/tieuma/Documents/school/SEMESTER 6/SEE600/A4/test_suite.py", line 261, in test_intentional_failure
    self.assertEqual(1, 2, "Intentional failure: 1 is not equal to 2.")
AssertionError: 1 != 2 : Intentional failure: 1 is not equal to 2.

----------------------------------------------------------------------
Ran 7 tests in 39.817s

FAILED (failures=1, errors=7)
2025-03-10 15:54:12 [INFO] 
2025-03-10 15:54:12 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:12 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:12 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:12 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:12 [DEBUG] Finished Request
2025-03-10 15:54:12 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:12 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:12 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.158"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:12 [DEBUG] Finished Request
2025-03-10 15:54:13 [INFO] Page loaded.
2025-03-10 15:54:13 [INFO] =================================
2025-03-10 15:54:13 [INFO] Test Case ID: RE-03
2025-03-10 15:54:13 [INFO] Description: Verify that Next and Prev buttons navigate correctly with wrap-around.
2025-03-10 15:54:13 [INFO] Date & Time: 2025-03-10 15:54:13
2025-03-10 15:54:13 [INFO] Tested By: John Doe
2025-03-10 15:54:13 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:13 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:13 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:13 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="picture"]'}
2025-03-10 15:54:13 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:13 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.160"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:13 [DEBUG] Finished Request
2025-03-10 15:54:13 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.160'}, 'src']}
2025-03-10 15:54:13 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:13 [DEBUG] Remote response: status=200 | data={"value":"https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG"} | headers=HTTPHeaderDict({'Content-Length': '124', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:13 [DEBUG] Finished Request
2025-03-10 15:54:13 [INFO] Initial image src: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:13 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="next"]'}
2025-03-10 15:54:13 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:13 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.173"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:13 [DEBUG] Finished Request
2025-03-10 15:54:13 [INFO] Clicking Next button...
2025-03-10 15:54:13 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.173/click {}
2025-03-10 15:54:13 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.173/click HTTP/1.1" 200 0
2025-03-10 15:54:13 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:13 [DEBUG] Finished Request
2025-03-10 15:54:14 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="picture"]'}
2025-03-10 15:54:14 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:14 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.160"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:14 [DEBUG] Finished Request
2025-03-10 15:54:14 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.160'}, 'src']}
2025-03-10 15:54:14 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:14 [DEBUG] Remote response: status=200 | data={"value":"https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/3956Beacham.PNG"} | headers=HTTPHeaderDict({'Content-Length': '115', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:14 [DEBUG] Finished Request
2025-03-10 15:54:14 [INFO] Image src after Next: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/3956Beacham.PNG
2025-03-10 15:54:14 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="prev"]'}
2025-03-10 15:54:14 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:14 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.172"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:14 [DEBUG] Finished Request
2025-03-10 15:54:14 [INFO] Clicking Prev button...
2025-03-10 15:54:14 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.172/click {}
2025-03-10 15:54:14 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.172/click HTTP/1.1" 200 0
2025-03-10 15:54:14 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:14 [DEBUG] Finished Request
2025-03-10 15:54:15 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="picture"]'}
2025-03-10 15:54:15 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:15 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.160"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:15 [DEBUG] Finished Request
2025-03-10 15:54:15 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.743A788D559D9F3923B20BD03379C1DA.e.160'}, 'src']}
2025-03-10 15:54:15 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:15 [DEBUG] Remote response: status=200 | data={"value":"https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG"} | headers=HTTPHeaderDict({'Content-Length': '124', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:15 [DEBUG] Finished Request
2025-03-10 15:54:15 [INFO] Image src after Prev: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:15 [INFO] Status: Pass
2025-03-10 15:54:15 [INFO] Notes: N/A
2025-03-10 15:54:15 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:15 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:15 [INFO] Issue: N/A
2025-03-10 15:54:15 [INFO] Resolution: N/A
2025-03-10 15:54:15 [INFO] =================================
2025-03-10 15:54:15 [INFO] [RE-03] - END test
2025-03-10 15:54:15 [INFO] 
2025-03-10 15:54:15 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:15 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:15 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:15 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:15 [DEBUG] Finished Request
2025-03-10 15:54:15 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:15 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:15 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.1EE3449420EF2EE57612152FAFB8A707.e.212"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:15 [DEBUG] Finished Request
2025-03-10 15:54:16 [INFO] Page loaded.
2025-03-10 15:54:16 [INFO] =================================
2025-03-10 15:54:16 [INFO] Test Case ID: RE-07
2025-03-10 15:54:16 [INFO] Description: Performance test: Measure time taken to navigate to next home.
2025-03-10 15:54:16 [INFO] Date & Time: 2025-03-10 15:54:16
2025-03-10 15:54:16 [INFO] Tested By: John Doe
2025-03-10 15:54:16 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:16 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:16 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:16 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="next"]'}
2025-03-10 15:54:16 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:16 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.1EE3449420EF2EE57612152FAFB8A707.e.219"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:16 [DEBUG] Finished Request
2025-03-10 15:54:16 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.1EE3449420EF2EE57612152FAFB8A707.e.219/click {}
2025-03-10 15:54:16 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.1EE3449420EF2EE57612152FAFB8A707.e.219/click HTTP/1.1" 200 0
2025-03-10 15:54:16 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:16 [DEBUG] Finished Request
2025-03-10 15:54:16 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="picture"]'}
2025-03-10 15:54:16 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:16 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.1EE3449420EF2EE57612152FAFB8A707.e.205"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:16 [DEBUG] Finished Request
2025-03-10 15:54:16 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.1EE3449420EF2EE57612152FAFB8A707.e.205'}, 'src']}
2025-03-10 15:54:16 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:16 [DEBUG] Remote response: status=200 | data={"value":"https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/3956Beacham.PNG"} | headers=HTTPHeaderDict({'Content-Length': '115', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:16 [DEBUG] Finished Request
2025-03-10 15:54:16 [INFO] Navigation to next home took 0.0299 seconds.
2025-03-10 15:54:16 [INFO] Status: Pass
2025-03-10 15:54:16 [INFO] Notes: N/A
2025-03-10 15:54:16 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:16 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:16 [INFO] Issue: N/A
2025-03-10 15:54:16 [INFO] Resolution: N/A
2025-03-10 15:54:16 [INFO] =================================
2025-03-10 15:54:16 [INFO] [RE-07] - END test
2025-03-10 15:54:16 [INFO] 
2025-03-10 15:54:16 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:16 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:16 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:16 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:16 [DEBUG] Finished Request
2025-03-10 15:54:16 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:16 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:16 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.249"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:16 [DEBUG] Finished Request
2025-03-10 15:54:17 [INFO] Page loaded.
2025-03-10 15:54:17 [INFO] =================================
2025-03-10 15:54:17 [INFO] Test Case ID: RE-06
2025-03-10 15:54:17 [INFO] Description: Scalability test: Add multiple comments and verify responsiveness.
2025-03-10 15:54:17 [INFO] Date & Time: 2025-03-10 15:54:17
2025-03-10 15:54:17 [INFO] Tested By: John Doe
2025-03-10 15:54:17 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:17 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:17 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': 'textarea.username'}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': 'textarea.comment'}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="submit"]'}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [INFO] Adding 50 comments...
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User0', 'value': ['U', 's', 'e', 'r', '0']}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 0', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '0']}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:17 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:17 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:17 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:17 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User1', 'value': ['U', 's', 'e', 'r', '1']}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 1', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1']}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User2', 'value': ['U', 's', 'e', 'r', '2']}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 2', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2']}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User3', 'value': ['U', 's', 'e', 'r', '3']}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 3', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3']}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:18 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:18 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:18 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:18 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User4', 'value': ['U', 's', 'e', 'r', '4']}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 4', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4']}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User5', 'value': ['U', 's', 'e', 'r', '5']}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 5', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '5']}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:19 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:19 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:19 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:19 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User6', 'value': ['U', 's', 'e', 'r', '6']}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 6', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '6']}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User7', 'value': ['U', 's', 'e', 'r', '7']}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 7', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '7']}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:20 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:20 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:20 [DEBUG] Finished Request
2025-03-10 15:54:20 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User8', 'value': ['U', 's', 'e', 'r', '8']}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 8', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '8']}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User9', 'value': ['U', 's', 'e', 'r', '9']}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 9', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '9']}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User10', 'value': ['U', 's', 'e', 'r', '1', '0']}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 10', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '0']}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:21 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:21 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:21 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:21 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User11', 'value': ['U', 's', 'e', 'r', '1', '1']}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 11', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '1']}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User12', 'value': ['U', 's', 'e', 'r', '1', '2']}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 12', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '2']}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:22 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:22 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:22 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:22 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User13', 'value': ['U', 's', 'e', 'r', '1', '3']}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 13', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '3']}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User14', 'value': ['U', 's', 'e', 'r', '1', '4']}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 14', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '4']}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:23 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:23 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:23 [DEBUG] Finished Request
2025-03-10 15:54:23 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User15', 'value': ['U', 's', 'e', 'r', '1', '5']}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 15', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '5']}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User16', 'value': ['U', 's', 'e', 'r', '1', '6']}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 16', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '6']}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User17', 'value': ['U', 's', 'e', 'r', '1', '7']}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 17', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '7']}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:24 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:24 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:24 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:24 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User18', 'value': ['U', 's', 'e', 'r', '1', '8']}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 18', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '8']}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User19', 'value': ['U', 's', 'e', 'r', '1', '9']}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 19', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '1', '9']}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:25 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:25 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:25 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:25 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User20', 'value': ['U', 's', 'e', 'r', '2', '0']}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 20', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '0']}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User21', 'value': ['U', 's', 'e', 'r', '2', '1']}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 21', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '1']}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:26 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:26 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:26 [DEBUG] Finished Request
2025-03-10 15:54:26 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User22', 'value': ['U', 's', 'e', 'r', '2', '2']}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 22', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '2']}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User23', 'value': ['U', 's', 'e', 'r', '2', '3']}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 23', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '3']}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User24', 'value': ['U', 's', 'e', 'r', '2', '4']}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 24', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '4']}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:27 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:27 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:27 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:27 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User25', 'value': ['U', 's', 'e', 'r', '2', '5']}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 25', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '5']}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User26', 'value': ['U', 's', 'e', 'r', '2', '6']}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 26', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '6']}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:28 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:28 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:28 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:28 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User27', 'value': ['U', 's', 'e', 'r', '2', '7']}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 27', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '7']}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User28', 'value': ['U', 's', 'e', 'r', '2', '8']}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 28', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '8']}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User29', 'value': ['U', 's', 'e', 'r', '2', '9']}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 29', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '2', '9']}
2025-03-10 15:54:29 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:29 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:29 [DEBUG] Finished Request
2025-03-10 15:54:29 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User30', 'value': ['U', 's', 'e', 'r', '3', '0']}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 30', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '0']}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User31', 'value': ['U', 's', 'e', 'r', '3', '1']}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 31', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '1']}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:30 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:30 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:30 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:30 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User32', 'value': ['U', 's', 'e', 'r', '3', '2']}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 32', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '2']}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User33', 'value': ['U', 's', 'e', 'r', '3', '3']}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 33', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '3']}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:31 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:31 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:31 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:31 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User34', 'value': ['U', 's', 'e', 'r', '3', '4']}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 34', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '4']}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User35', 'value': ['U', 's', 'e', 'r', '3', '5']}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 35', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '5']}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User36', 'value': ['U', 's', 'e', 'r', '3', '6']}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 36', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '6']}
2025-03-10 15:54:32 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:32 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:32 [DEBUG] Finished Request
2025-03-10 15:54:32 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User37', 'value': ['U', 's', 'e', 'r', '3', '7']}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 37', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '7']}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User38', 'value': ['U', 's', 'e', 'r', '3', '8']}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 38', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '8']}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:33 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:33 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:33 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:33 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User39', 'value': ['U', 's', 'e', 'r', '3', '9']}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 39', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '3', '9']}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User40', 'value': ['U', 's', 'e', 'r', '4', '0']}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 40', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '0']}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:34 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:34 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:34 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:34 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User41', 'value': ['U', 's', 'e', 'r', '4', '1']}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 41', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '1']}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User42', 'value': ['U', 's', 'e', 'r', '4', '2']}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 42', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '2']}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User43', 'value': ['U', 's', 'e', 'r', '4', '3']}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 43', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '3']}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:35 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:35 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:35 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:35 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User44', 'value': ['U', 's', 'e', 'r', '4', '4']}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 44', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '4']}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User45', 'value': ['U', 's', 'e', 'r', '4', '5']}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 45', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '5']}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:36 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:36 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:36 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:36 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User46', 'value': ['U', 's', 'e', 'r', '4', '6']}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 46', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '6']}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User47', 'value': ['U', 's', 'e', 'r', '4', '7']}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 47', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '7']}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:37 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:37 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:37 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:37 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User48', 'value': ['U', 's', 'e', 'r', '4', '8']}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 48', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '8']}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear {}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/clear HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear {}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/clear HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value {'text': 'User49', 'value': ['U', 's', 'e', 'r', '4', '9']}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.237/value HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value {'text': 'Comment 49', 'value': ['C', 'o', 'm', 'm', 'e', 'n', 't', ' ', '4', '9']}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.247/value HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click {}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.276/click HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="blogs"]'}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.277"}} | headers=HTTPHeaderDict({'Content-Length': '127', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.CC1C1FBD039285FCE042AF7FAF18AFB8.e.277'}, 'innerHTML']}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":"\u003Cp>\u003Cb>User0\u003C/b>: Comment 0\u003C/p>\u003Cp>\u003Cb>User1\u003C/b>: Comment 1\u003C/p>\u003Cp>\u003Cb>User2\u003C/b>: Comment 2\u003C/p>\u003Cp>\u003Cb>User3\u003C/b>: Comment 3\u003C/p>\u003Cp>\u003Cb>User4\u003C/b>: Comment 4\u003C/p>\u003Cp>\u003Cb>User5\u003C/b>: Comment 5\u003C/p>\u003Cp>\u003Cb>User6\u003C/b>: Comment 6\u003C/p>\u003Cp>\u003Cb>User7\u003C/b>: Comment 7\u003C/p>\u003Cp>\u003Cb>User8\u003C/b>: Comment 8\u003C/p>\u003Cp>\u003Cb>User9\u003C/b>: Comment 9\u003C/p>\u003Cp>\u003Cb>User10\u003C/b>: Comment 10\u003C/p>\u003Cp>\u003Cb>User11\u003C/b>: Comment 11\u003C/p>\u003Cp>\u003Cb>User12\u003C/b>: Comment 12\u003C/p>\u003Cp>\u003Cb>User13\u003C/b>: Comment 13\u003C/p>\u003Cp>\u003Cb>User14\u003C/b>: Comment 14\u003C/p>\u003Cp>\u003Cb>User15\u003C/b>: Comment 15\u003C/p>\u003Cp>\u003Cb>User16\u003C/b>: Comment 16\u003C/p>\u003Cp>\u003Cb>User17\u003C/b>: Comment 17\u003C/p>\u003Cp>\u003Cb>User18\u003C/b>: Comment 18\u003C/p>\u003Cp>\u003Cb>User19\u003C/b>: Comment 19\u003C/p>\u003Cp>\u003Cb>User20\u003C/b>: Comment 20\u003C/p>\u003Cp>\u003Cb>User21\u003C/b>: Comment 21\u003C/p>\u003Cp>\u003Cb>User22\u003C/b>: Comment 22\u003C/p>\u003Cp>\u003Cb>User23\u003C/b>: Comment 23\u003C/p>\u003Cp>\u003Cb>User24\u003C/b>: Comment 24\u003C/p>\u003Cp>\u003Cb>User25\u003C/b>: Comment 25\u003C/p>\u003Cp>\u003Cb>User26\u003C/b>: Comment 26\u003C/p>\u003Cp>\u003Cb>User27\u003C/b>: Comment 27\u003C/p>\u003Cp>\u003Cb>User28\u003C/b>: Comment 28\u003C/p>\u003Cp>\u003Cb>User29\u003C/b>: Comment 29\u003C/p>\u003Cp>\u003Cb>User30\u003C/b>: Comment 30\u003C/p>\u003Cp>\u003Cb>User31\u003C/b>: Comment 31\u003C/p>\u003Cp>\u003Cb>User32\u003C/b>: Comment 32\u003C/p>\u003Cp>\u003Cb>User33\u003C/b>: Comment 33\u003C/p>\u003Cp>\u003Cb>User34\u003C/b>: Comment 34\u003C/p>\u003Cp>\u003Cb>User35\u003C/b>: Comment 35\u003C/p>\u003Cp>\u003Cb>User36\u003C/b>: Comment 36\u003C/p>\u003Cp>\u003Cb>User37\u003C/b>: Comment 37\u003C/p>\u003Cp>\u003Cb>User38\u003C/b>: Comment 38\u003C/p>\u003Cp>\u003Cb>User39\u003C/b>: Comment 39\u003C/p>\u003Cp>\u003Cb>User40\u003C/b>: Comment 40\u003C/p>\u003Cp>\u003Cb>User41\u003C/b>: Comment 41\u003C/p>\u003Cp>\u003Cb>User42\u003C/b>: Comment 42\u003C/p>\u003Cp>\u003Cb>User43\u003C/b>: Comment 43\u003C/p>\u003Cp>\u003Cb>User44\u003C/b>: Comment 44\u003C/p>\u003Cp>\u003Cb>User45\u003C/b>: Comment 45\u003C/p>\u003Cp>\u003Cb>User46\u003C/b>: Comment 46\u003C/p>\u003Cp>\u003Cb>User47\u003C/b>: Comment 47\u003C/p>\u003Cp>\u003Cb>User48\u003C/b>: Comment 48\u003C/p>\u003Cp>\u003Cb>User49\u003C/b>: Comment 49\u003C/p>"} | headers=HTTPHeaderDict({'Content-Length': '2592', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [INFO] Final blogs section HTML (truncated): <p><b>User0</b>: Comment 0</p><p><b>User1</b>: Comment 1</p><p><b>User2</b>: Comment 2</p><p><b>User3</b>: Comment 3</p><p><b>User4</b>: Comment 4</p><p><b>User5</b>: Comment 5</p><p><b>User6</b>: Com
2025-03-10 15:54:38 [INFO] Status: Pass
2025-03-10 15:54:38 [INFO] Notes: N/A
2025-03-10 15:54:38 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:38 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:38 [INFO] Issue: N/A
2025-03-10 15:54:38 [INFO] Resolution: N/A
2025-03-10 15:54:38 [INFO] =================================
2025-03-10 15:54:38 [INFO] [RE-06] - END test
2025-03-10 15:54:38 [INFO] 
2025-03-10 15:54:38 [INFO] Opening Real Estate Predictor webpage...
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/url {'url': 'https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/RealEstatePredictor...'}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/url HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:38 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'tag name', 'value': 'body'}
2025-03-10 15:54:38 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:38 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5545"}} | headers=HTTPHeaderDict({'Content-Length': '128', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:38 [DEBUG] Finished Request
2025-03-10 15:54:39 [INFO] Page loaded.
2025-03-10 15:54:39 [INFO] =================================
2025-03-10 15:54:39 [INFO] Test Case ID: RE-05
2025-03-10 15:54:39 [INFO] Description: Stress test: Rapidly click Next button multiple times.
2025-03-10 15:54:39 [INFO] Date & Time: 2025-03-10 15:54:39
2025-03-10 15:54:39 [INFO] Tested By: John Doe
2025-03-10 15:54:39 [INFO] Environment: QA Environment, Chrome v123
2025-03-10 15:54:39 [INFO] Steps: See test script for detailed steps.
2025-03-10 15:54:39 [INFO] Expected Result: As described in test case documentation.
2025-03-10 15:54:39 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="next"]'}
2025-03-10 15:54:39 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:39 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547"}} | headers=HTTPHeaderDict({'Content-Length': '128', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:39 [DEBUG] Finished Request
2025-03-10 15:54:39 [DEBUG] Stress navigation iteration: 1
2025-03-10 15:54:39 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:39 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:39 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:39 [DEBUG] Finished Request
2025-03-10 15:54:40 [DEBUG] Stress navigation iteration: 2
2025-03-10 15:54:40 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:40 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:40 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:40 [DEBUG] Finished Request
2025-03-10 15:54:40 [DEBUG] Stress navigation iteration: 3
2025-03-10 15:54:40 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:40 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:40 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:40 [DEBUG] Finished Request
2025-03-10 15:54:40 [DEBUG] Stress navigation iteration: 4
2025-03-10 15:54:40 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:40 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:40 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:40 [DEBUG] Finished Request
2025-03-10 15:54:40 [DEBUG] Stress navigation iteration: 5
2025-03-10 15:54:40 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:40 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:40 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:40 [DEBUG] Finished Request
2025-03-10 15:54:41 [DEBUG] Stress navigation iteration: 6
2025-03-10 15:54:41 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:41 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:41 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:41 [DEBUG] Finished Request
2025-03-10 15:54:41 [DEBUG] Stress navigation iteration: 7
2025-03-10 15:54:41 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:41 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:41 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:41 [DEBUG] Finished Request
2025-03-10 15:54:41 [DEBUG] Stress navigation iteration: 8
2025-03-10 15:54:41 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:41 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:41 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:41 [DEBUG] Finished Request
2025-03-10 15:54:41 [DEBUG] Stress navigation iteration: 9
2025-03-10 15:54:41 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:41 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:41 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:41 [DEBUG] Finished Request
2025-03-10 15:54:42 [DEBUG] Stress navigation iteration: 10
2025-03-10 15:54:42 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:42 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:42 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:42 [DEBUG] Finished Request
2025-03-10 15:54:42 [DEBUG] Stress navigation iteration: 11
2025-03-10 15:54:42 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:42 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:42 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:42 [DEBUG] Finished Request
2025-03-10 15:54:42 [DEBUG] Stress navigation iteration: 12
2025-03-10 15:54:42 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:42 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:42 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:42 [DEBUG] Finished Request
2025-03-10 15:54:42 [DEBUG] Stress navigation iteration: 13
2025-03-10 15:54:42 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:42 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:42 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:42 [DEBUG] Finished Request
2025-03-10 15:54:43 [DEBUG] Stress navigation iteration: 14
2025-03-10 15:54:43 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:43 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:43 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:43 [DEBUG] Finished Request
2025-03-10 15:54:43 [DEBUG] Stress navigation iteration: 15
2025-03-10 15:54:43 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:43 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:43 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:43 [DEBUG] Finished Request
2025-03-10 15:54:43 [DEBUG] Stress navigation iteration: 16
2025-03-10 15:54:43 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:43 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:43 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:43 [DEBUG] Finished Request
2025-03-10 15:54:43 [DEBUG] Stress navigation iteration: 17
2025-03-10 15:54:43 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:43 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:43 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:43 [DEBUG] Finished Request
2025-03-10 15:54:44 [DEBUG] Stress navigation iteration: 18
2025-03-10 15:54:44 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:44 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:44 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:44 [DEBUG] Finished Request
2025-03-10 15:54:44 [DEBUG] Stress navigation iteration: 19
2025-03-10 15:54:44 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:44 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:44 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:44 [DEBUG] Finished Request
2025-03-10 15:54:44 [DEBUG] Stress navigation iteration: 20
2025-03-10 15:54:44 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click {}
2025-03-10 15:54:44 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element/f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5547/click HTTP/1.1" 200 0
2025-03-10 15:54:44 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:44 [DEBUG] Finished Request
2025-03-10 15:54:44 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/element {'using': 'css selector', 'value': '[id="picture"]'}
2025-03-10 15:54:44 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/element HTTP/1.1" 200 0
2025-03-10 15:54:44 [DEBUG] Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5551"}} | headers=HTTPHeaderDict({'Content-Length': '128', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:44 [DEBUG] Finished Request
2025-03-10 15:54:44 [DEBUG] POST http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d/execute/sync {'script': '/* getAttribute */return (function(){return (function(){var d=this||self;function f(a,b){function c(...', 'args': [{'element-6066-11e4-a52e-4f735466cecf': 'f.E16415D096F482CA2D75A36DAB17E16D.d.66541F0746E1F5D6A27AAF8979E8210A.e.5551'}, 'src']}
2025-03-10 15:54:44 [DEBUG] http://localhost:49719 "POST /session/9daa00d7f734a1208184110a60ee3b9d/execute/sync HTTP/1.1" 200 0
2025-03-10 15:54:44 [DEBUG] Remote response: status=200 | data={"value":"https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG"} | headers=HTTPHeaderDict({'Content-Length': '124', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:44 [DEBUG] Finished Request
2025-03-10 15:54:44 [INFO] Final picture src after stress navigation: https://github-pages.senecapolytechnic.ca/see600/Assignments/Assignment4/Webpage/images/5906ChurchillMeadows.PNG
2025-03-10 15:54:44 [INFO] Status: Pass
2025-03-10 15:54:44 [INFO] Notes: N/A
2025-03-10 15:54:44 [INFO] Screenshot: (Attach screenshot if applicable)
2025-03-10 15:54:44 [INFO] Log File: (Refer to log output)
2025-03-10 15:54:44 [INFO] Issue: N/A
2025-03-10 15:54:44 [INFO] Resolution: N/A
2025-03-10 15:54:44 [INFO] =================================
2025-03-10 15:54:44 [INFO] [RE-05] - END test
2025-03-10 15:54:44 [INFO] 
2025-03-10 15:54:44 [INFO] Closing WebDriver...
2025-03-10 15:54:44 [DEBUG] DELETE http://localhost:49719/session/9daa00d7f734a1208184110a60ee3b9d {}
2025-03-10 15:54:44 [DEBUG] http://localhost:49719 "DELETE /session/9daa00d7f734a1208184110a60ee3b9d HTTP/1.1" 200 0
2025-03-10 15:54:44 [DEBUG] Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'Content-Length': '14', 'Content-Type': 'application/json; charset=utf-8', 'cache-control': 'no-cache'})
2025-03-10 15:54:44 [DEBUG] Finished Request
2025-03-10 15:54:44 [INFO] WebDriver closed.
(venv) (base) tieuma@Tieus-MacBook-Pro A4 % 

```