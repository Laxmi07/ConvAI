#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Title of the app
st.title('Hello Streamlit!')

# Text input from the user
user_input = st.text_input('Enter some text:')

# Display the user input
st.write(f'You entered: {user_input}')

