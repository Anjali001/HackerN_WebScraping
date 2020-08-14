import requests # allows to download the html from beuatifulSoup
from bs4 import BeautifulSoup # allowss to use html to grab data /scape it
import pprint
#Grabbing data 
links=[]
subtext=[]
for i in range(1,20):
    res=requests.get('https://news.ycombinator.com/news?p={}',i)
    soup = BeautifulSoup(res.text,'html.parser')
    links +=soup.select('.storylink')
    subtext +=soup.select('.subtext')
#Parsing
# Parses for XML/lxml... too
#print(soup.body.contents)
#print(soup.body)
#print(soup)
#print(soup.find_all('div'))
#print(soup.find_all('a'))
#print(soup.title)
#print(soup.a)
#print(soup.find('a'))
#print(soup.select('.score')) # dot is for class
#print(soup.select('#score_24005443'))
#links=soup.select('.storylink')
#subtext=soup.select('.subtext')
#print(votes[0])
#print(links[0])

def sort_by_votes(hnlist):
    return sorted(hnlist,key= lambda k : k['votes'],reverse = True)

def create_custom_hn(links,subtext):
    hn=[]
    for index,item in enumerate(links):
        title=item.getText() # title = links[index].getText()
        href=item.get('href',None) # Same as above
        votes=subtext[index].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points',''))
            if points >99: #Filtering #then sorting
                hn.append({'title': title , 'link' : href , 'votes' : points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(links,subtext))