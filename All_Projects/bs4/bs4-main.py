from bs4 import BeautifulSoup
import requests
# with open("bs4-html.html", encoding="utf-8") as my_website:
#     content = my_website.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# # to get content inside the title
# print(soup.title.string)
# # type of content
# print(soup.title.name)
# # to get first of different tags in html file
# print(soup.h1)
# # to get all tags in specified tags
# all_tags = (soup.find_all(name="a"))
# for tag in all_tags:
#     print(tag.string)
#     print(tag.get("href"))
#
# print(soup.find(name="h1", id="name"))

# response = requests.get(url="https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)
# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = (article_tag.getText())
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
#
# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# # print(article_texts)
# # print(article_links)
# # print(article_upvote)
#
# max_vote = max(article_upvote)
# largest_index = article_upvote.index(max_vote)
#
# print(article_texts[largest_index])
# print(article_links[largest_index])
# print(max_vote)

# 100 Movies To Watch

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies"
                            "/features/best-movies-2/")
movie_web_page = response.text
print(movie_web_page)

# soup = BeautifulSoup(movie_web_page, "html.parser")
# movies_list = []
# movies_title = soup.find_all(name="h3", class_="title")
# for movie in movies_title:
#     title = movie.getText()
#     movies_list.append(title)
#
# movies = movies_list[::-1]
# print(movies)
# with open("my_movies_list.txt", "w") as movie_text:
#     for movie in movies:
#         movie_text.write(f"{movie}\n")




