from urllib.request import  Request,urlopen
from bs4 import BeautifulSoup
import requests
root = "https://www.google.com/"
link= "https://www.google.com/search?q=war+of+the+roses&biw=1366&bih=625&tbs=qdr%3Ad&tbm=nws&sxsrf=AOaemvKZqD6m0ux42YLS03ZZSjGpiXgRhw%3A1633929107793&ei=k8djYaToL8yfgQaKmIzgAw&oq=war+of&gs_l=psy-ab.3.0.0i433i273k1l2j0i512k1j0i512i433k1j0i512k1j0i512i433k1l2j0i67k1l2j0i512k1.181063.246186.0.248397.22.12.0.0.0.0.228.1354.2j7j1.11.0....0...1c.1.64.psy-ab..14.7.1050.0..0i433i67k1j0i273k1j0i512i433i131k1j0i433i131k1.132.WxmLuQ2iDEY"
req =Request(link,headers={'User-Agent': 'Mozilla/5.0'})
webpage= urlopen(req).read()

with requests.Session() as c:
    soup = BeautifulSoup(webpage,'html5lib')
        # print(soup)
    for item in soup.find_all('div',attrs={'class' : "ZINbbc xpd O9g5cc uUPGi"}):

        raw_link = (item.find('a',href=True)['href'])
    #
        link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
            # print(link)
            # print(item)
        title = (item.find('div', attrs={'class':'BNeawe vvjwJb AP7Wnd'}).get_text())
        context = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())
        title =title.replace(",","")
        context = context.replace(",", "")
        time = context.split(" · ")[0]
        cont = context.split(" · ")[1]

        document = open("history_data.csv","a")
        document.write("{}, {}, {}, {} \n".format(title,time,cont,link))
        document.close()


