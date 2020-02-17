import requests
from pyquery import PyQuery as pq

def main():
    # pass
    response = requests.get('http://andrei.ase.ro')
    html = response.text
    dom = pq(html)
    elements = dom('a')
    for element in elements:
        print(pq(element).text())

if __name__ == "__main__":
    main()

# pip install pyquery
# pip install scrapy
# mkdir scrapy-projects
# scrapy startproject ziare
# scrapy genspider adevarul adevarul.ro
# scrapy runspider adevarul