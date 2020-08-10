from selenium import webdriver
from PIL import Image

driver = webdriver.Chrome()

url = "https://www.youtube.com/channel/UCuxkk3TD7cfPR08JEWVyXZA"

driver.get(url)

driver.save_screenshot("image.png")

image = Image.open("image.png")

image.show()