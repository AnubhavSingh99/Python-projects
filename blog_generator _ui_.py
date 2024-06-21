import textwrap
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
from IPython.display import Markdown

import google.generativeai as genai

try:
    genai.configure(api_key='AIzaSyBmYQ9bVE3TEOuICBntcmOZ8qOQS86oGmY')
except Exception as e:
    messagebox.showerror("API Key Error", str(e))
    exit()

model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_content():
    inp = entry.get()
    prp = "Write a paragraph about the following topic: " + inp
    try:
        response = model.generate_content(prp)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(response.text))
    except Exception as e:
        messagebox.showerror("Content Generation Error", str(e))

window = tk.Tk()
window.title("Blog Topic Generator")

style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))

entry_label = ttk.Label(window, text="Enter your blog topic:")
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry = ttk.Entry(window, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(window, text="Generate", command=generate_content)
generate_button.grid(row=0, column=2, padx=10, pady=10)

result_label = ttk.Label(window, text="Generated Paragraph:")
result_label.grid(row=1, column=0, padx=10, pady=10)
result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

head = ttk.Label(window, text="Made by Anubhav Singh")
head.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
