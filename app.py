import streamlit as st
import numpy as np
import transformers
import torch
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import DistilBertTokenizer, DistilBertModel
import new  


def functional_level_prediction(text):
   result = new.find_functional_label(text)
   return result

user_input = st.text_area('enter profile description to get its functional level')
print(type(user_input))
button = st.button('predict')

if user_input and button:
    print(type(user_input))
    result = functional_level_prediction(user_input) 
    st.write('functional_level: ',result)
