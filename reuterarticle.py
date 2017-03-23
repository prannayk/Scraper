from subprocess import call
from bs4 import BeautifulSoup
import urllib.request

opener = urllib.request.FancyURLopener()

urllist = []
for i in range(10,16):
    for j in range(1,9):
        for k in range(1,9):
            urllist.append( "http://www.reuters.com/resources/archive/us/20"+str(i)+"0"+str(j)+"0"+str(k)+".html")
        for k in range(10,31):
            urllist.append( "http://www.reuters.com/resources/archive/us/20"+str(i)+"0"+str(j)+str(k)+".html")
    for j in range(10,12):
        for k in range(1,9):
            urllist.append("http://www.reuters.com/resources/archive/us/20"+str(i)+str(j)+"0"+str(k)+".html")
        for k in range(10,31):
            urllist.append("http://www.reuters.com/resources/archive/us/20"+str(i)+str(j)+str(k)+".html")

list2 = ['3M', 'american express','ge','', 'apple', 'boeing', 'caterpillar', 'chevron', 'cisco', 'coca-cola', 'disney', 'exxon', 'general electric', 'goldman', 'home depot', 'ibm', 'intel', 'johnson', 'jpmorgan', 'mcdonald', 'merck', 'microsoft', 'nike', 'pfizer', 'procter', 'gamble', 'verizon', 'visa', 'walmart']
urllist = ["http://www.reuters.com/resources/archive/us/20101208.html"]
linklist = []
for url in urllist:
    f = opener.open(url)
    print("read page")
    content = BeautifulSoup(f.read(),'html.parser')
    print("parsed")
    for element in content.find_all("div","headlineMed"):
        for stuff in list2:
            if(str(element.a.text).find(stuff)):
                linklist.append(stuff+element.a['href'])
                break
print("hahahaha")
for links in linklist:
    f = opener.open(links)
    content = BeautifulSoup(f.read(), 'html.parser')
    date = content.find_all("span", "timestamp")[0]
    date = data.split(" | ")[0]
    head = content.find_all("h1","article-headline")[0]
    call(["mkdir","article_data/"+date])
    article = content.find(id="article-text")
    text = ""
    for things in article.find_all("p"):
        text= text + things.text
    text_file = open("article_data/"+date+"/"+head, "w")
    textfile.write(text)
    text_file.close()
