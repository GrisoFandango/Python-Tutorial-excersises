import requests
from bs4 import BeautifulSoup
# we get the informations from the url, in this case an html page
response = requests.get("https://stackoverflow.com/questions")
# The Method Beautiful soup allow to read the data avoiding the 'parser' in this case all the html code
soup = BeautifulSoup(response.text, "html.parser")
# we can select specific data usind the CSS selector (we can find it inspecting the page)
question = soup.select(".question-summary")
# print(question[0].get("id", 0))
# print(question[0].select(".question-hyperlink"))
# print(question[0].select_one(".question-hyperlink"))
for question in question:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
