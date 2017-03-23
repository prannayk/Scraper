from subprocess import call
from bs4 import BeautifulSoup
import requests

opener = requests.get

urllist = []
for i in range(10,16):
    for j in range(1,9):
        for k in range(1,9):
            urllist.append( "https://www.reuters.com/resources/archive/us/20"+str(i)+"0"+str(j)+"0"+str(k)+".html")
        for k in range(10,31):
            urllist.append( "https://www.reuters.com/resources/archive/us/20"+str(i)+"0"+str(j)+str(k)+".html")
    for j in range(10,12):
        for k in range(1,9):
            urllist.append("https://www.reuters.com/resources/archive/us/20"+str(i)+str(j)+"0"+str(k)+".html")
        for k in range(10,31):
            urllist.append("https://www.reuters.com/resources/archive/us/20"+str(i)+str(j)+str(k)+".html")

list2 = ['3M', 'american express','ge','', 'apple', 'boeing', 'caterpillar', 'chevron', 'cisco', 'coca-cola', 'disney', 'exxon', 'general electric', 'goldman', 'home depot', 'ibm', 'intel', 'johnson', 'jpmorgan', 'mcdonald', 'merck', 'microsoft', 'nike', 'pfizer', 'procter', 'gamble', 'verizon', 'visa', 'walmart']
urllist = ["https://www.reuters.com/resources/archive/us/20101208.html"]
linklist = []
for url in urllist:
    f = opener(url,verify=False)
    print("read page")
    content = BeautifulSoup(f.content,'html.parser')
    print("parsed")
    for element in content.find_all("div","headlineMed"):
        for stuff in list2:
            if(str(element.a.text).find(stuff)):
                linklist.append(element.a['href'])
                break
print("hahahaha")
print(linklist[0])
for links in linklist:
    t = opener(links, verify=False)
    print("opened")
    content = BeautifulSoup(t.content, 'html.parser')
    print(content)
    date = content.find_all("span", "timestamp")[0]
    date = date.split(" | ")[0]
    head = content.find_all("h1","article-headline")[0]
    call(["mkdir","article_data/"+date])
    article = content.find(id="article-text")
    text = ""
    for things in article.find_all("p"):
        text= text + things.text
    text_file = open("article_data/"+date+"/"+head, "w")
    textfile.write(text)
    text_file.close()
