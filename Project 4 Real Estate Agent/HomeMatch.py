#A starter file for the HomeMatch application if you want to build your solution in a Python program instead of a notebook. 

import os

os.environ["OPENAI_API_KEY"] = "YOUR API KEY"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

from langchain.llms import OpenAI

