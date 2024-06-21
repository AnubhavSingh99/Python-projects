import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key='AIzaSyBmYQ9bVE3TEOuICBntcmOZ8qOQS86oGmY')

model = genai.GenerativeModel('gemini-pro')
inp=input("Enter your blog topic: ")
prp="Write a paragraph about the following topic."+inp
response = model.generate_content(prp)
print(str(response.text))