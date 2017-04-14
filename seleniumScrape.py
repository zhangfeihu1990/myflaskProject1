# -*- encoding:UTF-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
# driver.get("http://example.webscraping.com/search")
# driver.find_element_by_id('search_term').send_keys('.')
# js = "document.getElementById('page_size').options[1].text='1000'"
# driver.execute_script(js)
# driver.find_element_by_id('search').click()
# links = driver.find_element_by_css_selector('#results a')
# countries = [link.text for link in links]
# print countries


driver.get("http://www.ziroom.com/z/nl/z3-x1-a2-s5%E5%8F%B7%E7%BA%BF-t%E5%A4%A9%E9%80%9A%E8%8B%91%E5%8D%97.html")
links = driver.find_element_by_css_selector('#houseList a.t1')
print links
# for link in links:
#     print link