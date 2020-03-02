from selenium import webdriver

def main():
    with open('script.js') as f:
        script = f.read()
    driver = webdriver.Chrome(executable_path = './chromedriver.exe')
    driver.set_window_size(800, 600)
    driver.get('http://andrei.ase.ro')
    result = driver.execute_script(script)
    print(result)
    driver.quit()

if __name__ == "__main__":
    main()