from selenium import webdriver
import time


def main():
    email = input("Please enter your e-mail address: ")
    get_results(email)


def get_results(email):
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver_path = "geckodriver.exe"
    browser = webdriver.Firefox(executable_path=driver_path, options=options)

    url = 'https://haveibeenpwned.com/'

    browser.get(url)
    search_box = browser.find_element_by_id("Account")
    search_box.send_keys(email)
    search_box.submit()
    time.sleep(3)
    if browser.find_element_by_class_name("pwnTitle").text:
        print(browser.find_element_by_class_name("pwnTitle").text)
    else:
        print(browser.find_element_by_xpath('//*[@id="pwnedWebsiteBanner"]/div/div/div[1]/h2').text)

    print(browser.find_element_by_id("pwnCount").text + "\n\n")
    pwned_list = browser.find_elements_by_class_name("col-sm-10")
    for element in pwned_list:
        print(element.text + "\n")
    browser.quit()


if __name__ == '__main__': main()