import os
import requests
import lxml
import bs4
os.chdir("/Users/Akshat/Desktop")
os.mkdir("SoftCom")
os.chdir("/Users/Akshat/Desktop/SoftCom")
os.mkdir("India")
os.mkdir("World")
os.mkdir("Business")
os.mkdir("Homepage")

urli=['https://timesofindia.indiatimes.com/india','https://timesofindia.indiatimes.com/world',
'https://timesofindia.indiatimes.com/business','https://timesofindia.indiatimes.com/']
base_url='https://timesofindia.indiatimes.com/'
path=["/Users/Akshat/Desktop/SoftCom/India","/Users/Akshat/Desktop/SoftCom/World",
"/Users/Akshat/Desktop/SoftCom/Business","/Users/Akshat/Desktop/SoftCom/Homepage"]
#ITERATING THROUGH EACH URL AND FINDING HYPERLINK AND ACCESSING HYPERLINKS IN A SINGLE GO
for i in range(4):
    current_url=urli[i]
    url=requests.get(current_url)
    os.chdir(path[i])
    soup=bs4.BeautifulSoup(url.text,'html.parser')
    title=soup.find('div',{'class':'main-content'})
    if title==None:
        title=soup.find('div',{'id':'content'})
    mainTags=title.findAll('a',{'class':None})
    Dict={}
    for page in mainTags:
        href=page.get('href')
        if (href==None):
            continue
        if ('https://' not in href):
            href=base_url+href
        if (("photogallery" not in href) and ('videos' not in href)):
            Dict[page.get("title")]=href
        
    for titleh in Dict:    
        try:
            write_title=titleh+'\n\n'
            text=''
            write_date=''
            hyperlink=Dict[titleh].strip()
            content=requests.get(hyperlink)
            soup=bs4.BeautifulSoup(content.text,'html.parser')
            date=soup.find('div',{'class':'_3Mkg- byline'})
            if date.text!=None:
                write_date='Source and Date: '+date.text+'\n\n'
            roughText=soup.find('div',{'class':'ga-headlines'})
            text=roughText.text
            f=open('%s.txt' %titleh,'w',encoding='utf-8')
            f.writelines(write_title+write_date+text)
            f.close()
        except:
            pass
    
