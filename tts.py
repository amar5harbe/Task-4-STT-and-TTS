#!/usr/bin/env python
# coding: utf-8

# ## install

# In[3]:


get_ipython().system('pip install ibm_watson')


# ## Authenticate

# In[7]:


url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/3f784e7b-41f2-4440-a69f-ed785c5850c9'
apikey = 'zVs6ERS1z8skVAxwCfA9ydnP2HSfafLP6E88KRHj4NZx'


# In[8]:


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[9]:


# Setup Service
authenticator = IAMAuthenticator(apikey)
# New TTS Service 
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)


# ## convert to string

# In[11]:


with open('./speech.mp3', 'wb') as audio_file:
        res = tts.synthesize('Converting is Done successfully', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)


# In[ ]:





# In[ ]:




