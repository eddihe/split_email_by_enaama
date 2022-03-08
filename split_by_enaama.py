#! python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:43:31 2022

@author: Eddih Enaama
"""

# -*- coding: utf-8 -*-


import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import re
import urllib.request

root = tk.Tk(className='split_emails_users')

# set_color
# root['background']='white'

canvas = tk.Canvas(root)
canvas.grid(columnspan=3, rowspan=3)

# logo
urllib.request.urlretrieve('https://i.ibb.co/CJVWVz4/font.png', 'font.png')
logo = Image.open('font.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columns=1, row=0)

# instructions
instruction = tk.Label(root, text="Select you re file text you want to\n split it to email and username: ",
                       font="Relaway")

instruction.grid(columnspan=3, column=0, row=1)


# create function
def open_file():
    file = askopenfile(parent=root, title="Choose a file", filetype=[("Text File", '*.txt')])
    if file:
        string_email = ""
        string_user = ""
        for l in file.readlines():
            l1 = re.sub('[a-z]*://', '', l)
            l1 = l1.replace(' ', '')
            l1 = l1.replace('\n', '')
            l2 = l1 + "@"
            try:
                # extract email in string_email
                email_pass = re.compile(r'''([a-zA-Z0-9._%+-@]+    #extract email adresse user@exemple.com
                                        :[a-zA-Z0-9-._]+           #extract password after :untile@
                                        ([@]))''', re.VERBOSE)
                # email_pass = re.compile(r'^.*@.*:.*@',re.DOTALL | re.IGNORECASE | re.VERBOSE)
                moo = email_pass.search(l2)
                moo_index = moo.group()[:-1]
                if moo_index.find('@') > 0:
                    string_email += moo_index
                    string_email += "\n"
                else:
                    string_user += moo_index
                    string_user += "\n"

            except AttributeError:
                pass

        # text_book
        text_file = tk.Text(root, height=5, width=40, padx=15, pady=15)
        text_file.insert(1.0, string_email)
        text_file.grid(column=0, row=1)

        text_file = tk.Text(root, height=5, width=40, padx=15, pady=15)
        text_file.insert(1.0, string_user)
        text_file.grid(column=0, row=2)


# browse_button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), bg="#20bebe", fg="white", height=2,
                       width=15)
browse_text.set("Browse")
browse_btn.grid(column=0, row=3)

# root
root.mainloop()
