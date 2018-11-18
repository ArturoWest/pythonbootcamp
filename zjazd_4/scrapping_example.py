from requests import get
from bs4 import BeautifulSoup


url = "https://helion.pl/ksiazki/deep-learning-uczenie-glebokie-z-jezykiem-python-sztuczna-inteligencja-i-sieci-neuronowe-valentino-zocca-gianmario-spacagna-daniel-slater,deelea.htm#format/d"

respone = get(url)

print(respone)
print(dir(respone))
print(respone.text)

html_soup = BeautifulSoup(respone.text, 'html.parser')

print(html_soup)

books = html_soup.find_all('div', class_="book-info")
print(len(books))

for b in books:
    print(b.a.text)


print(books[0])
