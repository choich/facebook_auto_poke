from selenium import webdriver
from time import sleep

user_id = ""  # user_id
user_pw = ""  # user_password

driver = webdriver.PhantomJS()  # use PhantomJS
driver.get("https://www.facebook.com/pokes")  # facebook foke url

# find form and input
form = driver.find_element_by_id("login_form")

elem = form.find_element_by_id("email")
elem.send_keys(user_id)

elem = form.find_element_by_id("pass")
elem.send_keys(user_pw)

elem.submit()

sleep(0.9)

# check new foke and FOKE!!!
while True:
    driver.get("https://www.facebook.com/pokes")
    new_poke_div = driver.find_element_by_id("u_0_0")
    if new_poke_div.get_attribute("class") == "_6a":
        print("POKE!!!!!!")
        poke = new_poke_div.find_element_by_tag_name("a")
        poke.click()
    sleep(0.5)
