# from selenium import webdriver
# browser = webdriver.Chrome()
from selenium import webdriver
b = webdriver.PhantomJS()
b.get('https://www.baidu.com')
print(b.current_url)
'''
ssr://bWYxLnFxc3NyLnRvcDo1NzIwNjpvcmlnaW46cmM0LW1kNTpwbGFpbjpibkJ0VkVOTC8_b2Jmc3BhcmFtPSZwcm90b3BhcmFtPSZyZW1hcmtzPTU3MlI1NnVaNUxpSzZaMmk1TGlBNTV1MDVweUo1WVdONkxTNTU1cUVjM055Q25oNmMzTnlMblJ2Y0FybXM2amxob3pvdEtibGo3Zmt2Yl9ubEtnJmdyb3VwPTVhNlk1NzJST25oNmMzTnlMblJ2Y0E
'''
