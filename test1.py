# from selenium import webdriver
# browser = webdriver.Chrome()
from selenium import webdriver
b = webdriver.PhantomJS()
b.get('https://www.baidu.com')
print(b.current_url)
