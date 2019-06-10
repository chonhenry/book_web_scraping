import requests
import pandas as pd
from bs4 import BeautifulSoup  

def book_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser') 

    #ISBN
    results = soup.find_all('meta', attrs={'itemprop':'productID'})
    if len(results)==0:
        return [1,1,1,1,1,1,1,1,1,1,1,url]
    #print(results)
    s = '<meta content="isbn:'
    e = '" itemprop='
    isbn = str(results[0])
    isbn = isbn[isbn.find(s)+len(s):isbn.rfind(e)]
    #print (isbn)

    #Book Title
    results = soup.find_all('h1', attrs={'itemprop':'name'})
    s = '<h1 itemprop="name">'
    e = '</h1>'
    title = str(results[0])
    title = title[title.find(s)+len(s):title.rfind(e)]
    #print (title)

    #Author
    results = soup.find_all('meta')
    content = str(results[3])
    s = "作者："
    s_i = content.find(s)
    author = ""
    for i in content[s_i+3:-1]:
        if i=='，':
            break
        author+=i
    #print(author)

    #Origin
    ori = '台版'

    #Publisher
    results = soup.find_all('span', attrs={'itemprop':'brand'})
    s = '<span itemprop="brand">'
    e = '</span>'
    pub = str(results[0])
    pub = pub[pub.find(s)+len(s):pub.rfind(e)]
    #print (pub)

    #Publishing date
    results = soup.find_all('meta')
    content = str(results[3])
    s = "出版日期："
    s_i = content.find(s)
    pub_date = ""
    for i in content[s_i+5:-1]:
        if pub_date.count('/') > 1:
            pub_date = pub_date[:-1]
            break
        pub_date+=i
    #print(pub_date)

    #Catagories
    results = soup.find_all('ul', attrs={'class':'sort'})
    results = str(results[0])
    results = results.split('本書分類')
    results = results[1]
    s = '<span itemprop="brand">'
    e = '</span>'
    c = results.count('/">')
    cat = ""
    while c != 0:
        i = results.find('</a>')
        cat = cat + results[ results.find('/">')+3 : i ] + '>'
        results = results[i+4:]
        c=c-1
    cat = cat[:-1]
    #print(cat)
          
    #Price
    results = soup.find_all('ul', attrs={'class':'price'})
    results = str(results[0])
    i1 = results.find('定價：<em>')
    i2 = results.find('</em>')
    price = int(results[i1+7:i2])
    unitprice = price*0.07
    #print(price)
    #print(unitprice)

    return ([isbn,'', title, '', author, ori, pub, pub_date, cat, price, unitprice, url])

def main():
    book = []
    url=input('Enter url(click q to quit): ')

    while url != 'q':
        book.append(book_data(url))
        url=input('Enter url(click q to quit): ')

    df = pd.DataFrame(book, columns=['ISBN', 'Cover', 'Book Title', 'Intro', 'Author', 'Origin', 'Publisher', 'PubDate', 'Catagories', 'Ori Price', 'Unit Price', 'url'])
    df.to_csv('book.csv', index=False, encoding='utf-8-sig')
    
main()





