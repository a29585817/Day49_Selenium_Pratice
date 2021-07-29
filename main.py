from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver = "C:/Users/Meng Chien/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2648204134&geoId=106907071&keywords=python&location=%E5%8F%B0%E7%81%A3%20Taipei%20City%20%E5%8F%B0%E5%8C%97&originalSubdomain=tw&position=1&pageNum=0")

driver.maximize_window()
log_in_botton = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
log_in_botton.click()
# -------------------------------------------

time.sleep(3)

mail = "main_account"
password = "password"

user_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")
submit = driver.find_element_by_class_name("login__form_action_container")
user_input.send_keys(mail)
password_input.send_keys(password)
submit.click()
# -------------------------------------------
time.sleep(3)
send_job_keyword = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember41"]')
send_job_keyword.clear()
send_job_keyword.send_keys("Market")
location = driver.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember41"]')
location.clear()
location.send_keys("Tokyo")
submit_keywoed = driver.find_element_by_xpath('//*[@id="global-nav-search"]/div/div[2]/button[1]')
submit_keywoed.click()
# -------------------------------------------
time.sleep(3)
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        PHONE = "Phone_number"
        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")

        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()