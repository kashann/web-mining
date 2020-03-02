from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path = './chromedriver.exe')
    # driver = webdriver.Firefox(executable_path = './geckodriver.exe')
    driver.set_window_size(800, 600)
    driver.get('http://andrei.ase.ro')
    element = driver.find_element_by_css_selector('a[href^=wmda]')
    print(element.text)
    driver.quit()

if __name__ == "__main__":
    main()