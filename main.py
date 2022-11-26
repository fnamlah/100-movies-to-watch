import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")

URL = response.text

# print(movies_webpage)

soup = BeautifulSoup(URL, "html.parser")

titles = soup.find_all(name="h3", class_="title")

# titles_text = [title.getText() for title in titles]
for title in titles:
    print(title.getText())
# print(title_div)

"""
echo "# workout-tracking" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
"""