import urllib.request

url = input("Enter Image URL")

try:
    urllib.request.urlretrieve(url,"downloadedimage.png")
    print("Image Downloaded")
except:
    print("Error")