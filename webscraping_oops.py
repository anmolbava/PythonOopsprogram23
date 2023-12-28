import requests
import bs4
# we need to download and install packages requests and beautifulsoup - pip install requests
url = input("please input your url") # asks user to input target website to be scrapped
response=requests.get(url) # response variable is a object that stores response from request package from get method which passes url as a parameter
# print(type(response))
# print(response.text)
filename="temp.html" # creating a temp file for all html tags to be stored from the response object
bs=bs4.BeautifulSoup(response.text,"html.parser") # bs object is of Beautiful soup class which also passes response text and html parser as parameters
formatted_text=bs.prettify() # prettify function is called by the bs object  and stored in the formatted_text variable/object to beautfy the html code scraped from the website

# Once we have the prettify function we can put it in a variable/object called formatted_text,
# Now we need to store the preety formatted scrapped output in the temp.html

with open(filename,"w+", encoding="utf-8") as f:
    f.write(formatted_text)

list_imgs=bs.find_all('img')
print(list_imgs)
# the able list_imgs variable stores only imgs strings in the source code
# and then finally prints imgs tags found in temp.html scrapped