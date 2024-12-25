from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open("log.txt","w")

#driver = webdriver.Chrome()

option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

#end of setup

#Sc functions-----------

def set_up():
    driver.get('https://www.saucedemo.com')
    driver.maximize_window()

def login():
    user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login="standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password="secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

    login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_button.click()
    file.write("Success click login\n")

def login_wiht_enter():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

  #  login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
   # login_button.click()

    user_pass.send_keys(Keys.ENTER)
    file.write("Success Enter login\n")


def fake_login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce1"
    user_pass.send_keys(password)
    file.write("Success write fake password\n")

    login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_button.click()
    file.write("Success click login\n")


#End of Sc functions-------------
#Tests----------------------

def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_context_after_login_is_correct():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    print(datetime.datetime.now())
    driver.save_screenshot(f"sc_real_login\\screenshot_test_context_after_login_is_correct_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")

    assert correct_text == current_text.text,"test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")

def test_fake_login_label():
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text,"test_fake_login_label is Failed"
    file.write("test_fake_login_label is OK \n")

#End of tests

# main block
def sc_real_login_with_enter():
    set_up()
    login_wiht_enter()

    test_login_redirect()
    test_context_after_login_is_correct()

def sc_fake_login():
    set_up()
    fake_login()
    test_fake_login_label()

def sc_real_login():
    set_up()
    login()

    test_login_redirect()
    test_context_after_login_is_correct()

#sc_fake_login()

sc_real_login()

file.close()

