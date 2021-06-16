#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns


# In[22]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


# In[66]:


import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[2]:


import yagmail


# In[8]:


receiver = "roybiswajit010@gmail.com"
body = "Hello there from Yagmail"
filename = "cheque.pdf"

yag = yagmail.SMTP("roybiswajit010@gmail.com")
yag.send(to=receiver,subject="Yagmail test with attachment",contents=body, attachments=filename)


# In[ ]:




