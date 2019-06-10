import requests
import pandas as pd
from bs4 import BeautifulSoup  

def book_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser') 

    #ISBN
    #print (isbn)

    #Book Title
    title = soup.find_all('title')
    s = '[<title>'
    e = '</title>]'
    title = str(title[0])
    title = title[title.find(s)+len(s):title.find(e)-len(e)]
    print (title)

    #Author
    #print(author)

    #Origin
    ori = '港版'

    #Publisher

    #print (pub)

    #Publishing date

    #print(pub_date)

    #Catagories

    #print(cat)
          
    #Price

    #print(price)
    #print(unitprice)

    #return ([isbn,'', title, '', author, ori, pub, pub_date, cat, price, unitprice, url])

def main():
    book = []
    
    url=input('Enter url(click q to quit): ')
    print('\n')
    book_data(url)
    
    #while url != 'q':
    #    book.append(book_data(url))
    #    url=input('Enter url(click q to quit): ')

    #df = pd.DataFrame(book, columns=['ISBN', 'Cover', 'Book Title', 'Intro', 'Author', 'Origin', 'Publisher', 'PubDate', 'Catagories', 'Ori Price', 'Unit Price', 'url'])
    #df.to_csv('book.csv', index=False, encoding='utf-8-sig')
    
main()





