#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install newspaper3k


# In[2]:


pip install nltk


# In[2]:


pip install tensorflow


# In[2]:


import nltk
nltk.download('punkt')


# In[1]:


from newspaper import Article
import nltk
url="https://www.bbc.com/mundo/articles/c899v4372pqo"
article=Article(url,language='es')
article.download()


# In[2]:


from newspaper import Article
#url = "https://www.bbc.com/mundo/articles/c899v4372pqo"
#url="https://www.bbc.com/arabic/articles/ck77lg9llz3o"
url="https://www.bbc.com/hindi/articles/czrjy4l9xxmo"
toi_article = Article(url, language="hi") 
toi_article.download()
toi_article.parse()
toi_article.nlp()
#print("Author:",toi_article.author)
print("Article's Title:",toi_article.title)
print("n")
'''print("Article's Text:")
print(toi_article.text)
print("n")'''
print("Article's Summary:")
print(toi_article.summary)
print("n")
#print("Article's Keywords:")
#print(toi_article.keywords)
k=toi_article.summary


# In[10]:


pip install googletrans


# In[15]:


pip install deep-translator


# In[5]:


from deep_translator import GoogleTranslator
from langdetect import detect
var=GoogleTranslator(target='ta').translate(k)
print(var)


# In[1]:


pip install pyttsx3


# In[3]:


import pyttsx3
text=pyttsx3.init()
text.say(var)
text.runAndWait()


# In[1]:


pip install gTTS


# In[6]:


import os
from gtts import gTTS
from langdetect import detect
mytest=var
myobj=gTTS(text=mytest,lang=detect(var),slow=True)
myobj.save("library.mp3")


# In[8]:


os.system("library.mp3")


# In[14]:


from langdetect import detect
print(detect("ఉక్రెయిలోని విద్యుత్ గ్రిడ్‌ను లక్ష్యంగా చేసుకుని"))


# In[ ]:




