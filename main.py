import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")

URL = response.text

# print(movies_webpage)

soup = BeautifulSoup(URL, "html.parser")

titles = soup.find_all(name="h3", class_="title")

titles_text = []
for title in titles:
    titles_text.append(title.getText())

titles_text.reverse()
print(titles_text)

with open("movies.txt", "w") as file:
    for title in titles_text:
        file.write(title)
        file.write("\n")

"""
echo "# workout-tracking" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
"""