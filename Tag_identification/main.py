import urllib.request
from bs4 import  BeautifulSoup #Handling or Parsing html files
import nltk
nltk.download('stopwords')  #'or','was','the','is',etc... extracted lib
from nltk.corpus import stopwords

#Get the info from online websides
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/TATA')
html = response.read()
#print(html)

soup=BeautifulSoup(html,'html5lib')     #Remove unnessery space in text
text=soup.get_text(strip=True)
#print(text)

tokens=[t for t in text.split()]
#print(tokens)

sr=stopwords.words('english')   #Remove 'is','it','the',etc...
clean_token=tokens[:]   #Get the token 

for token in tokens:
    if token in stopwords.words('english'):
        clean_token.remove(token) 

#print(clean_token)
freq=nltk.FreqDist(clean_token)
for key,val in freq.items():
    print(str(key)+':'+str(val))

freq.plot(20,cumulative=False)
